import os
import io
import sys
import json
import math
import tempfile
import threading
import webbrowser
import requests
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scipy.ndimage import gaussian_filter
from flask import Flask, request, jsonify, render_template, send_file
from Bio.PDB import PDBParser, MMCIFParser, PPBuilder, is_aa
from Bio.PDB.Polypeptide import protein_letters_3to1
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)

# ── PROCHECK-style Ramachandran region definitions ───────────────────────────
# Regions defined as polygon masks matching PROCHECK's original boundaries
# Most favoured (A,B,L), Additional allowed (a,b,l,p), Generously allowed (~a,~b,~l,~p)

def _make_region_mask(phi_grid, psi_grid, polygons):
    """Rasterize a list of polygons onto the phi/psi grid."""
    from matplotlib.path import Path
    PHI, PSI = np.meshgrid(phi_grid, psi_grid)
    pts = np.column_stack([PHI.ravel(), PSI.ravel()])
    mask = np.zeros(PHI.shape, dtype=bool)
    for poly in polygons:
        p = Path(poly)
        mask |= p.contains_points(pts).reshape(PHI.shape)
    return mask


def _build_rama_regions():
    """
    Build three region masks: favoured, allowed, generously_allowed.
    Coordinates approximate PROCHECK boundaries for non-Gly, non-Pro residues.
    """
    phi = np.linspace(-180, 180, 720)
    psi = np.linspace(-180, 180, 720)

    # ── Most favoured regions (red in PROCHECK, dark blue in our colour scheme) ──
    # Region A: alpha-helix
    A = [(-160,-60),(-160,-20),(-140,-20),(-120,-10),(-100,-10),
         (-80,-20),(-60,-20),(-60,-80),(-80,-100),(-100,-100),
         (-140,-80),(-160,-80),(-160,-60)]
    # Region B: beta-sheet
    B = [(-180,100),(-180,180),(-100,180),(-100,160),(-80,160),
         (-60,140),(-60,100),(-80,80),(-100,80),(-120,80),
         (-140,80),(-160,80),(-180,100)]
    # Region L: left-handed helix
    L = [(30,20),(30,100),(80,100),(80,20),(30,20)]

    favoured_polys = [A, B, L]

    # ── Additional allowed (yellow in PROCHECK) ──
    # Expanded A
    Aa = [(-180,-60),(-180,0),(-160,20),(-140,20),(-120,10),(-100,10),
          (-80,10),(-60,10),(-40,10),(-40,-20),(-60,-20),(-60,-100),
          (-80,-120),(-100,-120),(-140,-100),(-160,-100),(-180,-80),(-180,-60)]
    # Expanded B
    Ba = [(-180,80),(-180,180),(-40,180),(-40,140),(-60,140),
          (-60,100),(-80,80),(-100,60),(-140,60),(-160,60),(-180,60),(-180,80)]
    # p region (cis-like)
    Pa = [(40,-60),(40,20),(80,20),(100,0),(100,-60),(80,-80),(40,-60)]
    # ~l
    La = [(20,20),(20,120),(100,120),(100,20),(20,20)]

    allowed_polys = [Aa, Ba, Pa, La]

    # ── Generously allowed (light yellow in PROCHECK) ──
    # Even wider expansions
    Ag = [(-180,-80),(-180,20),(-160,40),(-120,30),(-80,30),
          (-40,20),(-40,-40),(-60,-40),(-60,-120),
          (-100,-140),(-160,-120),(-180,-100),(-180,-80)]
    Bg = [(-180,60),(-180,180),(-20,180),(-20,120),(-60,120),
          (-60,80),(-100,40),(-160,40),(-180,40),(-180,60)]
    Pg = [(20,-80),(20,40),(110,40),(120,-20),(120,-80),(80,-100),(20,-80)]
    Lg = [(10,10),(10,130),(110,130),(110,10),(10,10)]

    generous_polys = [Ag, Bg, Pg, Lg]

    fav  = _make_region_mask(phi, psi, favoured_polys)
    alw  = _make_region_mask(phi, psi, allowed_polys) & ~fav
    gen  = _make_region_mask(phi, psi, generous_polys) & ~fav & ~alw

    return phi, psi, fav, alw, gen


# Cache regions
_RAMA_REGIONS = None

def get_rama_regions():
    global _RAMA_REGIONS
    if _RAMA_REGIONS is None:
        _RAMA_REGIONS = _build_rama_regions()
    return _RAMA_REGIONS


def classify_region(phi, psi):
    """Return 'favoured', 'allowed', 'generous', or 'outlier' for a phi/psi pair."""
    r_phi, r_psi, fav, alw, gen = get_rama_regions()
    # Find nearest grid indices
    i = int(np.clip(round((phi + 180) / 360 * 719), 0, 719))
    j = int(np.clip(round((psi + 180) / 360 * 719), 0, 719))
    if fav[j, i]: return 'favoured'
    if alw[j, i]: return 'allowed'
    if gen[j, i]: return 'generous'
    return 'outlier'


def classify_residue(resname):
    if resname == 'GLY': return 'gly'
    elif resname == 'PRO': return 'pro'
    else: return 'general'


def is_outlier(phi, psi, residue_type='general'):
    if residue_type == 'gly':
        return False
    region = classify_region(phi, psi)
    return region == 'outlier'


def _smart_label_outliers(ax, outliers, phi_range=360, psi_range=360):
    """
    Place outlier labels with collision avoidance.
    Uses a simple grid-based occupancy map to prevent overlaps.
    """
    if not outliers:
        return

    # Sort by distance from origin descending (label most extreme first)
    sorted_out = sorted(outliers, key=lambda r: -(r['phi']**2 + r['psi']**2)**0.5)

    # Track placed label bounding boxes (in data coords)
    placed = []  # list of (x0, y0, x1, y1)
    label_w = 28   # approximate label width in data units
    label_h = 10   # approximate label height in data units

    def overlaps(x, y):
        for (x0, y0, x1, y1) in placed:
            if not (x + label_w < x0 or x > x1 or
                    y + label_h < y0 or y > y1):
                return True
        return False

    def try_offsets(phi, psi):
        """Try multiple offset directions, return first non-overlapping."""
        candidates = [
            (phi + 8,  psi + 8),
            (phi - 8,  psi + 8),
            (phi + 8,  psi - 12),
            (phi - 8,  psi - 12),
            (phi + 18, psi),
            (phi - 18, psi),
            (phi,      psi + 15),
            (phi,      psi - 18),
            (phi + 25, psi + 10),
            (phi - 25, psi + 10),
        ]
        for (tx, ty) in candidates:
            # Keep inside plot
            tx = np.clip(tx, -175, 145)
            ty = np.clip(ty, -175, 165)
            if not overlaps(tx, ty):
                return tx, ty
        # Fallback: just use first candidate clamped
        tx = np.clip(candidates[0][0], -175, 145)
        ty = np.clip(candidates[0][1], -175, 165)
        return tx, ty

    for r in sorted_out:
        tx, ty = try_offsets(r['phi'], r['psi'])
        ax.annotate(
            r['label'],
            xy=(r['phi'], r['psi']),
            xytext=(tx, ty),
            fontsize=6.2,
            color='#bb0000',
            fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.18', facecolor='white',
                      edgecolor='#cc0000', linewidth=0.7, alpha=0.92),
            arrowprops=dict(arrowstyle='->', color='#cc0000',
                            lw=0.65, alpha=0.75,
                            connectionstyle='arc3,rad=0.1'),
            zorder=10
        )
        placed.append((tx, ty, tx + label_w, ty + label_h))


def generate_plot(residues, title="Ramachandran Plot"):
    """Generate a PROCHECK-style Ramachandran plot with stats table below."""

    r_phi, r_psi, fav_mask, alw_mask, gen_mask = get_rama_regions()

    # ── Figure with extra space below for stats table ──
    fig = plt.figure(figsize=(9, 11.5), facecolor='white')
    ax  = fig.add_axes([0.10, 0.28, 0.82, 0.65])   # plot area
    ax.set_facecolor('white')

    # ── Draw PROCHECK-style filled regions ──
    PHI_g, PSI_g = np.meshgrid(r_phi, r_psi)

    # Build RGBA image: colour each pixel by region
    rgba = np.ones((*fav_mask.shape, 4))            # white default
    # Generously allowed — soft pastel cream/silver
    rgba[gen_mask] = [0.91, 0.93, 0.97, 1.0]
    # Additional allowed — pastel steel blue
    rgba[alw_mask] = [0.72, 0.82, 0.93, 1.0]
    # Most favoured — muted teal/slate blue (metallic pastel)
    rgba[fav_mask] = [0.35, 0.57, 0.78, 1.0]

    ax.imshow(rgba, origin='lower', aspect='auto',
              extent=[-180, 180, -180, 180], zorder=1, interpolation='nearest')

    # ── Thin black borders between regions ──
    for mask, lw in [(fav_mask | alw_mask | gen_mask, 0.5),
                     (fav_mask | alw_mask, 0.5),
                     (fav_mask, 0.7)]:
        from scipy.ndimage import binary_erosion
        border = mask & ~binary_erosion(mask)
        ys, xs = np.where(border)
        if len(xs):
            phi_pts = r_phi[xs]
            psi_pts = r_psi[ys]
            ax.scatter(phi_pts, psi_pts, s=0.05, c='#555555', zorder=2,
                       linewidths=0, alpha=0.4)

    # ── Dashed zero lines ──
    ax.axhline(0, color='#666666', linewidth=0.7, linestyle='--', alpha=0.6, zorder=3)
    ax.axvline(0, color='#666666', linewidth=0.7, linestyle='--', alpha=0.6, zorder=3)

    # ── Region letter labels (PROCHECK style) ──
    region_labels = [
        (-80, -42, 'A'),   # alpha helix
        (-120, 140, 'B'),  # beta sheet
        (55,   55, 'L'),   # left helix
    ]
    for (lx, ly, lt) in region_labels:
        ax.text(lx, ly, lt, fontsize=18, fontweight='bold',
                color='#1a3a5c', alpha=0.30, ha='center', va='center',
                zorder=4, style='italic')

    # ── Classify and separate residues ──
    general = [r for r in residues if classify_residue(r['resname']) == 'general']
    glys    = [r for r in residues if classify_residue(r['resname']) == 'gly']
    pros    = [r for r in residues if classify_residue(r['resname']) == 'pro']
    outliers = [r for r in residues if is_outlier(r['phi'], r['psi'], classify_residue(r['resname']))]

    gen_normal = [r for r in general if not is_outlier(r['phi'], r['psi'], 'general')]

    # ── Plot points ──
    if gen_normal:
        ax.scatter([r['phi'] for r in gen_normal],
                   [r['psi'] for r in gen_normal],
                   s=18, marker='s', c='#111111', alpha=0.80, zorder=5, linewidths=0)

    if glys:
        ax.scatter([r['phi'] for r in glys],
                   [r['psi'] for r in glys],
                   s=22, marker='x', c='#222222', alpha=0.82, zorder=5, linewidths=1.4)

    if pros:
        ax.scatter([r['phi'] for r in pros],
                   [r['psi'] for r in pros],
                   s=20, marker='^', c='#222222', alpha=0.80, zorder=5, linewidths=0)

    # Outlier markers (orange, on top)
    for r in outliers:
        rtype = classify_residue(r['resname'])
        mk = 's' if rtype == 'general' else ('^' if rtype == 'pro' else 'x')
        ax.scatter(r['phi'], r['psi'], s=50, marker=mk,
                   c='#e07000', alpha=0.95, zorder=7, linewidths=0)

    # Smart non-overlapping labels — cap at 15 most extreme outliers
    MAX_LABELS = 15
    scored = sorted(outliers,
                    key=lambda r: min(
                        abs(r['phi']+63)**2 + abs(r['psi']+42)**2,   # dist from alpha
                        abs(r['phi']+120)**2 + abs(r['psi']-130)**2, # dist from beta
                        abs(r['phi']-60)**2 + abs(r['psi']-40)**2,   # dist from L
                    ))
    # Most extreme = furthest from ALL favoured clusters
    scored_extreme = sorted(outliers,
        key=lambda r: -min(
            (r['phi']+63)**2+(r['psi']+42)**2,
            (r['phi']+120)**2+(r['psi']-130)**2,
            (r['phi']-60)**2+(r['psi']-40)**2,
        ))
    _smart_label_outliers(ax, scored_extreme[:MAX_LABELS])

    # ── Legend (outside plot, right side, no overlap) ──
    import matplotlib.lines as mlines
    legend_elements = [
        mpatches.Patch(facecolor='#5a92c7', label='Most favoured'),
        mpatches.Patch(facecolor='#b8cedf', label='Additional allowed'),
        mpatches.Patch(facecolor='#e8eaf0', edgecolor='#bbbbbb', label='Generously allowed'),
        mlines.Line2D([],[],marker='s', color='w', markerfacecolor='#111111',
                      markersize=6, label=f'General ({len(general)})'),
        mlines.Line2D([],[],marker='x', color='#222222', markersize=6,
                      linewidth=1.4, label=f'Glycine ({len(glys)})'),
        mlines.Line2D([],[],marker='^', color='w', markerfacecolor='#222222',
                      markersize=6, label=f'Proline ({len(pros)})'),
        mlines.Line2D([],[],marker='s', color='w', markerfacecolor='#e07000',
                      markersize=7, label=f'Outliers ({len(outliers)})'),
    ]
    # Place legend OUTSIDE the axes (top-right corner, no overlap with data)
    ax.legend(handles=legend_elements,
              loc='upper left', bbox_to_anchor=(1.01, 1.0),
              fontsize=7.8, framealpha=0.95,
              edgecolor='#bbbbbb', fancybox=False,
              title='Residue Types', title_fontsize=8,
              borderpad=0.7, handlelength=1.4)

    # ── Axes ──
    ax.set_xlim(-180, 180)
    ax.set_ylim(-180, 180)
    ax.set_xlabel('Phi (degrees)', fontsize=11, fontweight='bold', color='#1a1a1a', labelpad=6)
    ax.set_ylabel('Psi (degrees)', fontsize=11, fontweight='bold', color='#1a1a1a', labelpad=6)
    ax.set_xticks([-180,-135,-90,-45,0,45,90,135,180])
    ax.set_yticks([-180,-135,-90,-45,0,45,90,135,180])
    ax.tick_params(axis='both', labelsize=8.5, color='#666666')
    for sp in ax.spines.values():
        sp.set_edgecolor('#aaaaaa')
        sp.set_linewidth(1.0)
    ax.set_title(title, fontsize=13, fontweight='bold', color='#111111', pad=10)

    # ── Statistics table below the plot (PROCHECK style) ──
    total = len(residues)
    non_gly_pro = [r for r in residues if classify_residue(r['resname']) == 'general']
    n_total_nongp = len(non_gly_pro)

    n_fav  = sum(1 for r in non_gly_pro if classify_region(r['phi'],r['psi'])=='favoured')
    n_alw  = sum(1 for r in non_gly_pro if classify_region(r['phi'],r['psi'])=='allowed')
    n_gen  = sum(1 for r in non_gly_pro if classify_region(r['phi'],r['psi'])=='generous')
    n_out  = sum(1 for r in non_gly_pro if classify_region(r['phi'],r['psi'])=='outlier')

    pct = lambda n: f'{n/n_total_nongp*100:.1f}%' if n_total_nongp else '0.0%'

    table_ax = fig.add_axes([0.08, 0.02, 0.88, 0.22])
    table_ax.axis('off')

    # Title
    table_ax.text(0.5, 0.97, 'Plot Statistics', fontsize=10, fontweight='bold',
                  ha='center', va='top', transform=table_ax.transAxes, color='#111111')

    rows = [
        ('Residues in most favoured regions [A, B, L]',
         str(n_fav), pct(n_fav)),
        ('Residues in additional allowed regions [a, b, l, p]',
         str(n_alw), pct(n_alw)),
        ('Residues in generously allowed regions [~a, ~b, ~l, ~p]',
         str(n_gen), pct(n_gen)),
        ('Residues in disallowed regions',
         str(n_out), pct(n_out)),
        ('', '', ''),
        ('Number of non-glycine and non-proline residues',
         str(n_total_nongp), '100.0%' if n_total_nongp else ''),
        ('Number of glycine residues (shown as triangles)',    # note: we use ×
         str(len(glys)), ''),
        ('Number of proline residues',
         str(len(pros)), ''),
        ('', '', ''),
        ('Total number of residues', str(total), ''),
    ]

    col_x = [0.01, 0.74, 0.87]
    y = 0.86
    dy = 0.088

    # Header line
    table_ax.plot([0, 1], [y + dy * 0.5]*2,
                  color='#333333', linewidth=0.8,
                  transform=table_ax.transAxes, clip_on=False)

    for (label, count, pct_str) in rows:
        if label == '':
            table_ax.plot([0, 1], [y - dy*0.3]*2,
                          color='#cccccc', linewidth=0.5,
                          transform=table_ax.transAxes, clip_on=False)
            y -= dy * 0.5
            continue
        is_total = 'Total number' in label or 'non-glycine' in label
        fw = 'bold' if is_total else 'normal'
        fs = 8.0
        table_ax.text(col_x[0], y, label, fontsize=fs, fontweight=fw,
                      va='top', transform=table_ax.transAxes, color='#222222')
        table_ax.text(col_x[1], y, count, fontsize=fs, fontweight=fw,
                      va='top', ha='right', transform=table_ax.transAxes,
                      color='#222222')
        table_ax.text(col_x[2], y, pct_str, fontsize=fs, fontweight=fw,
                      va='top', ha='right', transform=table_ax.transAxes,
                      color='#555555')
        y -= dy

    # Bottom rule
    table_ax.plot([0, 1], [y + dy*0.3]*2,
                  color='#333333', linewidth=0.8,
                  transform=table_ax.transAxes, clip_on=False)

    # PROCHECK quality note
    table_ax.text(0.5, 0.01,
        'Based on analysis of 118 structures of resolution ≥2.0 Å and R-factor ≤20%,\n'
        'a well-refined structure should have over 90% residues in the most favoured regions.',
        fontsize=6.8, ha='center', va='bottom', transform=table_ax.transAxes,
        color='#666666', style='italic')

    return fig


def extract_angles(structure):
    """Extract phi/psi angles from a BioPython structure."""
    ppb = PPBuilder()
    residues = []
    for model in structure:
        for chain in model:
            polypeptides = ppb.build_peptides(chain)
            for pp in polypeptides:
                angles = pp.get_phi_psi_list()
                for i, (res, (phi, psi)) in enumerate(zip(pp, angles)):
                    if phi is None or psi is None:
                        continue
                    import math
                    phi_deg = math.degrees(phi)
                    psi_deg = math.degrees(psi)
                    resname = res.get_resname().strip()
                    resid = res.get_id()[1]
                    chain_id = res.get_parent().get_id()
                    try:
                        aa1 = protein_letters_3to1.get(resname, 'X')
                    except:
                        aa1 = 'X'
                    residues.append({
                        'phi': round(phi_deg, 2),
                        'psi': round(psi_deg, 2),
                        'resname': resname,
                        'aa1': aa1,
                        'resid': resid,
                        'chain': chain_id,
                        'label': f"{chain_id}{resid} {resname}"
                    })
    return residues



def parse_structure(filepath, fmt='pdb'):
    if fmt == 'pdb':
        parser = PDBParser(QUIET=True)
    else:
        parser = MMCIFParser(QUIET=True)
    structure = parser.get_structure('protein', filepath)
    return structure


# ── Routes ────────────────────────────────────────────────────────────────────

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        pdb_id = request.form.get('pdb_id', '').strip().upper()
        file = request.files.get('file')
        fmt = 'pdb'
        tmp_path = None

        if pdb_id:
            # Fetch from RCSB
            url = f"https://files.rcsb.org/download/{pdb_id}.pdb"
            r = requests.get(url, timeout=15)
            if r.status_code != 200:
                # Try CIF
                url = f"https://files.rcsb.org/download/{pdb_id}.cif"
                r = requests.get(url, timeout=15)
                if r.status_code != 200:
                    return jsonify({'error': f'PDB ID {pdb_id} not found'}), 404
                fmt = 'cif'
            with tempfile.NamedTemporaryFile(delete=False, suffix=f'.{fmt}', mode='wb') as f:
                f.write(r.content)
                tmp_path = f.name
            title = f"Ramachandran Plot — {pdb_id}"

        elif file:
            filename = file.filename.lower()
            fmt = 'cif' if filename.endswith('.cif') else 'pdb'
            with tempfile.NamedTemporaryFile(delete=False, suffix=f'.{fmt}', mode='wb') as f:
                file.save(f)
                tmp_path = f.name
            title = f"Ramachandran Plot — {file.filename}"
        else:
            return jsonify({'error': 'No PDB ID or file provided'}), 400

        structure = parse_structure(tmp_path, fmt)
        residues = extract_angles(structure)

        if not residues:
            return jsonify({'error': 'No residues with phi/psi angles found'}), 400

        # Generate plot
        fig = generate_plot(residues, title=title)
        img_buf = io.BytesIO()
        fig.savefig(img_buf, format='png', dpi=150, bbox_inches='tight',
                    facecolor='white', edgecolor='none')
        img_buf.seek(0)
        import base64
        img_b64 = base64.b64encode(img_buf.read()).decode('utf-8')
        plt.close(fig)

        # Stats
        total = len(residues)
        outliers = [r for r in residues if is_outlier(r['phi'], r['psi'], classify_residue(r['resname']))]
        n_favored = total - len(outliers)

        return jsonify({
            'success': True,
            'plot_b64': img_b64,
            'residues': residues,
            'stats': {
                'total': total,
                'favored': n_favored,
                'outliers': len(outliers),
                'pct_favored': round(n_favored / total * 100, 1) if total else 0,
                'pct_outliers': round(len(outliers) / total * 100, 1) if total else 0,
                'glycine': sum(1 for r in residues if r['resname'] == 'GLY'),
                'proline': sum(1 for r in residues if r['resname'] == 'PRO'),
            },
            'title': title
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if tmp_path and os.path.exists(tmp_path):
            os.unlink(tmp_path)


@app.route('/download_png', methods=['POST'])
def download_png():
    try:
        data = request.get_json()
        residues = data.get('residues', [])
        title = data.get('title', 'Ramachandran Plot')

        fig = generate_plot(residues, title=title)
        buf = io.BytesIO()
        fig.savefig(buf, format='png', dpi=200, bbox_inches='tight',
                    facecolor='white', edgecolor='none')
        buf.seek(0)
        plt.close(fig)
        return send_file(buf, mimetype='image/png',
                         as_attachment=True, download_name='ramachandran_plot.png')
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/download_svg', methods=['POST'])
def download_svg():
    try:
        data = request.get_json()
        residues = data.get('residues', [])
        title = data.get('title', 'Ramachandran Plot')

        fig = generate_plot(residues, title=title)
        buf = io.BytesIO()
        fig.savefig(buf, format='svg', bbox_inches='tight',
                    facecolor='white', edgecolor='none')
        buf.seek(0)
        plt.close(fig)
        return send_file(buf, mimetype='image/svg+xml',
                         as_attachment=True, download_name='ramachandran_plot.svg')
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/download_pdf', methods=['POST'])
def download_pdf():
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.lib import colors
        from reportlab.lib.units import cm
        from reportlab.platypus import SimpleDocTemplate, Image as RLImage, Paragraph, Spacer, Table, TableStyle
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.enums import TA_CENTER, TA_LEFT

        data = request.get_json()
        residues = data.get('residues', [])
        title = data.get('title', 'Ramachandran Plot')
        stats = data.get('stats', {})

        # Generate high-res plot
        fig = generate_plot(residues, title=title)
        img_buf = io.BytesIO()
        fig.savefig(img_buf, format='png', dpi=200, bbox_inches='tight',
                    facecolor='white', edgecolor='none')
        img_buf.seek(0)
        plt.close(fig)

        # Build PDF
        pdf_buf = io.BytesIO()
        doc = SimpleDocTemplate(pdf_buf, pagesize=A4,
                                rightMargin=2*cm, leftMargin=2*cm,
                                topMargin=2*cm, bottomMargin=2*cm)
        styles = getSampleStyleSheet()
        story = []

        # Title
        title_style = ParagraphStyle('Title', parent=styles['Title'],
                                     fontSize=18, spaceAfter=6,
                                     textColor=colors.HexColor('#1a1a2e'),
                                     alignment=TA_CENTER)
        story.append(Paragraph("Ramachandran Plot Analysis", title_style))

        sub_style = ParagraphStyle('Sub', parent=styles['Normal'],
                                   fontSize=11, spaceAfter=16,
                                   textColor=colors.HexColor('#555555'),
                                   alignment=TA_CENTER)
        story.append(Paragraph(title, sub_style))
        story.append(Spacer(1, 0.3*cm))

        # Plot image
        img_buf.seek(0)
        rl_img = RLImage(img_buf, width=14*cm, height=14*cm)
        story.append(rl_img)
        story.append(Spacer(1, 0.5*cm))

        # Stats table
        stat_style = ParagraphStyle('StatTitle', parent=styles['Heading2'],
                                    fontSize=12, spaceAfter=8,
                                    textColor=colors.HexColor('#1a1a2e'))
        story.append(Paragraph("Summary Statistics", stat_style))

        tdata = [
            ['Metric', 'Count', 'Percentage'],
            ['Total Residues', str(stats.get('total', 0)), '100%'],
            ['Favored Region', str(stats.get('favored', 0)),
             f"{stats.get('pct_favored', 0)}%"],
            ['Outliers', str(stats.get('outliers', 0)),
             f"{stats.get('pct_outliers', 0)}%"],
            ['Glycine Residues', str(stats.get('glycine', 0)), '—'],
            ['Proline Residues', str(stats.get('proline', 0)), '—'],
        ]
        t = Table(tdata, colWidths=[6*cm, 4*cm, 4*cm])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1a1a2e')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1),
             [colors.HexColor('#f8f9fa'), colors.white]),
            ('FONTSIZE', (0, 1), (-1, -1), 9),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#dddddd')),
            ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('ROWHEIGHT', (0, 0), (-1, -1), 0.7*cm),
            ('TOPPADDING', (0, 0), (-1, -1), 5),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ]))
        story.append(t)
        story.append(Spacer(1, 0.5*cm))

        # Outlier table
        outliers = [r for r in residues if is_outlier(r['phi'], r['psi'], classify_residue(r['resname']))]
        if outliers:
            story.append(Paragraph("Outlier Residues", stat_style))
            odata = [['Residue', 'Chain', 'φ (phi)', 'ψ (psi)', 'Type']]
            for r in sorted(outliers, key=lambda x: (x['chain'], x['resid']))[:50]:
                odata.append([
                    f"{r['resname']} {r['resid']}",
                    r['chain'],
                    f"{r['phi']:.1f}°",
                    f"{r['psi']:.1f}°",
                    classify_residue(r['resname']).capitalize()
                ])
            ot = Table(odata, colWidths=[4*cm, 2.5*cm, 3*cm, 3*cm, 2.5*cm])
            ot.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#c0392b')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 8),
                ('ROWBACKGROUNDS', (0, 1), (-1, -1),
                 [colors.HexColor('#fef9f9'), colors.white]),
                ('GRID', (0, 0), (-1, -1), 0.4, colors.HexColor('#dddddd')),
                ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                ('ROWHEIGHT', (0, 0), (-1, -1), 0.6*cm),
                ('TOPPADDING', (0, 0), (-1, -1), 4),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
            ]))
            story.append(ot)

        # Footer
        story.append(Spacer(1, 0.8*cm))
        footer_style = ParagraphStyle('Footer', parent=styles['Normal'],
                                      fontSize=8, textColor=colors.HexColor('#aaaaaa'),
                                      alignment=TA_CENTER)
        story.append(Paragraph("Generated by RamaPlot • Ramachandran Plot Analyzer", footer_style))

        doc.build(story)
        pdf_buf.seek(0)
        return send_file(pdf_buf, mimetype='application/pdf',
                         as_attachment=True, download_name='ramachandran_report.pdf')

    except Exception as e:
        return jsonify({'error': str(e)}), 500


def open_browser(port):
    import time
    time.sleep(1.2)
    webbrowser.open(f'http://localhost:{port}')


if __name__ == '__main__':
    port = 7432
    print(f"\n{'='*50}")
    print(f"  RamaPlot — Ramachandran Plot Analyzer")
    print(f"  Running at: http://localhost:{port}")
    print(f"{'='*50}\n")
    t = threading.Thread(target=open_browser, args=(port,), daemon=True)
    t.start()
    app.run(host='127.0.0.1', port=port, debug=False)
