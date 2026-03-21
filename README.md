# 🧬 RamaPlot — Ramachandran Plot Analyzer

<div align="center">

![RamaPlot Banner](https://img.shields.io/badge/RamaPlot-v1.0.0-2d6be4?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0xMiAyQzYuNDggMiAyIDYuNDggMiAxMnM0LjQ4IDEwIDEwIDEwIDEwLTQuNDggMTAtMTBTMTcuNTIgMiAxMiAyem0tMiAxNWwtNS01IDEuNDEtMS40MUwxMCAxNC4xN2w3LjU5LTcuNTlMMTkgOGwtOSA5eiIvPjwvc3ZnPg==)
![Python](https://img.shields.io/badge/Python-3.10%2B-3776ab?style=for-the-badge&logo=python&logoColor=white)
![BioPython](https://img.shields.io/badge/BioPython-1.84-28a745?style=for-the-badge)
![License](https://img.shields.io/badge/License-Free-yellow?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows-0078d4?style=for-the-badge&logo=windows)

**A standalone desktop application for generating publication-quality Ramachandran plots from protein structures.**

[⬇ Download Latest Release](../../releases/latest) · [🐛 Report Bug](../../issues) · [💡 Request Feature](../../issues)

</div>

---

## 📸 Screenshot

> *Ramachandran plot of TOR kinase (6W4H) showing PROCHECK-style region classification and outlier labeling*

---

## ✨ Features

- 🔍 **PDB ID Fetch** — enter any RCSB accession code, structure downloads automatically
- 📁 **File Upload** — supports `.pdb` and `.cif` files (AlphaFold, Rosetta, experimental)
- 🗺️ **PROCHECK Regions** — most favoured, additional allowed, generously allowed, disallowed
- ⚠️ **Smart Outlier Labeling** — top outliers labeled with collision-free placement
- 📊 **Statistics Table** — PROCHECK-style summary with counts and percentages
- 📄 **PDF Report** — full report with plot, stats table, and outlier residue list
- 🖼️ **PNG / SVG Export** — publication-ready image downloads
- 💻 **100% Offline** — no internet needed for file upload mode
- ⚡ **Zero Setup** — single `.exe`, no Python or dependencies required

---

## 🚀 Quick Start

### Option A — Download the .exe (Windows)

1. Go to [Releases](../../releases/latest)
2. Download `RamaPlot.exe`
3. Double-click to run — browser opens automatically at `localhost:7432`

No Python. No installation. No setup.

### Option B — Run from source

```bash
# Clone the repository
git clone https://github.com/jobinjobzz/RamaPlot.git
cd RamaPlot

# Install dependencies
pip install flask biopython matplotlib numpy scipy requests reportlab pillow

# Run
python app.py
```

Browser opens automatically at `http://localhost:7432`

---

## 🔨 Build the .exe Yourself

On Windows, double-click `build_windows.bat`:

```
build_windows.bat
```

This will:
1. Install all dependencies via pip
2. Embed the HTML frontend into `app_embedded.py`
3. Build `dist/RamaPlot.exe` using PyInstaller

**Requirements:** Python 3.10–3.13, internet connection for pip

---

## 🧪 Usage

### Using a PDB ID
1. Launch RamaPlot
2. Select the **PDB ID** tab
3. Enter any 4-character code (e.g. `1CRN`, `4HHB`, `1TIM`)
4. Click **Analyze**

### Using a local file
1. Launch RamaPlot
2. Select the **Upload File** tab
3. Drag & drop or click to select a `.pdb` or `.cif` file
4. Click **Analyze**

### Exporting results
After analysis, use the buttons at the top of the results panel:
- **PNG** — high-resolution raster image (200 DPI)
- **SVG** — scalable vector for publications
- **PDF Report** — full report with plot + statistics + outlier table

---

## 📐 Understanding the Plot

| Region | Colour | Description |
|--------|--------|-------------|
| Most Favoured | 🟦 Steel Blue | Core α-helix (A), β-sheet (B), left-handed helix (L) |
| Additional Allowed | 🔵 Light Blue | Sterically acceptable loop conformations |
| Generously Allowed | ⬜ Silver-Blue | Borderline — warrants inspection |
| Disallowed | 🟠 Orange | Sterically unfavourable — potential model errors |

> A well-refined structure (resolution ≥ 2.0 Å, R-factor ≤ 20%) should have **> 90%** of residues in the most favoured regions.

Residue types are shown as:
- **■ Black squares** — general (non-Gly, non-Pro) residues
- **× Crosses** — Glycine (wider conformational freedom)
- **▲ Triangles** — Proline (restricted φ angle)
- **■ Orange squares** — outlier residues

---

## 🏗️ Project Structure

```
RamaPlot/
├── app.py                  ← Flask backend + BioPython analysis + Matplotlib plot
├── generate_embedded.py    ← Builds app_embedded.py (HTML baked in, for PyInstaller)
├── ramaplot.spec           ← PyInstaller build configuration
├── build_windows.bat       ← One-click Windows build script
├── requirements.txt        ← Python dependencies
└── templates/
    └── index.html          ← Full frontend UI (auto-embedded at build time)
```

---

## 🔬 Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3, Flask |
| Chemistry | BioPython (PPBuilder, PDBParser, MMCIFParser) |
| Plotting | Matplotlib, SciPy |
| PDF Generation | ReportLab |
| Frontend | HTML / CSS / Vanilla JS |
| Packaging | PyInstaller (single .exe) |

---

## 📦 Dependencies

```
flask
biopython
matplotlib
numpy
scipy
requests
reportlab
pillow
pyinstaller  # build only
```

---

## 🤝 Related Projects

- [**MolPredict**](https://github.com/jobinjobzz/Molpredict) — Molecule property predictor for drug discovery (SMILES → physicochemical properties, Lipinski rules, ADMET analysis)

---

## 📄 License

Free to use, modify, and distribute.

---

## 👤 Author

**Jobin** · [@jobinjobzz](https://github.com/jobinjobzz)

---

<div align="center">
Made with 🧬 BioPython + Matplotlib
</div>
