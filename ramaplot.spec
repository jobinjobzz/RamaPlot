# ramaplot.spec
# Run: python -m PyInstaller ramaplot.spec --clean --noconfirm

import sys
import os
from PyInstaller.utils.hooks import collect_data_files, collect_submodules

block_cipher = None

biopython_datas = collect_data_files('Bio')
matplotlib_datas = collect_data_files('matplotlib')

a = Analysis(
    ['app_embedded.py'],
    pathex=['.'],
    binaries=[],
    datas=[] + biopython_datas + matplotlib_datas,
    hiddenimports=[
        'Bio', 'Bio.PDB', 'Bio.PDB.PDBParser', 'Bio.PDB.MMCIFParser',
        'Bio.PDB.PPBuilder', 'Bio.PDB.Polypeptide', 'Bio.SeqRecord', 'Bio.Seq',
        'flask', 'flask.templating', 'jinja2', 'jinja2.ext',
        'werkzeug', 'werkzeug.serving', 'werkzeug.debug',
        'matplotlib', 'matplotlib.backends.backend_agg', 'matplotlib.pyplot',
        'scipy', 'scipy.ndimage', 'numpy',
        'reportlab', 'reportlab.platypus', 'reportlab.lib',
        'reportlab.lib.pagesizes', 'reportlab.lib.styles',
        'PIL', 'requests',
    ] + collect_submodules('Bio.PDB')
      + collect_submodules('flask')
      + collect_submodules('jinja2'),
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['tkinter', 'PyQt5', 'wx', 'gtk', 'Bio.PDB.mmtf'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='RamaPlot',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
    onefile=True,
)
