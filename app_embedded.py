HTML_PAGE = '<!DOCTYPE html>\n<!-- RamaPlot v2.2 Phase2 built 2026-03-22 11:19 -->\n<html lang="en">\n<head>\n  <meta charset="UTF-8" />\n  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>\n  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate"/>\n  <meta http-equiv="Pragma" content="no-cache"/>\n  <meta http-equiv="Expires" content="0"/>\n  <title>RamaPlot — Ramachandran Plot Analyzer</title>\n  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 120 120\' width=\'16\' height=\'16\' style=\'display:block;flex-shrink:0\'><defs><linearGradient id=\'lg\' x1=\'0\' y1=\'0\' x2=\'1\' y2=\'1\'><stop offset=\'0%\' stop-color=\'#2d6be4\'/><stop offset=\'100%\' stop-color=\'#1a9b8a\'/></linearGradient><linearGradient id=\'ls\' x1=\'0\' y1=\'0\' x2=\'0\' y2=\'1\'><stop offset=\'0%\' stop-color=\'rgba(255,255,255,0.18)\'/><stop offset=\'100%\' stop-color=\'rgba(255,255,255,0)\'/></linearGradient><clipPath id=\'lc\'><rect width=\'120\' height=\'120\' rx=\'26\'/></clipPath></defs><rect width=\'120\' height=\'120\' rx=\'26\' fill=\'url(#lg)\'/><rect width=\'120\' height=\'60\' rx=\'26\' fill=\'url(#ls)\' clip-path=\'url(#lc)\'/><rect x=\'14\' y=\'16\' width=\'92\' height=\'88\' rx=\'6\' fill=\'rgba(0,0,0,0.18)\'/><line x1=\'24\' y1=\'94\' x2=\'97\' y2=\'94\' stroke=\'rgba(255,255,255,0.5)\' stroke-width=\'1.2\' stroke-linecap=\'round\'/><line x1=\'24\' y1=\'94\' x2=\'24\' y2=\'24\' stroke=\'rgba(255,255,255,0.5)\' stroke-width=\'1.2\' stroke-linecap=\'round\'/><polygon points=\'97,91 100,94 97,97\' fill=\'rgba(255,255,255,0.5)\'/><polygon points=\'21,24 24,21 27,24\' fill=\'rgba(255,255,255,0.5)\'/><ellipse cx=\'42\' cy=\'52\' rx=\'11\' ry=\'13\' fill=\'rgba(255,255,255,0.12)\'/><ellipse cx=\'40\' cy=\'78\' rx=\'9\' ry=\'7\' fill=\'rgba(255,255,255,0.10)\'/><rect x=\'34\' y=\'42\' width=\'4\' height=\'4\' rx=\'0.8\' fill=\'white\' opacity=\'0.92\'/><rect x=\'40\' y=\'37\' width=\'4\' height=\'4\' rx=\'0.8\' fill=\'white\' opacity=\'0.92\'/><rect x=\'47\' y=\'44\' width=\'4\' height=\'4\' rx=\'0.8\' fill=\'white\' opacity=\'0.90\'/><rect x=\'36\' y=\'50\' width=\'4\' height=\'4\' rx=\'0.8\' fill=\'white\' opacity=\'0.88\'/><rect x=\'44\' y=\'49\' width=\'4\' height=\'4\' rx=\'0.8\' fill=\'white\' opacity=\'0.85\'/><rect x=\'39\' y=\'56\' width=\'4\' height=\'4\' rx=\'0.8\' fill=\'white\' opacity=\'0.82\'/><rect x=\'33\' y=\'72\' width=\'4\' height=\'4\' rx=\'0.8\' fill=\'white\' opacity=\'0.88\'/><rect x=\'39\' y=\'76\' width=\'4\' height=\'4\' rx=\'0.8\' fill=\'white\' opacity=\'0.85\'/><rect x=\'45\' y=\'73\' width=\'4\' height=\'4\' rx=\'0.8\' fill=\'white\' opacity=\'0.82\'/><rect x=\'36\' y=\'80\' width=\'4\' height=\'4\' rx=\'0.8\' fill=\'white\' opacity=\'0.80\'/><line x1=\'64\' y1=\'46\' x2=\'68\' y2=\'50\' stroke=\'rgba(255,255,255,0.6)\' stroke-width=\'1.4\' stroke-linecap=\'round\'/><line x1=\'68\' y1=\'46\' x2=\'64\' y2=\'50\' stroke=\'rgba(255,255,255,0.6)\' stroke-width=\'1.4\' stroke-linecap=\'round\'/><rect x=\'75\' y=\'30\' width=\'5\' height=\'5\' rx=\'1\' fill=\'#fbbf24\'/><rect x=\'83\' y=\'55\' width=\'4.5\' height=\'4.5\' rx=\'0.8\' fill=\'#fbbf24\' opacity=\'0.85\'/><rect x=\'68\' y=\'82\' width=\'4\' height=\'4\' rx=\'0.8\' fill=\'#fbbf24\' opacity=\'0.75\'/><text x=\'100\' y=\'98\' font-family=\'Georgia,serif\' font-size=\'8.5\' font-style=\'italic\' fill=\'rgba(255,255,255,0.65)\'>φ</text><text x=\'16\' y=\'22\' font-family=\'Georgia,serif\' font-size=\'8.5\' font-style=\'italic\' fill=\'rgba(255,255,255,0.65)\'>ψ</text></svg>">\n  <style>\n    /* System fonts — no external requests, works fully offline */\n\n    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }\n\n    :root {\n      --bg: #f7f9fc;\n      --surface: #ffffff;\n      --surface2: #f0f4f8;\n      --border: #e2e8f0;\n      --accent: #2563eb;\n      --accent2: #0ea5e9;\n      --accent-dark: #1d4ed8;\n      --text: #0f172a;\n      --text2: #475569;\n      --text3: #94a3b8;\n      --success: #059669;\n      --warning: #d97706;\n      --danger: #dc2626;\n      --shadow: 0 4px 24px rgba(37,99,235,0.08);\n      --shadow-lg: 0 12px 40px rgba(37,99,235,0.13);\n    }\n\n    html, body {\n      height: 100%;\n      font-family: -apple-system, BlinkMacSystemFont, \'Segoe UI\', system-ui, sans-serif;\n      background: var(--bg);\n      color: var(--text);\n      overflow-x: hidden;\n    }\n\n    /* ── Animated protein background canvas ── */\n    #bg-canvas {\n      position: fixed;\n      top: 0; left: 0;\n      width: 100%; height: 100%;\n      z-index: 0;\n      pointer-events: none;\n      opacity: 0.45;\n    }\n\n    /* ── Layout ── */\n    .app {\n      position: relative;\n      z-index: 1;\n      min-height: 100vh;\n      display: flex;\n      flex-direction: column;\n    }\n\n    /* ── Header ── */\n    header {\n      background: rgba(255,255,255,0.92);\n      backdrop-filter: blur(16px);\n      border-bottom: 1px solid var(--border);\n      padding: 0 2rem;\n      height: 64px;\n      display: flex;\n      align-items: center;\n      justify-content: space-between;\n      position: sticky;\n      top: 0;\n      z-index: 100;\n      box-shadow: 0 2px 12px rgba(37,99,235,0.06);\n    }\n\n    .logo {\n      display: flex;\n      align-items: center;\n      gap: 10px;\n      text-decoration: none;\n    }\n\n    .logo-icon { display:flex; align-items:center; }\n\n    .logo-text {\n      font-size: 1.25rem;\n      font-weight: 700;\n      color: var(--text);\n      letter-spacing: -0.5px;\n    }\n\n    .logo-text span { color: var(--accent); }\n\n    .header-badge {\n      font-size: 0.7rem;\n      font-weight: 600;\n      background: linear-gradient(90deg, #2563eb22, #0ea5e922);\n      color: var(--accent);\n      border: 1px solid #2563eb33;\n      padding: 3px 10px;\n      border-radius: 999px;\n      letter-spacing: 0.5px;\n    }\n\n    /* ── Main ── */\n    main {\n      flex: 1;\n      max-width: 1100px;\n      margin: 0 auto;\n      padding: 2rem 1.5rem 4rem;\n      width: 100%;\n    }\n\n    /* ── Hero ── */\n    .hero {\n      text-align: center;\n      margin-bottom: 2.5rem;\n    }\n\n    .hero h1 {\n      font-size: 2.2rem;\n      font-weight: 700;\n      color: var(--text);\n      letter-spacing: -1px;\n      line-height: 1.2;\n      margin-bottom: 0.6rem;\n    }\n\n    .hero h1 span {\n      background: linear-gradient(90deg, #2563eb, #0ea5e9);\n      -webkit-background-clip: text;\n      -webkit-text-fill-color: transparent;\n      background-clip: text;\n    }\n\n    .hero p {\n      color: var(--text2);\n      font-size: 1rem;\n      max-width: 520px;\n      margin: 0 auto;\n      line-height: 1.6;\n    }\n\n    /* ── Input card ── */\n    .input-card {\n      background: var(--surface);\n      border: 1px solid var(--border);\n      border-radius: 20px;\n      padding: 2rem;\n      box-shadow: var(--shadow);\n      margin-bottom: 2rem;\n    }\n\n    .input-tabs {\n      display: flex;\n      gap: 6px;\n      margin-bottom: 1.6rem;\n      background: var(--surface2);\n      padding: 5px;\n      border-radius: 12px;\n      width: fit-content;\n    }\n\n    .tab-btn {\n      padding: 7px 20px;\n      border: none;\n      border-radius: 9px;\n      font-size: 0.875rem;\n      font-weight: 500;\n      cursor: pointer;\n      transition: all 0.2s;\n      background: transparent;\n      color: var(--text2);\n      font-family: -apple-system, BlinkMacSystemFont, \'Segoe UI\', system-ui, sans-serif;\n    }\n\n    .tab-btn.active {\n      background: var(--surface);\n      color: var(--accent);\n      box-shadow: 0 2px 8px rgba(37,99,235,0.12);\n      font-weight: 600;\n    }\n\n    .tab-panel { display: none; }\n    .tab-panel.active { display: block; }\n\n    .input-row {\n      display: flex;\n      gap: 12px;\n      align-items: flex-end;\n    }\n\n    .input-group {\n      flex: 1;\n    }\n\n    .input-group label {\n      display: block;\n      font-size: 0.8rem;\n      font-weight: 600;\n      color: var(--text2);\n      margin-bottom: 6px;\n      letter-spacing: 0.3px;\n      text-transform: uppercase;\n    }\n\n    .input-field {\n      width: 100%;\n      padding: 10px 14px;\n      border: 1.5px solid var(--border);\n      border-radius: 10px;\n      font-size: 0.95rem;\n      font-family: \'Consolas\', \'Courier New\', monospace;\n      color: var(--text);\n      background: var(--bg);\n      transition: all 0.2s;\n      outline: none;\n    }\n\n    .input-field:focus {\n      border-color: var(--accent);\n      box-shadow: 0 0 0 3px rgba(37,99,235,0.1);\n      background: white;\n    }\n\n    .file-drop {\n      border: 2px dashed var(--border);\n      border-radius: 12px;\n      padding: 2rem;\n      text-align: center;\n      cursor: pointer;\n      transition: all 0.2s;\n      background: var(--bg);\n    }\n\n    .file-drop:hover, .file-drop.drag-over {\n      border-color: var(--accent);\n      background: rgba(37,99,235,0.03);\n    }\n\n    .file-drop-icon { font-size: 2rem; margin-bottom: 8px; }\n\n    .file-drop p {\n      color: var(--text2);\n      font-size: 0.875rem;\n      margin-bottom: 4px;\n    }\n\n    .file-drop small { color: var(--text3); font-size: 0.775rem; }\n\n    #file-input { display: none; }\n\n    .file-name {\n      display: none;\n      margin-top: 8px;\n      font-size: 0.8rem;\n      color: var(--success);\n      font-weight: 600;\n    }\n\n    .btn-analyze {\n      padding: 11px 28px;\n      background: linear-gradient(135deg, #2563eb, #0ea5e9);\n      color: white;\n      border: none;\n      border-radius: 10px;\n      font-size: 0.95rem;\n      font-weight: 600;\n      cursor: pointer;\n      transition: all 0.2s;\n      white-space: nowrap;\n      font-family: -apple-system, BlinkMacSystemFont, \'Segoe UI\', system-ui, sans-serif;\n      box-shadow: 0 4px 14px rgba(37,99,235,0.3);\n      display: flex;\n      align-items: center;\n      gap: 8px;\n    }\n\n    .btn-analyze:hover {\n      transform: translateY(-1px);\n      box-shadow: 0 6px 20px rgba(37,99,235,0.38);\n    }\n\n    .btn-analyze:disabled {\n      opacity: 0.6;\n      cursor: not-allowed;\n      transform: none;\n    }\n\n    /* ── Loading ── */\n    .loading {\n      display: none;\n      text-align: center;\n      padding: 3rem;\n    }\n\n    .loading.active { display: block; }\n\n    .spinner {\n      width: 48px; height: 48px;\n      border: 4px solid var(--border);\n      border-top-color: var(--accent);\n      border-radius: 50%;\n      animation: spin 0.8s linear infinite;\n      margin: 0 auto 1rem;\n    }\n\n    @keyframes spin { to { transform: rotate(360deg); } }\n\n    .loading p { color: var(--text2); font-size: 0.95rem; }\n\n    /* ── Error ── */\n    .error-box {\n      display: none;\n      background: #fef2f2;\n      border: 1px solid #fecaca;\n      border-radius: 12px;\n      padding: 1rem 1.25rem;\n      color: var(--danger);\n      font-size: 0.9rem;\n      margin-bottom: 1.5rem;\n      display: none;\n      align-items: center;\n      gap: 8px;\n    }\n\n    .error-box.active { display: flex; }\n\n    /* ── Results ── */\n    .results { display: none; }\n    .results.active { display: block; }\n\n    .results-header {\n      display: flex;\n      align-items: center;\n      justify-content: space-between;\n      margin-bottom: 1.5rem;\n      flex-wrap: gap;\n      gap: 12px;\n    }\n\n    .results-title {\n      font-size: 1.1rem;\n      font-weight: 700;\n      color: var(--text);\n    }\n\n    .results-title small {\n      display: block;\n      font-size: 0.8rem;\n      font-weight: 400;\n      color: var(--text3);\n      margin-top: 2px;\n    }\n\n    .download-btns {\n      display: flex;\n      gap: 8px;\n      flex-wrap: wrap;\n    }\n\n    .btn-dl {\n      padding: 8px 16px;\n      border-radius: 8px;\n      border: 1.5px solid var(--border);\n      background: white;\n      color: var(--text);\n      font-size: 0.82rem;\n      font-weight: 600;\n      cursor: pointer;\n      transition: all 0.2s;\n      font-family: -apple-system, BlinkMacSystemFont, \'Segoe UI\', system-ui, sans-serif;\n      display: flex; align-items: center; gap: 6px;\n    }\n\n    .btn-dl:hover {\n      border-color: var(--accent);\n      color: var(--accent);\n      background: rgba(37,99,235,0.04);\n    }\n\n    .btn-dl.pdf { border-color: #e74c3c44; color: #c0392b; }\n    .btn-dl.pdf:hover { background: #fef2f2; border-color: #c0392b; }\n\n    /* ── Stats grid ── */\n    .stats-grid {\n      display: grid;\n      grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));\n      gap: 12px;\n      margin-bottom: 1.5rem;\n    }\n\n    .stat-card {\n      background: var(--surface);\n      border: 1px solid var(--border);\n      border-radius: 14px;\n      padding: 1rem;\n      text-align: center;\n      box-shadow: 0 2px 8px rgba(0,0,0,0.04);\n    }\n\n    .stat-card .stat-val {\n      font-size: 1.6rem;\n      font-weight: 700;\n      line-height: 1;\n      margin-bottom: 4px;\n    }\n\n    .stat-card .stat-label {\n      font-size: 0.75rem;\n      color: var(--text3);\n      font-weight: 500;\n      text-transform: uppercase;\n      letter-spacing: 0.4px;\n    }\n\n    .stat-card.good .stat-val { color: var(--success); }\n    .stat-card.warn .stat-val { color: var(--warning); }\n    .stat-card.info .stat-val { color: var(--accent); }\n    .stat-card.gly  .stat-val { color: #7c3aed; }\n    .stat-card.pro  .stat-val { color: #0891b2; }\n\n    /* ── Plot container ── */\n    .plot-wrap {\n      background: white;\n      border: 1px solid var(--border);\n      border-radius: 16px;\n      overflow: hidden;\n      box-shadow: var(--shadow-lg);\n      margin-bottom: 1.5rem;\n    }\n\n    .plot-wrap img {\n      width: 100%;\n      height: auto;\n      display: block;\n    }\n\n    /* ── Outlier table ── */\n    .outlier-section { margin-top: 1.5rem; }\n\n    .section-title {\n      font-size: 0.9rem;\n      font-weight: 700;\n      color: var(--text);\n      margin-bottom: 0.75rem;\n      display: flex;\n      align-items: center;\n      gap: 6px;\n    }\n\n    .badge {\n      padding: 2px 8px;\n      border-radius: 999px;\n      font-size: 0.72rem;\n      font-weight: 600;\n    }\n\n    .badge-danger { background: #fef2f2; color: var(--danger); }\n    .badge-info   { background: #eff6ff; color: var(--accent); }\n\n    .table-wrap {\n      overflow-x: auto;\n      border: 1px solid var(--border);\n      border-radius: 12px;\n    }\n\n    table {\n      width: 100%;\n      border-collapse: collapse;\n      font-size: 0.825rem;\n    }\n\n    thead th {\n      background: #f8fafc;\n      padding: 9px 14px;\n      text-align: left;\n      font-weight: 600;\n      color: var(--text2);\n      font-size: 0.775rem;\n      text-transform: uppercase;\n      letter-spacing: 0.4px;\n      border-bottom: 1px solid var(--border);\n    }\n\n    tbody tr:hover { background: #f8fafc; }\n\n    tbody td {\n      padding: 8px 14px;\n      border-bottom: 1px solid #f1f5f9;\n      color: var(--text);\n      font-family: \'Consolas\', \'Courier New\', monospace;\n      font-size: 0.8rem;\n    }\n\n    .type-badge {\n      padding: 2px 8px;\n      border-radius: 6px;\n      font-size: 0.72rem;\n      font-weight: 600;\n      font-family: -apple-system, BlinkMacSystemFont, \'Segoe UI\', system-ui, sans-serif;\n    }\n\n    .type-gly { background: #f3e8ff; color: #7c3aed; }\n    .type-pro { background: #e0f2fe; color: #0369a1; }\n    .type-gen { background: #fef9c3; color: #854d0e; }\n\n    /* ── Footer ── */\n    footer {\n      text-align: center;\n      padding: 1.5rem;\n      color: var(--text3);\n      font-size: 0.8rem;\n      border-top: 1px solid var(--border);\n      background: rgba(255,255,255,0.7);\n    }\n\n    /* ── Responsive ── */\n    @media (max-width: 600px) {\n      .hero h1 { font-size: 1.5rem; }\n      .input-row { flex-direction: column; }\n      .btn-analyze { width: 100%; justify-content: center; }\n    }\n\n    /* ── Analysis Tabs ── */\n    .analysis-tabs {\n      display: flex;\n      gap: 4px;\n      background: var(--surface2);\n      padding: 5px;\n      border-radius: 14px;\n      margin-bottom: 1.5rem;\n      flex-wrap: wrap;\n    }\n    .atab {\n      padding: 8px 18px;\n      border: none;\n      border-radius: 10px;\n      font-size: 0.85rem;\n      font-weight: 500;\n      cursor: pointer;\n      transition: all 0.2s;\n      background: transparent;\n      color: var(--text2);\n      font-family: -apple-system, BlinkMacSystemFont, \'Segoe UI\', system-ui, sans-serif;\n      display: flex; align-items: center; gap: 6px;\n      white-space: nowrap;\n    }\n    .atab.active {\n      background: white;\n      color: var(--accent);\n      box-shadow: 0 2px 8px rgba(37,99,235,0.12);\n      font-weight: 600;\n    }\n    .atab .badge-dot {\n      width: 7px; height: 7px;\n      border-radius: 50%;\n      flex-shrink: 0;\n    }\n    .atab .badge-dot.pass    { background: #059669; }\n    .atab .badge-dot.warning { background: #d97706; }\n    .atab .badge-dot.fail    { background: #dc2626; }\n    .atab .badge-dot.none    { background: #94a3b8; }\n\n    .atab-panel { display: none; }\n    .atab-panel.active { display: block; }\n\n    /* ── Summary Cards ── */\n    .summary-grid {\n      display: grid;\n      grid-template-columns: repeat(6, 1fr);\n      gap: 10px;\n      margin-bottom: 1.5rem;\n    }\n    @media (max-width: 900px) {\n      .summary-grid { grid-template-columns: repeat(3, 1fr); }\n    }\n    .summary-card {\n      background: white;\n      border: 1px solid var(--border);\n      border-radius: 14px;\n      padding: 0.9rem 1rem;\n      display: flex;\n      flex-direction: column;\n      gap: 6px;\n      box-shadow: 0 2px 8px rgba(0,0,0,0.04);\n      transition: all 0.2s;\n      cursor: pointer;\n      overflow: hidden;\n      position: relative;\n    }\n    .summary-card:hover { box-shadow: 0 4px 16px rgba(37,99,235,0.10); transform: translateY(-1px); }\n    .summary-card-icon {\n      width: 28px; height: 28px;\n      border-radius: 8px;\n      display: flex; align-items: center; justify-content: center;\n      font-size: 1rem;\n      flex-shrink: 0;\n    }\n    .sc-pass    { background: #d1fae5; }\n    .sc-warning { background: #fef3c7; }\n    .sc-fail    { background: #fee2e2; }\n    .sc-info    { background: #e8f0fd; }\n    .summary-card-body {}\n    .summary-card-title {\n      font-size: 0.82rem;\n      color: var(--text2);\n      font-weight: 500;\n      margin-bottom: 2px;\n      text-transform: uppercase;\n      letter-spacing: 0.4px;\n    }\n    .summary-card-val {\n      font-size: 1.15rem;\n      font-weight: 700;\n      line-height: 1.1;\n    }\n    .cv-pass    { color: #059669; }\n    .cv-warning { color: #d97706; }\n    .cv-fail    { color: #dc2626; }\n    .cv-info    { color: var(--accent); }\n    .summary-badge {\n      padding: 2px 7px;\n      border-radius: 999px;\n      font-size: 0.68rem;\n      font-weight: 700;\n      text-transform: uppercase;\n      letter-spacing: 0.4px;\n      display: inline-block;\n      width: fit-content;\n    }\n    .sb-pass    { background: #d1fae5; color: #059669; }\n    .sb-warning { background: #fef3c7; color: #d97706; }\n    .sb-fail    { background: #fee2e2; color: #dc2626; }\n\n    /* ── Sub-plot grid ── */\n    .subplot-grid {\n      display: grid;\n      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));\n      gap: 16px;\n      margin-top: 1rem;\n    }\n    .subplot-card {\n      background: white;\n      border: 1px solid var(--border);\n      border-radius: 14px;\n      overflow: hidden;\n      box-shadow: 0 2px 8px rgba(0,0,0,0.04);\n    }\n    .subplot-card img { width: 100%; height: auto; display: block; }\n    .subplot-label {\n      padding: 8px 12px;\n      font-size: 0.78rem;\n      font-weight: 600;\n      color: var(--text2);\n      border-top: 1px solid var(--border);\n      text-align: center;\n      background: var(--surface2);\n    }\n\n    /* ── Omega section ── */\n    .omega-grid {\n      display: grid;\n      grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));\n      gap: 12px;\n      margin-top: 1rem;\n    }\n    .omega-stat {\n      background: white;\n      border: 1px solid var(--border);\n      border-radius: 12px;\n      padding: 1rem;\n      text-align: center;\n    }\n    .omega-val { font-size: 1.6rem; font-weight: 700; color: var(--accent); }\n    .omega-lbl { font-size: 0.75rem; color: var(--text3); font-weight: 500; margin-top: 3px; text-transform: uppercase; letter-spacing: 0.4px; }\n\n  </style>\n</head>\n<body>\n\n<!-- Animated protein backbone background -->\n<canvas id="bg-canvas"></canvas>\n\n<div class="app">\n  <header>\n    <a class="logo" href="#">\n      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="34" height="34" style="display:block;flex-shrink:0"><defs><linearGradient id="lg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#2d6be4"/><stop offset="100%" stop-color="#1a9b8a"/></linearGradient><linearGradient id="ls" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="rgba(255,255,255,0.18)"/><stop offset="100%" stop-color="rgba(255,255,255,0)"/></linearGradient><clipPath id="lc"><rect width="120" height="120" rx="26"/></clipPath></defs><rect width="120" height="120" rx="26" fill="url(#lg)"/><rect width="120" height="60" rx="26" fill="url(#ls)" clip-path="url(#lc)"/><rect x="14" y="16" width="92" height="88" rx="6" fill="rgba(0,0,0,0.18)"/><line x1="24" y1="94" x2="97" y2="94" stroke="rgba(255,255,255,0.5)" stroke-width="1.2" stroke-linecap="round"/><line x1="24" y1="94" x2="24" y2="24" stroke="rgba(255,255,255,0.5)" stroke-width="1.2" stroke-linecap="round"/><polygon points="97,91 100,94 97,97" fill="rgba(255,255,255,0.5)"/><polygon points="21,24 24,21 27,24" fill="rgba(255,255,255,0.5)"/><ellipse cx="42" cy="52" rx="11" ry="13" fill="rgba(255,255,255,0.12)"/><ellipse cx="40" cy="78" rx="9" ry="7" fill="rgba(255,255,255,0.10)"/><rect x="34" y="42" width="4" height="4" rx="0.8" fill="white" opacity="0.92"/><rect x="40" y="37" width="4" height="4" rx="0.8" fill="white" opacity="0.92"/><rect x="47" y="44" width="4" height="4" rx="0.8" fill="white" opacity="0.90"/><rect x="36" y="50" width="4" height="4" rx="0.8" fill="white" opacity="0.88"/><rect x="44" y="49" width="4" height="4" rx="0.8" fill="white" opacity="0.85"/><rect x="39" y="56" width="4" height="4" rx="0.8" fill="white" opacity="0.82"/><rect x="33" y="72" width="4" height="4" rx="0.8" fill="white" opacity="0.88"/><rect x="39" y="76" width="4" height="4" rx="0.8" fill="white" opacity="0.85"/><rect x="45" y="73" width="4" height="4" rx="0.8" fill="white" opacity="0.82"/><rect x="36" y="80" width="4" height="4" rx="0.8" fill="white" opacity="0.80"/><line x1="64" y1="46" x2="68" y2="50" stroke="rgba(255,255,255,0.6)" stroke-width="1.4" stroke-linecap="round"/><line x1="68" y1="46" x2="64" y2="50" stroke="rgba(255,255,255,0.6)" stroke-width="1.4" stroke-linecap="round"/><rect x="75" y="30" width="5" height="5" rx="1" fill="#fbbf24"/><rect x="83" y="55" width="4.5" height="4.5" rx="0.8" fill="#fbbf24" opacity="0.85"/><rect x="68" y="82" width="4" height="4" rx="0.8" fill="#fbbf24" opacity="0.75"/><text x="100" y="98" font-family="Georgia,serif" font-size="8.5" font-style="italic" fill="rgba(255,255,255,0.65)">φ</text><text x="16" y="22" font-family="Georgia,serif" font-size="8.5" font-style="italic" fill="rgba(255,255,255,0.65)">ψ</text></svg>\n      <span class="logo-text">Rama<span>Plot</span></span>\n    </a>\n    <span class="header-badge">RAMACHANDRAN ANALYZER</span>\n  </header>\n\n  <main>\n    <!-- Hero -->\n    <div class="hero">\n      <h1>Ramachandran <span>Plot Analyzer</span></h1>\n      <p>Visualize backbone torsion angles φ and ψ for protein structures. Identify favored regions, allowed regions, and outliers.</p>\n    </div>\n\n    <!-- Input Card -->\n    <div class="input-card">\n      <div class="input-tabs">\n        <button class="tab-btn active" onclick="switchTab(\'pdb-id\')">🔍 PDB ID</button>\n        <button class="tab-btn" onclick="switchTab(\'upload\')">📁 Upload File</button>\n      </div>\n\n      <!-- PDB ID Tab -->\n      <div class="tab-panel active" id="tab-pdb-id">\n        <div class="input-row">\n          <div class="input-group">\n            <label>PDB Accession Code</label>\n            <input type="text" class="input-field" id="pdb-id-input"\n                   placeholder="e.g. 1CRN, 4HHB, 1TIM..."\n                   maxlength="6" autocomplete="off"\n                   onkeydown="if(event.key===\'Enter\') analyze()"/>\n          </div>\n          <button class="btn-analyze" onclick="analyze()">\n            <span>⚡</span> Analyze\n          </button>\n        </div>\n        <p style="margin-top:10px; font-size:0.78rem; color:var(--text3);">\n          Try: <a href="#" onclick="setExample(\'1CRN\')" style="color:var(--accent);text-decoration:none;font-weight:600;">1CRN</a> (Crambin) ·\n          <a href="#" onclick="setExample(\'4HHB\')" style="color:var(--accent);text-decoration:none;font-weight:600;">4HHB</a> (Hemoglobin) ·\n          <a href="#" onclick="setExample(\'1TIM\')" style="color:var(--accent);text-decoration:none;font-weight:600;">1TIM</a> (Triose Phosphate Isomerase) ·\n          <a href="#" onclick="setExample(\'2LZM\')" style="color:var(--accent);text-decoration:none;font-weight:600;">2LZM</a> (Lysozyme)\n        </p>\n      </div>\n\n      <!-- Upload Tab -->\n      <div class="tab-panel" id="tab-upload">\n        <div class="file-drop" id="file-drop" onclick="document.getElementById(\'file-input\').click()"\n             ondragover="dragOver(event)" ondragleave="dragLeave(event)" ondrop="dropFile(event)">\n          <div class="file-drop-icon">📄</div>\n          <p><strong>Click to upload</strong> or drag & drop</p>\n          <small>Supports .pdb and .cif files</small>\n          <div class="file-name" id="file-name"></div>\n        </div>\n        <input type="file" id="file-input" accept=".pdb,.cif,.ent"\n               onchange="fileSelected(this)"/>\n        <div style="margin-top:12px; display:flex; justify-content:flex-end;">\n          <button class="btn-analyze" onclick="analyze()">\n            <span>⚡</span> Analyze\n          </button>\n        </div>\n      </div>\n    </div>\n\n    <!-- Loading -->\n    <div class="loading" id="loading">\n      <div class="spinner"></div>\n      <p>Fetching structure and calculating torsion angles…</p>\n    </div>\n\n    <!-- Error -->\n    <div class="error-box" id="error-box">\n      <span>⚠️</span>\n      <span id="error-msg">Something went wrong.</span>\n    </div>\n\n    <!-- Results -->\n    <div class="results" id="results">\n\n      <!-- Results header -->\n      <div class="results-header">\n        <div class="results-title">\n          Analysis Results\n          <small id="results-subtitle"></small>\n        </div>\n        <div class="download-btns" style="align-items:center;gap:8px;">\n          <div style="display:flex;align-items:center;gap:6px;background:var(--surface2);border:1px solid var(--border);border-radius:8px;padding:4px 10px;">\n            <label style="font-size:0.75rem;font-weight:600;color:var(--text2);white-space:nowrap;">DPI</label>\n            <select id="dpi-select" style="border:none;background:transparent;font-size:0.82rem;font-weight:600;color:var(--text);cursor:pointer;outline:none;padding:2px 4px;">\n              <option value="150">150</option>\n              <option value="300">300</option>\n              <option value="600" selected>600</option>\n              <option value="900">900</option>\n              <option value="1200">1200</option>\n            </select>\n          </div>\n          <button class="btn-dl" onclick="downloadPNG()">🖼️ PNG</button>\n          <button class="btn-dl" onclick="downloadSVG()">📐 SVG</button>\n          <button class="btn-dl pdf" onclick="downloadPDF()">📄 PDF Report</button>\n        </div>\n      </div>\n\n      <!-- Summary cards -->\n      <div class="summary-grid" id="summary-grid"></div>\n\n      <!-- Analysis tabs -->\n      <div class="analysis-tabs" id="analysis-tabs">\n        <button class="atab active" onclick="switchATab(\'main\')" id="tab-main">\n          <span class="badge-dot none" id="dot-main"></span> Ramachandran\n        </button>\n        <button class="atab" onclick="switchATab(\'subplots\')" id="tab-subplots">\n          <span class="badge-dot none" id="dot-subplots"></span> All Rama\n        </button>\n        <button class="atab" onclick="switchATab(\'chi\')" id="tab-chi">\n          <span class="badge-dot none" id="dot-chi"></span> Chi1-Chi2\n        </button>\n        <button class="atab" onclick="switchATab(\'errat\')" id="tab-errat">\n          <span class="badge-dot none" id="dot-errat"></span> ERRAT\n        </button>\n        <button class="atab" onclick="switchATab(\'bond\')" id="tab-bond">\n          <span class="badge-dot none" id="dot-bond"></span> Bond Geometry\n        </button>\n        <button class="atab" onclick="switchATab(\'bfactor\')" id="tab-bfactor">\n          <span class="badge-dot none" id="dot-bfactor"></span> B-factors\n        </button>\n        <button class="atab" onclick="switchATab(\'outliers\')" id="tab-outliers">\n          <span class="badge-dot none" id="dot-outliers"></span> Outliers\n        </button>\n      </div>\n\n      <!-- TAB: Main Ramachandran -->\n      <div class="atab-panel active" id="panel-main">\n        <div class="stats-grid" id="stats-grid"></div>\n        <div class="plot-wrap">\n          <img id="plot-img" src="" alt="Ramachandran Plot"/>\n        </div>\n      </div>\n\n      <!-- TAB: All Ramachandrans -->\n      <div class="atab-panel" id="panel-subplots">\n        <p style="font-size:0.85rem;color:var(--text2);margin-bottom:1rem;">\n          Separate Ramachandran plots for each residue class, following PROCHECK conventions.\n        </p>\n        <div class="subplot-grid" id="subplot-grid"></div>\n      </div>\n\n      <!-- TAB: Chi1-Chi2 -->\n      <div class="atab-panel" id="panel-chi">\n        <p style="font-size:0.85rem;color:var(--text2);margin-bottom:1rem;">\n          Side-chain torsion angle distribution. Points cluster at gauche⁻ (−60°), trans (180°) and gauche⁺ (+60°) conformations.\n        </p>\n        <div class="plot-wrap" id="chi-plot-wrap" style="max-width:560px;margin:0 auto;">\n          <img id="chi-img" src="" alt="Chi1-Chi2 Plot"/>\n        </div>\n        <div class="omega-grid" id="omega-grid"></div>\n      </div>\n\n      <!-- TAB: ERRAT -->\n      <div class="atab-panel" id="panel-errat">\n        <p style="font-size:0.85rem;color:var(--text2);margin-bottom:1rem;">\n          ERRAT analyses the statistics of non-bonded interactions in a 9-residue sliding window.\n          Residues above the 95% threshold (yellow) or 99% threshold (red) may have modelling errors.\n        </p>\n        <div class="plot-wrap" id="errat-plot-wrap">\n          <img id="errat-img" src="" alt="ERRAT Plot"/>\n        </div>\n        <div class="stats-grid" id="errat-stats" style="margin-top:1rem;"></div>\n      </div>\n\n      <!-- TAB: Bond Geometry -->\n      <div class="atab-panel" id="panel-bond">\n        <p style="font-size:0.85rem;color:var(--text2);margin-bottom:1rem;">\n          Bond length and angle deviations from Engh &amp; Huber (1991) ideal values, expressed as Z-scores.\n          Green = within ±2σ · Yellow = 2–4σ · Red = outlier (&gt;4σ).\n        </p>\n        <div class="plot-wrap" id="bond-plot-wrap">\n          <img id="bond-img" src="" alt="Bond Geometry Plot"/>\n        </div>\n        <div class="stats-grid" id="bond-stats" style="margin-top:1rem;"></div>\n      </div>\n\n      <!-- TAB: B-factors -->\n      <div class="atab-panel" id="panel-bfactor">\n        <p style="font-size:0.85rem;color:var(--text2);margin-bottom:1rem;">\n          Per-residue B-factors (temperature factors) represent atomic displacement. High values indicate\n          flexibility or disorder. Very high B-factors (&gt;80 Å²) may indicate poorly defined regions.\n        </p>\n        <div class="plot-wrap" id="bfactor-plot-wrap">\n          <img id="bfactor-img" src="" alt="B-factor Plot"/>\n        </div>\n        <div class="stats-grid" id="bfactor-stats" style="margin-top:1rem;"></div>\n      </div>\n\n      <!-- TAB: Outliers -->\n      <div class="atab-panel" id="panel-outliers">\n        <div class="outlier-section" id="outlier-section"></div>\n        <!-- Clash table -->\n        <div id="clash-section" style="margin-top:1.5rem;"></div>\n      </div>\n\n    </div>\n  </main>\n\n  <footer>\n    RamaPlot &nbsp;·&nbsp; Ramachandran Plot Analyzer &nbsp;·&nbsp;\n    Built with BioPython + Matplotlib &nbsp;·&nbsp; Running locally\n  </footer>\n</div>\n\n<script>\n  // ── App state ──\n  let currentResidues = [];\n  let currentChiData  = [];\n  let currentTitle    = \'\';\n  let currentStats    = {};\n  let activeTab = \'pdb-id\';\n  let activeATab = \'main\';\n\n  // ── Input Tab switching ──\n  function switchTab(tab) {\n    activeTab = tab;\n    document.querySelectorAll(\'.tab-btn\').forEach((b, i) => {\n      b.classList.toggle(\'active\', (i === 0 && tab === \'pdb-id\') || (i === 1 && tab === \'upload\'));\n    });\n    document.querySelectorAll(\'.tab-panel\').forEach(p => p.classList.remove(\'active\'));\n    document.getElementById(\'tab-\' + tab).classList.add(\'active\');\n  }\n\n  // ── Analysis Tab switching ──\n  function switchATab(tab) {\n    activeATab = tab;\n    document.querySelectorAll(\'.atab\').forEach(b => b.classList.remove(\'active\'));\n    document.querySelectorAll(\'.atab-panel\').forEach(p => p.classList.remove(\'active\'));\n    document.getElementById(\'tab-\' + tab).classList.add(\'active\');\n    document.getElementById(\'panel-\' + tab).classList.add(\'active\');\n  }\n\n  function setExample(id) {\n    switchTab(\'pdb-id\');\n    document.getElementById(\'pdb-id-input\').value = id;\n    analyze();\n    return false;\n  }\n\n  // ── File handling ──\n  function fileSelected(input) {\n    if (input.files && input.files[0]) {\n      const fn = document.getElementById(\'file-name\');\n      fn.textContent = \'✓ \' + input.files[0].name;\n      fn.style.display = \'block\';\n    }\n  }\n\n  function dragOver(e) {\n    e.preventDefault();\n    document.getElementById(\'file-drop\').classList.add(\'drag-over\');\n  }\n  function dragLeave(e) {\n    document.getElementById(\'file-drop\').classList.remove(\'drag-over\');\n  }\n  function dropFile(e) {\n    e.preventDefault();\n    document.getElementById(\'file-drop\').classList.remove(\'drag-over\');\n    const file = e.dataTransfer.files[0];\n    if (file) {\n      const dt = new DataTransfer();\n      dt.items.add(file);\n      document.getElementById(\'file-input\').files = dt.files;\n      fileSelected(document.getElementById(\'file-input\'));\n    }\n  }\n\n  // ── Main analyze ──\n  async function analyze() {\n    showLoading(true);\n    hideError();\n    hideResults();\n\n    const formData = new FormData();\n    if (activeTab === \'pdb-id\') {\n      const pdbId = document.getElementById(\'pdb-id-input\').value.trim();\n      if (!pdbId) { showError(\'Please enter a PDB ID.\'); showLoading(false); return; }\n      formData.append(\'pdb_id\', pdbId);\n    } else {\n      const file = document.getElementById(\'file-input\').files[0];\n      if (!file) { showError(\'Please select a PDB or CIF file.\'); showLoading(false); return; }\n      formData.append(\'file\', file);\n    }\n\n    try {\n      const res = await fetch(\'/analyze\', { method: \'POST\', body: formData });\n      const data = await res.json();\n      if (!res.ok || data.error) { showError(data.error || \'Analysis failed.\'); return; }\n\n      currentResidues = data.residues;\n      currentChiData  = data.chi_data || [];\n      currentTitle    = data.title;\n      currentStats    = data.stats;\n\n      renderResults(data);\n    } catch (err) {\n      showError(\'Network error: \' + err.message);\n    } finally {\n      showLoading(false);\n    }\n  }\n\n  // ── Render all results ──\n  function renderResults(data) {\n    const { stats, plot_b64, residues, title, summary, subplots, chi_b64, omega_data } = data;\n\n    document.getElementById(\'results-subtitle\').textContent = title;\n\n    // ── Summary cards ──\n    const rama = summary.ramachandran;\n    const chi  = summary.chi;\n    const omg  = summary.omega;\n    const cnt  = summary.counts;\n\n    const badgeClass = b => b === \'pass\' ? \'sb-pass\' : b === \'warning\' ? \'sb-warning\' : \'sb-fail\';\n    const valClass   = b => b === \'pass\' ? \'cv-pass\' : b === \'warning\' ? \'cv-warning\' : \'cv-fail\';\n    const iconBg     = b => b === \'pass\' ? \'sc-pass\' : b === \'warning\' ? \'sc-warning\' : \'sc-fail\';\n    const icon       = b => b === \'pass\' ? \'✅\' : b === \'warning\' ? \'⚠️\' : \'❌\';\n\n    const errat   = summary.errat   || {};\n    const bond    = summary.bond    || {};\n    const rotamer = summary.rotamer || {};\n    const clash   = summary.clash   || {};\n    const bfac    = summary.bfactor || {};\n\n    function mkCard(tab, bgCls, ico, title, val, valCls, sub, badge, badgeCls) {\n      var d = document.createElement(\'div\');\n      d.className = \'summary-card\';\n      d.setAttribute(\'data-tab\', tab);\n      d.onclick = function(){ switchATab(this.getAttribute(\'data-tab\')); };\n      var topRow = \'<div style="display:flex;align-items:center;justify-content:space-between;gap:4px">\';\n      topRow += \'<div class="summary-card-icon \' + bgCls + \'">\' + ico + \'</div>\';\n      if (badge) topRow += \'<span class="summary-badge \' + badgeCls + \'">\' + badge + \'</span>\';\n      topRow += \'</div>\';\n      d.innerHTML = topRow +\n        \'<div class="summary-card-val \' + valCls + \'">\' + val + \'</div>\' +\n        \'<div class="summary-card-title">\' + title + \'</div>\' +\n        \'<div style="font-size:0.7rem;color:var(--text3);line-height:1.3">\' + sub + \'</div>\';\n      return d.outerHTML;\n    }\n\n    document.getElementById(\'summary-grid\').innerHTML =\n      mkCard(\'main\',     iconBg(rama.badge),           icon(rama.badge),           \'Ramachandran\',  rama.pct_favoured + \'%\',  valClass(rama.badge),           \'favoured regions\',                                    rama.badge,          badgeClass(rama.badge)) +\n      mkCard(\'chi\',      iconBg(chi.badge),             icon(chi.badge),            \'Chi1-Chi2\',     chi.pct_ok + \'%\',         valClass(chi.badge),            \'rotamers OK\',                                         chi.badge,           badgeClass(chi.badge)) +\n      mkCard(\'errat\',    iconBg(errat.badge||\'pass\'),   icon(errat.badge||\'pass\'),  \'ERRAT\',         (errat.overall||0) + \'%\', valClass(errat.badge||\'pass\'),  (errat.n_warning||0) + \' warnings\',                   errat.badge||\'pass\', badgeClass(errat.badge||\'pass\')) +\n      mkCard(\'bond\',     iconBg(bond.badge||\'pass\'),    icon(bond.badge||\'pass\'),   \'Bond Geometry\', bond.bond_rms||0,         valClass(bond.badge||\'pass\'),   \'RMSD \' + (bond.bond_outliers||0) + \' outliers\',       bond.badge||\'pass\',  badgeClass(bond.badge||\'pass\')) +\n      mkCard(\'outliers\', iconBg(clash.badge||\'pass\'),   icon(clash.badge||\'pass\'),  \'Clash Score\',   clash.clash_score||0,     valClass(clash.badge||\'pass\'),  \'per 1000 atoms\',                                      clash.badge||\'pass\', badgeClass(clash.badge||\'pass\')) +\n      mkCard(\'bfactor\',  \'sc-info\',                     \'&#x1F4CA;\',                \'B-factors\',     (bfac.mean||0) + \' Å²\', \'cv-info\',           \'mean / max \' + (bfac.max||0),                         \'\',                  \'\');\n\n    // Update tab badge dots\n    const dotColor = b => b === \'pass\' ? \'pass\' : b === \'warning\' ? \'warning\' : \'fail\';\n    document.getElementById(\'dot-main\').className     = `badge-dot ${dotColor(rama.badge)}`;\n    document.getElementById(\'dot-subplots\').className = `badge-dot ${dotColor(rama.badge)}`;\n    document.getElementById(\'dot-chi\').className      = `badge-dot ${dotColor(chi.badge)}`;\n\n    // ── Stats grid (main tab) ──\n    document.getElementById(\'stats-grid\').innerHTML = `\n      <div class="stat-card info"><div class="stat-val">${stats.total}</div><div class="stat-label">Total Residues</div></div>\n      <div class="stat-card ${stats.pct_favored >= 90 ? \'good\' : \'warn\'}">\n        <div class="stat-val">${stats.pct_favored}%</div><div class="stat-label">Favored Region</div>\n      </div>\n      <div class="stat-card ${stats.pct_outliers > 5 ? \'warn\' : \'good\'}">\n        <div class="stat-val">${stats.outliers}</div><div class="stat-label">Outliers (${stats.pct_outliers}%)</div>\n      </div>\n      <div class="stat-card gly"><div class="stat-val">${stats.glycine}</div><div class="stat-label">Glycine</div></div>\n      <div class="stat-card pro"><div class="stat-val">${stats.proline}</div><div class="stat-label">Proline</div></div>\n    `;\n\n    // ── Main plot ──\n    document.getElementById(\'plot-img\').src = \'data:image/png;base64,\' + plot_b64;\n\n    // ── Sub-plots ──\n    const SUBPLOT_LABELS = {\n      gly:     \'Glycine — all φ/ψ stereochemically allowed\',\n      pro:     \'Proline — restricted φ angle (~−60°)\',\n      prepro:  \'Pre-Proline — residue preceding a Pro\',\n      beta:    \'β-Branched — Val, Ile, Thr\',\n      general: \'General — Ala and remaining 14 residue types\',\n    };\n    const subGrid = document.getElementById(\'subplot-grid\');\n    subGrid.innerHTML = \'\';\n    for (const [key, label] of Object.entries(SUBPLOT_LABELS)) {\n      if (subplots[key]) {\n        subGrid.innerHTML += `\n          <div class="subplot-card">\n            <img src="data:image/png;base64,${subplots[key]}" alt="${label}"/>\n            <div class="subplot-label">${label}</div>\n          </div>`;\n      }\n    }\n    if (subGrid.innerHTML === \'\') {\n      subGrid.innerHTML = \'<p style="color:var(--text3);font-size:0.85rem">No sub-plots available.</p>\';\n    }\n\n    // ── Chi1-Chi2 plot ──\n    if (chi_b64) {\n      document.getElementById(\'chi-img\').src = \'data:image/png;base64,\' + chi_b64;\n      document.getElementById(\'chi-plot-wrap\').style.display = \'\';\n    } else {\n      document.getElementById(\'chi-plot-wrap\').style.display = \'none\';\n    }\n\n    // ── ERRAT plot ──\n    if (data.errat_b64) {\n      document.getElementById(\'errat-img\').src = \'data:image/png;base64,\' + data.errat_b64;\n      document.getElementById(\'errat-plot-wrap\').style.display = \'\';\n      const es = summary.errat || {};\n      document.getElementById(\'errat-stats\').innerHTML = `\n        <div class="stat-card info"><div class="stat-val">${es.overall || 0}%</div><div class="stat-label">Overall Quality</div></div>\n        <div class="stat-card ${(es.n_warning||0) === 0 ? \'good\' : \'warn\'}"><div class="stat-val">${es.n_warning || 0}</div><div class="stat-label">Warning Regions</div></div>\n        <div class="stat-card info"><div class="stat-val">${es.n_total || 0}</div><div class="stat-label">Residues Analysed</div></div>\n      `;\n      document.getElementById(\'dot-errat\').className = \'badge-dot \' + dotColor(es.badge || \'pass\');\n    }\n\n    // ── Bond geometry plot ──\n    if (data.bond_b64) {\n      document.getElementById(\'bond-img\').src = \'data:image/png;base64,\' + data.bond_b64;\n      document.getElementById(\'bond-plot-wrap\').style.display = \'\';\n      const bs = summary.bond || {};\n      document.getElementById(\'bond-stats\').innerHTML = `\n        <div class="stat-card info"><div class="stat-val">${bs.bond_rms || 0}</div><div class="stat-label">Bond Length RMSD</div></div>\n        <div class="stat-card info"><div class="stat-val">${bs.angle_rms || 0}</div><div class="stat-label">Bond Angle RMSD</div></div>\n        <div class="stat-card ${(bs.bond_outliers||0) === 0 ? \'good\' : \'warn\'}"><div class="stat-val">${bs.bond_outliers || 0}</div><div class="stat-label">Length Outliers (>4σ)</div></div>\n        <div class="stat-card ${(bs.angle_outliers||0) === 0 ? \'good\' : \'warn\'}"><div class="stat-val">${bs.angle_outliers || 0}</div><div class="stat-label">Angle Outliers (>4σ)</div></div>\n      `;\n      document.getElementById(\'dot-bond\').className = \'badge-dot \' + dotColor(bs.badge || \'pass\');\n    }\n\n    // ── B-factor plot ──\n    if (data.bfactor_b64) {\n      document.getElementById(\'bfactor-img\').src = \'data:image/png;base64,\' + data.bfactor_b64;\n      document.getElementById(\'bfactor-plot-wrap\').style.display = \'\';\n      const bf = summary.bfactor || {};\n      document.getElementById(\'bfactor-stats\').innerHTML = `\n        <div class="stat-card info"><div class="stat-val">${bf.mean || 0}</div><div class="stat-label">Mean B-factor (Å²)</div></div>\n        <div class="stat-card info"><div class="stat-val">${bf.max || 0}</div><div class="stat-label">Max B-factor (Å²)</div></div>\n      `;\n    }\n\n    // ── Clash table ──\n    const clashSection = document.getElementById(\'clash-section\');\n    const cd = data.clash_data || {};\n    if (cd.n_clashes > 0) {\n      let rows = \'\';\n      (cd.clashes || []).slice(0, 30).forEach(function(c) {\n        rows += \'<tr><td>\' + c.atom1 + \'</td><td>\' + c.atom2 + \'</td><td>\' +\n                c.dist + \'</td><td style="color:#dc2626;font-weight:600">\' +\n                c.overlap + \'</td></tr>\';\n      });\n      clashSection.innerHTML =\n        \'<div class="section-title">Steric Clashes \' +\n        \'<span class="badge badge-danger">\' + cd.n_clashes + \' clashes &middot; score \' + cd.clash_score + \'</span></div>\' +\n        \'<div class="table-wrap"><table>\' +\n        \'<thead><tr><th>Atom 1</th><th>Atom 2</th><th>Distance (&Aring;)</th><th>Overlap (&Aring;)</th></tr></thead>\' +\n        \'<tbody>\' + rows + \'</tbody></table></div>\';\n    } else {\n      clashSection.innerHTML = \'<div style="text-align:center;padding:1rem;color:var(--success);font-size:0.9rem;font-weight:600">No serious clashes detected</div>\';\n    }\n\n    // ── Omega stats ──\n    const omegaGrid = document.getElementById(\'omega-grid\');\n    if (omega_data && omega_data.length) {\n      const n = omega_data.length;\n      const cis     = omega_data.filter(function(o){ return Math.abs(o.omega) < 30; }).length;\n      const twisted = omega_data.filter(function(o){ return !(Math.abs(o.omega) < 30 || Math.abs(Math.abs(o.omega)-180) < 30); }).length;\n      const trans   = n - cis - twisted;\n      omegaGrid.innerHTML =\n        \'<div class="omega-stat"><div class="omega-val">\' + n + \'</div><div class="omega-lbl">Total &omega; angles</div></div>\' +\n        \'<div class="omega-stat"><div class="omega-val" style="color:#059669">\' + trans + \'</div><div class="omega-lbl">Trans (~180&deg;)</div></div>\' +\n        \'<div class="omega-stat"><div class="omega-val" style="color:#d97706">\' + cis + \'</div><div class="omega-lbl">Cis (~0&deg;)</div></div>\' +\n        \'<div class="omega-stat"><div class="omega-val" style="color:#dc2626">\' + twisted + \'</div><div class="omega-lbl">Twisted</div></div>\' +\n        \'<div class="omega-stat"><div class="omega-val" style="color:#7a8a9e">\' + (twisted/n*100).toFixed(1) + \'%</div><div class="omega-lbl">% Twisted</div></div>\';\n    }\n\n    // ── Outlier table ──\n    const outlierSection = document.getElementById(\'outlier-section\');\n    const outliers = residues.filter(function(r){ return isOutlier(r.phi, r.psi, r.resname); });\n    if (outliers.length > 0) {\n      let orows = \'\';\n      outliers.slice(0, 100).forEach(function(r) {\n        const ttype = r.resname === \'GLY\' ? \'gly\' : r.resname === \'PRO\' ? \'pro\' : \'gen\';\n        const tlabel = r.resname === \'GLY\' ? \'Glycine\' : r.resname === \'PRO\' ? \'Proline\' : \'General\';\n        orows += \'<tr><td>\' + r.resname + \'</td><td>\' + r.chain + \'</td><td>\' + r.resid +\n                 \'</td><td>\' + r.phi.toFixed(1) + \'&deg;</td><td>\' + r.psi.toFixed(1) +\n                 \'</td><td><span class="type-badge type-\' + ttype + \'">\' + tlabel + \'</span></td></tr>\';\n      });\n      outlierSection.innerHTML =\n        \'<div class="section-title">Outlier Residues <span class="badge badge-danger">\' + outliers.length + \' found</span></div>\' +\n        \'<div class="table-wrap"><table>\' +\n        \'<thead><tr><th>Residue</th><th>Chain</th><th>Res #</th><th>&phi; (phi)</th><th>&psi; (psi)</th><th>Type</th></tr></thead>\' +\n        \'<tbody>\' + orows + \'</tbody></table></div>\' +\n        (outliers.length > 100 ? \'<p style="text-align:center;color:var(--text3);font-size:0.8rem;margin-top:8px">Showing 100 of \' + outliers.length + \' outliers</p>\' : \'\');\n      document.getElementById(\'dot-outliers\').className = \'badge-dot fail\';\n    } else {\n      outlierSection.innerHTML = \'<div style="text-align:center;padding:2rem;color:var(--success);font-size:0.9rem;font-weight:600">No outliers detected</div>\';\n      document.getElementById(\'dot-outliers\').className = \'badge-dot pass\';\n    }\n\n    document.getElementById(\'results\').classList.add(\'active\');\n    document.getElementById(\'results\').scrollIntoView({ behavior: \'smooth\', block: \'start\' });\n  }\n\n  function isOutlier(phi, psi, resname) {\n    if (resname === \'GLY\') return false;\n    const favored = [[-63,-42,45,40],[-120,130,50,45],[-65,140,40,35]];\n    const margin = 30;\n    for (const [pc,tc,sp,st] of favored) {\n      if (Math.abs(phi-pc) < sp+margin && Math.abs(psi-tc) < st+margin) return false;\n    }\n    return true;\n  }\n\n  async function downloadPNG() {\n    const dpi = parseInt(document.getElementById(\'dpi-select\').value) || 600;\n    const res = await fetch(\'/download_png\', { method:\'POST\', headers:{\'Content-Type\':\'application/json\'},\n      body: JSON.stringify({ residues: currentResidues, title: currentTitle, dpi }) });\n    downloadBlob(await res.blob(), `ramachandran_${dpi}dpi.png`);\n  }\n  async function downloadSVG() {\n    const res = await fetch(\'/download_svg\', { method:\'POST\', headers:{\'Content-Type\':\'application/json\'},\n      body: JSON.stringify({ residues: currentResidues, title: currentTitle }) });\n    downloadBlob(await res.blob(), \'ramachandran_plot.svg\');\n  }\n  async function downloadPDF() {\n    const dpi = Math.min(parseInt(document.getElementById(\'dpi-select\').value) || 300, 600);\n    const res = await fetch(\'/download_pdf\', { method:\'POST\', headers:{\'Content-Type\':\'application/json\'},\n      body: JSON.stringify({ residues: currentResidues, title: currentTitle, stats: currentStats, dpi }) });\n    downloadBlob(await res.blob(), \'ramachandran_report.pdf\');\n  }\n  function downloadBlob(blob, name) {\n    const url = URL.createObjectURL(blob);\n    const a = document.createElement(\'a\');\n    a.href = url; a.download = name; a.click();\n    URL.revokeObjectURL(url);\n  }\n\n  function showLoading(v) { document.getElementById(\'loading\').classList.toggle(\'active\', v); }\n  function showError(msg) {\n    document.getElementById(\'error-msg\').textContent = msg;\n    document.getElementById(\'error-box\').classList.add(\'active\');\n  }\n  function hideError()   { document.getElementById(\'error-box\').classList.remove(\'active\'); }\n  function hideResults() { document.getElementById(\'results\').classList.remove(\'active\'); }\n\n  // ── Animated protein background ──\n  (function() {\n    const canvas = document.getElementById(\'bg-canvas\');\n    const ctx = canvas.getContext(\'2d\');\n    let W, H, nodes, t = 0;\n    function resize() {\n      W = canvas.width = window.innerWidth;\n      H = canvas.height = window.innerHeight;\n      init();\n    }\n    function init() {\n      nodes = [];\n      const count = Math.floor((W * H) / 14000);\n      for (let i = 0; i < count; i++) {\n        nodes.push({ x:Math.random()*W, y:Math.random()*H,\n          vx:(Math.random()-0.5)*0.4, vy:(Math.random()-0.5)*0.4,\n          r:Math.random()*3+2, phase:Math.random()*Math.PI*2 });\n      }\n    }\n    function draw() {\n      ctx.clearRect(0,0,W,H); t+=0.008;\n      nodes.forEach(n => {\n        n.x += n.vx + Math.sin(t+n.phase)*0.3;\n        n.y += n.vy + Math.cos(t+n.phase*0.7)*0.3;\n        if(n.x<0)n.x=W; if(n.x>W)n.x=0;\n        if(n.y<0)n.y=H; if(n.y>H)n.y=0;\n      });\n      for(let i=0;i<nodes.length;i++) for(let j=i+1;j<nodes.length;j++) {\n        const dx=nodes[i].x-nodes[j].x, dy=nodes[i].y-nodes[j].y;\n        const dist=Math.sqrt(dx*dx+dy*dy);\n        if(dist<110){\n          const alpha=(1-dist/110)*0.5;\n          ctx.beginPath(); ctx.moveTo(nodes[i].x,nodes[i].y); ctx.lineTo(nodes[j].x,nodes[j].y);\n          ctx.strokeStyle=`rgba(37,99,235,${alpha * 1.8})`; ctx.lineWidth=dist<55?1.2:0.6; ctx.stroke();\n        }\n      }\n      nodes.forEach(n => {\n        ctx.beginPath(); ctx.arc(n.x,n.y,n.r,0,Math.PI*2);\n        ctx.fillStyle=\'rgba(14,165,233,0.85)\'; ctx.fill();\n      });\n      requestAnimationFrame(draw);\n    }\n    window.addEventListener(\'resize\', resize); resize(); draw();\n  })();\n</script>\n</body>\n</html>'

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
from flask import Flask, request, jsonify, send_file, Response, make_response
from Bio.PDB import PDBParser, MMCIFParser, PPBuilder, is_aa
from Bio.PDB.Polypeptide import protein_letters_3to1
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)

# ── Ramachandran region definitions (density-based, PROCHECK calibrated) ─────
# Uses Gaussian density from known structural populations (Lovell et al. 2003)
# Thresholds calibrated to match PROCHECK coverage:
#   Most favoured ~22%, Additional allowed ~15%, Generously allowed ~10%

def _build_rama_regions():
    """
    Build Ramachandran region masks using density-based approach.
    Calibrated to match PROCHECK/MolProbity region boundaries.
    Grid resolution: 1 degree (360x360).
    """
    phi_g = np.linspace(-180, 180, 360)
    psi_g = np.linspace(-180, 180, 360)
    PHI, PSI = np.meshgrid(phi_g, psi_g)

    density = np.zeros((360, 360))

    # Population centres from Top500 high-resolution crystal structures
    # (phi_c, psi_c, sigma_phi, sigma_psi, weight)
    populations = [
        # Alpha helix
        (-63, -43, 18, 15, 100),
        (-65, -40, 30, 25,  60),
        (-70, -35, 45, 38,  35),
        # Beta sheet core
        (-120, 130, 22, 20,  95),
        (-115, 135, 35, 30,  60),
        (-110, 140, 50, 42,  38),
        # Beta extended / upper-left
        (-130, 160, 25, 22,  45),
        (-140, 155, 40, 35,  30),
        (-150, 160, 30, 25,  35),
        (-160, 165, 25, 20,  30),
        (-170, 170, 20, 18,  25),
        # Polyproline II
        (-75, 145, 20, 18,  40),
        (-70, 150, 30, 25,  25),
        # Left-handed helix
        ( 60,  40, 18, 16,  30),
        ( 65,  38, 28, 24,  18),
        # Alpha-beta bridge
        (-95, -15, 22, 20,  20),
        (-100,  10, 20, 18,  18),
        # Epsilon / inverse-gamma
        (-145, -175, 18, 15, 15),
        # Pre-Pro / PPII variant
        (-60, 130, 18, 16,  20),
    ]

    for (pc, tc, sp, st, w) in populations:
        density += w * np.exp(-((PHI-pc)**2/(2*sp**2) + (PSI-tc)**2/(2*st**2)))

    # Handle phi=±180 wraparound (torus topology)
    density[:, 0]  += density[:, -1] * 0.5
    density[:, -1] += density[:,  0] * 0.5
    density[ 0, :] += density[-1, :] * 0.5
    density[-1, :] += density[ 0, :] * 0.5
    density = gaussian_filter(density, sigma=1.5)
    density = density / density.max()

    # Calibrated thresholds → PROCHECK-equivalent coverage
    t_fav = 0.080   # → ~22% most favoured
    t_alw = 0.026   # → ~15% additional allowed
    t_gen = 0.012   # → ~10% generously allowed

    fav = density > t_fav
    alw = (density > t_alw) & ~fav
    gen = (density > t_gen) & ~fav & ~alw

    return phi_g, psi_g, fav, alw, gen


# Cache regions (reset to None to force rebuild after code change)
_RAMA_REGIONS = None

def get_rama_regions():
    global _RAMA_REGIONS
    if _RAMA_REGIONS is None:
        _RAMA_REGIONS = _build_rama_regions()
    return _RAMA_REGIONS


def classify_region(phi, psi):
    """Return 'favoured', 'allowed', 'generous', or 'outlier'."""
    r_phi, r_psi, fav, alw, gen = get_rama_regions()
    i = int(np.clip(round((phi + 180) / 360 * 359), 0, 359))
    j = int(np.clip(round((psi + 180) / 360 * 359), 0, 359))
    if fav[j, i]: return 'favoured'
    if alw[j, i]: return 'allowed'
    if gen[j, i]: return 'generous'
    return 'outlier'


def get_rama_regions():
    global _RAMA_REGIONS
    if _RAMA_REGIONS is None:
        _RAMA_REGIONS = _build_rama_regions()
    return _RAMA_REGIONS


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



# ─────────────────────────────────────────────────────────────────────
# PHASE 1 — All Ramachandrans + Chi1-Chi2 + Summary
# ─────────────────────────────────────────────────────────────────────

# Residue type groupings for PROCHECK-style sub-plots
GLY_RESIDUES  = {'GLY'}
PRO_RESIDUES  = {'PRO'}
PREPRO_RESIDUES = set()          # filled dynamically
BETA_BRANCHED = {'VAL','ILE','THR'}
GENERAL_AA    = set()            # everything else

# Chi angle atom name lookup per residue
CHI_ATOMS = {
    'ARG': [('N','CA','CB','CG'),('CA','CB','CG','CD'),('CB','CG','CD','NE'),('CG','CD','NE','CZ')],
    'ASN': [('N','CA','CB','CG'),('CA','CB','CG','OD1')],
    'ASP': [('N','CA','CB','CG'),('CA','CB','CG','OD1')],
    'CYS': [('N','CA','CB','SG')],
    'GLN': [('N','CA','CB','CG'),('CA','CB','CG','CD'),('CB','CG','CD','OE1')],
    'GLU': [('N','CA','CB','CG'),('CA','CB','CG','CD'),('CB','CG','CD','OE1')],
    'HIS': [('N','CA','CB','CG'),('CA','CB','CG','ND1')],
    'ILE': [('N','CA','CB','CG1'),('CA','CB','CG1','CD1')],
    'LEU': [('N','CA','CB','CG'),('CA','CB','CG','CD1')],
    'LYS': [('N','CA','CB','CG'),('CA','CB','CG','CD'),('CB','CG','CD','CE'),('CG','CD','CE','NZ')],
    'MET': [('N','CA','CB','CG'),('CA','CB','CG','SD'),('CB','CG','SD','CE')],
    'PHE': [('N','CA','CB','CG'),('CA','CB','CG','CD1')],
    'PRO': [('N','CA','CB','CG'),('CA','CB','CG','CD')],
    'SER': [('N','CA','CB','OG')],
    'THR': [('N','CA','CB','OG1')],
    'TRP': [('N','CA','CB','CG'),('CA','CB','CG','CD1')],
    'TYR': [('N','CA','CB','CG'),('CA','CB','CG','CD1')],
    'VAL': [('N','CA','CB','CG1')],
}


def _calc_dihedral(p1, p2, p3, p4):
    """Calculate dihedral angle (degrees) from 4 atom positions."""
    b1 = p2 - p1
    b2 = p3 - p2
    b3 = p4 - p3
    n1 = np.cross(b1, b2)
    n2 = np.cross(b2, b3)
    m1 = np.cross(n1, b2 / np.linalg.norm(b2))
    x = np.dot(n1, n2)
    y = np.dot(m1, n2)
    return math.degrees(math.atan2(y, x))


def extract_full_data(structure):
    """
    Extract phi/psi angles + chi1/chi2 + omega angles from structure.
    Returns dict with keys: residues, chi_data, omega_data, prepro_residues
    """
    ppb = PPBuilder()
    residues = []
    chi_data = []       # [{resname, chi1, chi2, chain, resid}]
    omega_data = []     # [{omega, resname, chain, resid}]

    # First pass: collect all residue objects in order (for pre-Pro detection)
    all_res_list = []
    for model in structure:
        for chain in model:
            polypeptides = ppb.build_peptides(chain)
            for pp in polypeptides:
                for res in pp:
                    all_res_list.append(res)

    # Build pre-Pro set
    prepro_set = set()
    for i, res in enumerate(all_res_list[:-1]):
        next_res = all_res_list[i+1]
        if next_res.get_resname().strip() == 'PRO':
            prepro_set.add((res.get_parent().get_id(), res.get_id()[1]))

    # Second pass: extract angles
    for model in structure:
        for chain in model:
            chain_id = chain.get_id()
            polypeptides = ppb.build_peptides(chain)
            for pp in polypeptides:
                angles = pp.get_phi_psi_list()
                for i, (res, (phi, psi)) in enumerate(zip(pp, angles)):
                    if phi is None or psi is None:
                        continue
                    phi_deg = math.degrees(phi)
                    psi_deg = math.degrees(psi)
                    resname = res.get_resname().strip()
                    resid = res.get_id()[1]
                    try:
                        aa1 = protein_letters_3to1.get(resname, 'X')
                    except:
                        aa1 = 'X'

                    is_prepro = (chain_id, resid) in prepro_set
                    rtype = classify_residue(resname)
                    if is_prepro and rtype == 'general':
                        rtype = 'prepro'

                    residues.append({
                        'phi': round(phi_deg, 2),
                        'psi': round(psi_deg, 2),
                        'resname': resname,
                        'aa1': aa1,
                        'resid': resid,
                        'chain': chain_id,
                        'label': f"{chain_id}{resid} {resname}",
                        'rtype': rtype,
                        'is_prepro': is_prepro,
                    })

                    # Chi angles
                    if resname in CHI_ATOMS:
                        atom_names = CHI_ATOMS[resname]
                        chi_vals = []
                        for atom_quad in atom_names[:2]:  # chi1, chi2 only
                            try:
                                atoms = [res[a].get_vector().get_array() for a in atom_quad]
                                chi = _calc_dihedral(*[np.array(a) for a in atoms])
                                chi_vals.append(round(chi, 2))
                            except (KeyError, Exception):
                                chi_vals.append(None)
                        if chi_vals[0] is not None:
                            chi_data.append({
                                'resname': resname,
                                'chi1': chi_vals[0],
                                'chi2': chi_vals[1] if len(chi_vals) > 1 else None,
                                'chain': chain_id,
                                'resid': resid,
                                'label': f"{chain_id}{resid} {resname}"
                            })

                    # Omega angle (peptide bond planarity)
                    if i > 0:
                        prev_res = pp[i-1]
                        try:
                            CA_prev = prev_res['CA'].get_vector().get_array()
                            C_prev  = prev_res['C'].get_vector().get_array()
                            N_curr  = res['N'].get_vector().get_array()
                            CA_curr = res['CA'].get_vector().get_array()
                            omega = _calc_dihedral(
                                np.array(CA_prev), np.array(C_prev),
                                np.array(N_curr),  np.array(CA_curr)
                            )
                            omega_data.append({
                                'omega': round(omega, 2),
                                'resname': resname,
                                'chain': chain_id,
                                'resid': resid,
                            })
                        except (KeyError, Exception):
                            pass

    return {
        'residues': residues,
        'chi_data': chi_data,
        'omega_data': omega_data,
    }


def generate_sub_plot(residues, title, subtitle=""):
    """Generate a compact Ramachandran plot for a residue subset."""
    r_phi, r_psi, fav_mask, alw_mask, gen_mask = get_rama_regions()
    fig, ax = plt.subplots(figsize=(5.5, 5.5), facecolor='white')
    ax.set_facecolor('white')

    # Region image
    rgba = np.ones((*fav_mask.shape, 4))
    rgba[gen_mask] = [0.91, 0.93, 0.97, 1.0]
    rgba[alw_mask] = [0.72, 0.82, 0.93, 1.0]
    rgba[fav_mask] = [0.35, 0.57, 0.78, 1.0]
    ax.imshow(rgba, origin='lower', aspect='auto',
              extent=[-180,180,-180,180], zorder=1, interpolation='nearest')

    # Grid
    ax.axhline(0, color='#888', linewidth=0.6, linestyle='--', alpha=0.5, zorder=2)
    ax.axvline(0, color='#888', linewidth=0.6, linestyle='--', alpha=0.5, zorder=2)

    # Points
    outliers = [r for r in residues if is_outlier(r['phi'], r['psi'], classify_residue(r['resname']))]
    normal   = [r for r in residues if not is_outlier(r['phi'], r['psi'], classify_residue(r['resname']))]

    if normal:
        ax.scatter([r['phi'] for r in normal], [r['psi'] for r in normal],
                   s=12, marker='s', c='#111', alpha=0.75, zorder=4, linewidths=0)
    if outliers:
        ax.scatter([r['phi'] for r in outliers], [r['psi'] for r in outliers],
                   s=28, marker='s', c='#e07000', alpha=0.95, zorder=5, linewidths=0)

    # Stats
    total = len(residues)
    n_fav = len(normal)
    pct = n_fav/total*100 if total else 0

    ax.set_xlim(-180, 180); ax.set_ylim(-180, 180)
    ax.set_xlabel('φ', fontsize=10, fontweight='bold')
    ax.set_ylabel('ψ', fontsize=10, fontweight='bold')
    ax.set_xticks([-180,-90,0,90,180])
    ax.set_yticks([-180,-90,0,90,180])
    ax.tick_params(labelsize=8)
    ax.set_title(f"{title}\n{subtitle} (n={total}, fav={pct:.1f}%)",
                 fontsize=9, fontweight='bold', pad=6)
    for sp in ax.spines.values():
        sp.set_edgecolor('#ccc'); sp.set_linewidth(0.8)
    plt.tight_layout(pad=1.0)
    return fig


def generate_chi_plot(chi_data):
    """Generate Chi1-Chi2 scatter plot."""
    has_chi2 = [d for d in chi_data if d['chi2'] is not None]
    chi1_only = [d for d in chi_data if d['chi2'] is None]

    fig, ax = plt.subplots(figsize=(6, 6), facecolor='white')
    ax.set_facecolor('#f9fafb')

    # Light grid lines at preferred angles
    for angle in [-180,-120,-60,0,60,120,180]:
        ax.axhline(angle, color='#e0e4ea', linewidth=0.5, zorder=1)
        ax.axvline(angle, color='#e0e4ea', linewidth=0.5, zorder=1)
    ax.axhline(0, color='#aab', linewidth=0.8, linestyle='--', alpha=0.6, zorder=2)
    ax.axvline(0, color='#aab', linewidth=0.8, linestyle='--', alpha=0.6, zorder=2)

    # Color by residue group
    color_map = {
        'ARG':'#e74c3c','ASN':'#3498db','ASP':'#e67e22','CYS':'#f1c40f',
        'GLN':'#2ecc71','GLU':'#1abc9c','HIS':'#9b59b6','ILE':'#34495e',
        'LEU':'#e91e63','LYS':'#00bcd4','MET':'#ff9800','PHE':'#795548',
        'SER':'#4caf50','THR':'#03a9f4','TRP':'#673ab7','TYR':'#ff5722','VAL':'#607d8b',
    }

    # Group by residue
    from collections import defaultdict
    by_res = defaultdict(list)
    for d in has_chi2:
        by_res[d['resname']].append(d)

    handles = []
    for resname, pts in sorted(by_res.items()):
        col = color_map.get(resname, '#888888')
        sc = ax.scatter([p['chi1'] for p in pts], [p['chi2'] for p in pts],
                        s=14, c=col, alpha=0.7, zorder=3, linewidths=0, label=resname)
        handles.append(sc)

    # Chi1-only residues
    if chi1_only:
        ax.scatter([d['chi1'] for d in chi1_only], [0]*len(chi1_only),
                   s=10, c='#888', alpha=0.5, zorder=3, linewidths=0,
                   marker='^', label='χ1 only')

    ax.set_xlim(-180, 180); ax.set_ylim(-180, 180)
    ax.set_xlabel('χ1 (degrees)', fontsize=11, fontweight='bold')
    ax.set_ylabel('χ2 (degrees)', fontsize=11, fontweight='bold')
    ax.set_xticks([-180,-120,-60,0,60,120,180])
    ax.set_yticks([-180,-120,-60,0,60,120,180])
    ax.tick_params(labelsize=9)
    ax.set_title(f"Chi1-Chi2 Plot  (n={len(chi_data)} residues)",
                 fontsize=12, fontweight='bold', pad=10)

    # Compact legend outside
    if by_res:
        ax.legend(handles, list(sorted(by_res.keys())),
                  loc='upper right', bbox_to_anchor=(1.28, 1.0),
                  fontsize=7, framealpha=0.9, ncol=1,
                  title='Residue', title_fontsize=7.5,
                  borderpad=0.5, handlelength=1.2)

    # Stats box
    n_total = len(chi_data)
    ax.text(0.02, 0.02, f"Total: {n_total} residues\n{len(by_res)} residue types",
            transform=ax.transAxes, fontsize=8,
            bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor='#ccc', alpha=0.9))

    for sp in ax.spines.values():
        sp.set_edgecolor('#ccc'); sp.set_linewidth(0.8)
    plt.tight_layout(pad=1.0)
    return fig


def compute_summary(residues, chi_data, omega_data):
    """Compute PROCHECK-style Pass/Warning/Fail for each analysis."""
    total = len(residues)
    non_gp = [r for r in residues if classify_residue(r['resname']) == 'general']
    n_ngp = len(non_gp)

    n_fav = sum(1 for r in non_gp if classify_region(r['phi'],r['psi'])=='favoured')
    pct_fav = n_fav/n_ngp*100 if n_ngp else 0

    def badge(pct_fav):
        if pct_fav >= 90: return 'pass'
        if pct_fav >= 80: return 'warning'
        return 'fail'

    # Omega planarity — cis peptides (|omega| < 30 or |omega-180| < 30 = trans OK)
    n_omega = len(omega_data)
    n_cis = sum(1 for o in omega_data if abs(o['omega']) < 30)
    n_twisted = sum(1 for o in omega_data
                    if not (abs(o['omega']) < 30 or abs(abs(o['omega'])-180) < 30))
    pct_twisted = n_twisted/n_omega*100 if n_omega else 0

    # Chi1-Chi2 — residues in gauche-/trans/gauche+ wells
    n_chi = len(chi_data)
    n_chi_ok = sum(1 for d in chi_data
                   if any(abs(d['chi1'] - g) < 40 for g in [-60, 60, 180]))
    pct_chi_ok = n_chi_ok/n_chi*100 if n_chi else 100

    # Glycine sub-plot
    glys = [r for r in residues if r['resname']=='GLY']
    n_gly = len(glys)

    # Proline sub-plot
    pros = [r for r in residues if r['resname']=='PRO']
    n_pro = len(pros)

    return {
        'ramachandran': {
            'pct_favoured': round(pct_fav, 1),
            'badge': badge(pct_fav),
            'n_favoured': n_fav,
            'n_total': n_ngp,
        },
        'chi': {
            'pct_ok': round(pct_chi_ok, 1),
            'badge': 'pass' if pct_chi_ok >= 90 else ('warning' if pct_chi_ok >= 75 else 'fail'),
            'n_total': n_chi,
        },
        'omega': {
            'pct_twisted': round(pct_twisted, 1),
            'n_cis': n_cis,
            'n_twisted': n_twisted,
            'badge': 'pass' if pct_twisted < 2 else ('warning' if pct_twisted < 5 else 'fail'),
        },
        'counts': {
            'total': total, 'glycine': n_gly, 'proline': n_pro,
            'non_gp': n_ngp, 'chi_residues': n_chi,
        }
    }


# ═══════════════════════════════════════════════════════════════════════════════
# PHASE 2 — ERRAT · Bond Geometry · Rotamer · Clash Score · B-factor
# ═══════════════════════════════════════════════════════════════════════════════

# ── Engh & Huber 1991 ideal bond geometry reference values ──────────────────
# (mean, std_dev) for main-chain bonds and angles
IDEAL_BONDS = {
    ('N','CA'):  (1.458, 0.019), ('CA','C'):   (1.525, 0.021),
    ('C','O'):   (1.229, 0.019), ('C','N'):    (1.336, 0.023),
    ('CA','CB'): (1.532, 0.020),
}
IDEAL_ANGLES = {
    ('N','CA','C'):  (111.0, 2.8), ('CA','C','N'):  (116.2, 2.0),
    ('C','N','CA'):  (121.7, 2.5), ('CA','C','O'):  (120.1, 1.7),
    ('O','C','N'):   (123.0, 1.6), ('N','CA','CB'): (110.5, 1.7),
    ('CB','CA','C'): (111.5, 2.1),
}

# ── MolProbity rotamer library (chi1 preferred angles) ──────────────────────
ROTAMER_CHI1 = {
    'ARG': [-177, -67, -65], 'ASN': [-177, -65, 63],
    'ASP': [-177, -70, 70],  'CYS': [-177, -65, 65],
    'GLN': [-177, -67, -65], 'GLU': [-177, -67, -65],
    'HIS': [-177, -65, 63],  'ILE': [-177, -67, 63],
    'LEU': [-177, -85, 65],  'LYS': [-177, -67, -65],
    'MET': [-177, -67, -65], 'PHE': [-177, -65, 65],
    'PRO': [-29,  26],       'SER': [64,  -177, -65],
    'THR': [62,  -177],      'TRP': [-177, -65, 65],
    'TYR': [-177, -65, 65],  'VAL': [-177, 64,  -65],
}


def compute_bond_geometry(structure):
    """Compute bond length and angle Z-scores vs Engh & Huber ideal values."""
    bond_data   = []   # [{bond, length, z, resname, resid, chain}]
    angle_data  = []   # [{angle, value, z, resname, resid, chain}]

    for model in structure:
        for chain in model:
            chain_id = chain.get_id()
            res_list = [r for r in chain if r.get_id()[0] == ' ']

            for i, res in enumerate(res_list):
                resname = res.get_resname().strip()
                resid   = res.get_id()[1]

                # Bond lengths
                for (a1, a2), (mean, std) in IDEAL_BONDS.items():
                    try:
                        p1 = res[a1].get_vector()
                        p2 = res[a2].get_vector() if a2 != 'N' or i == 0 else                              res_list[i][a2].get_vector()
                        # Handle peptide bond (C of prev → N of current)
                        if a1 == 'C' and a2 == 'N' and i + 1 < len(res_list):
                            p2 = res_list[i+1]['N'].get_vector()
                        length = (p1 - p2).norm()
                        z = (length - mean) / std
                        bond_data.append({
                            'bond': f"{a1}-{a2}", 'length': round(length, 3),
                            'z': round(z, 2), 'mean': mean,
                            'resname': resname, 'resid': resid, 'chain': chain_id,
                            'label': f"{chain_id}{resid} {resname}"
                        })
                    except (KeyError, Exception):
                        pass

                # Bond angles
                for (a1, a2, a3), (mean, std) in IDEAL_ANGLES.items():
                    try:
                        p1 = res[a1].get_vector()
                        p2 = res[a2].get_vector()
                        p3 = res[a3].get_vector()
                        # Handle cross-residue (C-N-CA spans two residues)
                        if a1 == 'C' and i > 0:
                            p1 = res_list[i-1]['C'].get_vector()
                        elif a3 == 'N' and i + 1 < len(res_list):
                            p3 = res_list[i+1]['N'].get_vector()
                        v1 = (p1 - p2).normalized()
                        v2 = (p3 - p2).normalized()
                        cos_a = max(-1.0, min(1.0, v1 * v2))
                        angle = math.degrees(math.acos(cos_a))
                        z = (angle - mean) / std
                        angle_data.append({
                            'angle': f"{a1}-{a2}-{a3}", 'value': round(angle, 2),
                            'z': round(z, 2), 'mean': mean,
                            'resname': resname, 'resid': resid, 'chain': chain_id,
                            'label': f"{chain_id}{resid} {resname}"
                        })
                    except (KeyError, Exception):
                        pass

    return bond_data, angle_data


def compute_errat(structure):
    """
    ERRAT: non-bonded interaction statistics in a 9-residue sliding window.
    Returns per-residue error values and overall score.
    """
    from Bio.PDB import NeighborSearch, Selection

    # Expected C-C, C-N, C-O interaction ratios from Colovos & Yeates 1993
    EXPECTED = {'CC': 0.395, 'CN': 0.115, 'CO': 0.140,
                'NC': 0.115, 'NN': 0.015, 'NO': 0.020,
                'OC': 0.140, 'ON': 0.020, 'OO': 0.060}

    all_atoms = []
    res_order = []

    for model in structure:
        for chain in model:
            res_list = [r for r in chain if r.get_id()[0] == ' ']
            for res in res_list:
                res_order.append(res)
                for atom in res:
                    elem = atom.element.strip() if atom.element else atom.get_name()[0]
                    if elem in ('C', 'N', 'O'):
                        all_atoms.append((atom, elem, res))

    ns = NeighborSearch([a[0] for a in all_atoms])
    atom_elem = {a[0]: a[1] for a in all_atoms}

    errat_scores = []
    window = 9

    for i in range(len(res_order)):
        start = max(0, i - window // 2)
        end   = min(len(res_order), i + window // 2 + 1)
        window_res = set(id(r) for r in res_order[start:end])

        counts = {k: 0 for k in EXPECTED}
        total_pairs = 0

        for atom, elem1, res in all_atoms:
            if id(res) not in window_res:
                continue
            nearby = ns.search(atom.get_vector().get_array(), 3.5, 'A')
            for nbr in nearby:
                if nbr is atom:
                    continue
                elem2 = atom_elem.get(nbr, '')
                if elem2 not in ('C', 'N', 'O'):
                    continue
                key = elem1 + elem2
                if key in counts:
                    counts[key] += 1
                    total_pairs += 1

        if total_pairs == 0:
            errat_scores.append({
                'resid': res_order[i].get_id()[1],
                'chain': res_order[i].get_parent().get_id(),
                'resname': res_order[i].get_resname().strip(),
                'error': 0.0
            })
            continue

        # Chi-squared-like error vs expected
        error = 0.0
        for key, expected_frac in EXPECTED.items():
            observed = counts[key] / total_pairs
            if expected_frac > 0:
                error += (observed - expected_frac) ** 2 / expected_frac

        errat_scores.append({
            'resid':   res_order[i].get_id()[1],
            'chain':   res_order[i].get_parent().get_id(),
            'resname': res_order[i].get_resname().strip(),
            'error':   round(error * 100, 2)
        })

    # Overall score = % residues below error threshold (95% confidence = 0.346)
    threshold = 34.6
    n_ok = sum(1 for s in errat_scores if s['error'] < threshold)
    overall = n_ok / len(errat_scores) * 100 if errat_scores else 0

    return errat_scores, round(overall, 1)


def compute_rotamers(chi_data):
    """
    Assess side-chain rotamer quality.
    Returns % in favoured rotamer wells.
    """
    n_total = len(chi_data)
    n_favoured = 0

    for d in chi_data:
        resname = d['resname']
        chi1    = d['chi1']
        if resname not in ROTAMER_CHI1:
            continue
        preferred = ROTAMER_CHI1[resname]
        # Check if chi1 is within 40° of any preferred angle
        if any(abs(chi1 - p) < 40 or abs(chi1 - p + 360) < 40 or
               abs(chi1 - p - 360) < 40 for p in preferred):
            n_favoured += 1

    pct = n_favoured / n_total * 100 if n_total else 0
    return {
        'n_total':    n_total,
        'n_favoured': n_favoured,
        'pct_favoured': round(pct, 1),
        'badge': 'pass' if pct >= 98 else ('warning' if pct >= 95 else 'fail')
    }


def compute_clash_score(structure):
    """
    MolProbity-style clash score: serious steric overlaps > 0.4Å.
    Returns clashscore (clashes per 1000 atoms) and clash list.
    """
    from Bio.PDB import NeighborSearch

    atoms = []
    for model in structure:
        for chain in model:
            for res in chain:
                if res.get_id()[0] != ' ':
                    continue
                for atom in res:
                    if atom.get_name() == 'H':
                        continue
                    atoms.append(atom)

    ns = NeighborSearch(atoms)

    # Van der Waals radii
    VDW = {'C': 1.70, 'N': 1.55, 'O': 1.52, 'S': 1.80,
           'P': 1.80, 'SE': 1.90}

    clashes = []
    seen = set()
    BONDED_DIST = 2.0  # ignore bonded pairs

    for atom in atoms:
        elem1 = (atom.element or atom.get_name()[0]).strip().upper()
        r1 = VDW.get(elem1, 1.70)
        pos = atom.get_vector().get_array()
        nearby = ns.search(pos, r1 + 2.5, 'A')

        for other in nearby:
            if other is atom:
                continue
            # Skip same residue
            if other.get_parent() is atom.get_parent():
                continue
            # Skip adjacent residues (bonded across peptide)
            res1 = atom.get_parent().get_id()[1]
            res2 = other.get_parent().get_id()[1]
            if abs(res1 - res2) <= 1:
                continue

            pair_key = tuple(sorted([id(atom), id(other)]))
            if pair_key in seen:
                continue
            seen.add(pair_key)

            elem2 = (other.element or other.get_name()[0]).strip().upper()
            r2 = VDW.get(elem2, 1.70)
            dist = float(np.linalg.norm(
                pos - other.get_vector().get_array()))
            overlap = r1 + r2 - dist

            if overlap > 0.4:
                clashes.append({
                    'atom1': f"{atom.get_parent().get_parent().get_id()}"
                             f"{atom.get_parent().get_id()[1]}"
                             f" {atom.get_parent().get_resname().strip()}"
                             f" {atom.get_name()}",
                    'atom2': f"{other.get_parent().get_parent().get_id()}"
                             f"{other.get_parent().get_id()[1]}"
                             f" {other.get_parent().get_resname().strip()}"
                             f" {other.get_name()}",
                    'overlap': round(overlap, 3),
                    'dist':    round(dist, 3),
                })

    n_atoms = len(atoms)
    clash_score = len(clashes) / n_atoms * 1000 if n_atoms else 0

    return {
        'clash_score':  round(clash_score, 1),
        'n_clashes':    len(clashes),
        'n_atoms':      n_atoms,
        'clashes':      sorted(clashes, key=lambda x: -x['overlap'])[:50],
        'badge': 'pass' if clash_score < 20 else ('warning' if clash_score < 40 else 'fail')
    }


def compute_bfactors(structure):
    """Extract per-residue B-factors (average over all atoms)."""
    bfactor_data = []
    for model in structure:
        for chain in model:
            chain_id = chain.get_id()
            for res in chain:
                if res.get_id()[0] != ' ':
                    continue
                bfs = [a.get_bfactor() for a in res
                       if a.get_bfactor() is not None]
                if not bfs:
                    continue
                bfactor_data.append({
                    'resid':   res.get_id()[1],
                    'chain':   chain_id,
                    'resname': res.get_resname().strip(),
                    'bfactor': round(sum(bfs) / len(bfs), 2),
                    'label':   f"{chain_id}{res.get_id()[1]} {res.get_resname().strip()}"
                })
    return bfactor_data


def generate_errat_plot(errat_scores, overall_score, title="ERRAT"):
    """Generate ERRAT error function plot."""
    fig, ax = plt.subplots(figsize=(10, 4), facecolor='white')
    ax.set_facecolor('#f9fafb')

    xs = list(range(len(errat_scores)))
    ys = [s['error'] for s in errat_scores]

    # Fill under curve
    ax.fill_between(xs, ys, alpha=0.25, color='#2d6be4')
    ax.plot(xs, ys, color='#2d6be4', linewidth=1.2, alpha=0.9)

    # Threshold lines
    ax.axhline(95.0, color='#fbbf24', linewidth=1.5, linestyle='--',
               label='95% confidence (warning)')
    ax.axhline(99.5, color='#ef4444', linewidth=1.5, linestyle='--',
               label='99% confidence (error)')
    ax.fill_between(xs, 95, 99.5, alpha=0.06, color='#fbbf24')
    ax.fill_between(xs, 99.5, max(max(ys)+5, 105), alpha=0.06, color='#ef4444')

    # Mark bad residues
    bad = [(i, s) for i, s in enumerate(errat_scores) if s['error'] >= 95]
    if bad:
        ax.scatter([b[0] for b in bad], [b[1]['error'] for b in bad],
                   s=30, c='#ef4444', zorder=5, linewidths=0)

    # X-axis labels — residue numbers, every 20
    tick_xs = xs[::20]
    tick_labels = [f"{errat_scores[i]['chain']}{errat_scores[i]['resid']}"
                   for i in tick_xs]
    ax.set_xticks(tick_xs)
    ax.set_xticklabels(tick_labels, rotation=45, ha='right', fontsize=7)

    ax.set_ylim(0, max(max(ys) + 10, 110))
    ax.set_xlim(0, len(xs))
    ax.set_xlabel('Residue', fontsize=10, fontweight='bold')
    ax.set_ylabel('Error value', fontsize=10, fontweight='bold')
    ax.set_title(f"ERRAT — Overall quality: {overall_score:.1f}%  "
                 f"(residues below 95% threshold)",
                 fontsize=11, fontweight='bold', pad=8)
    ax.legend(fontsize=8, loc='upper right', framealpha=0.9)
    ax.tick_params(labelsize=8)
    for sp in ax.spines.values():
        sp.set_edgecolor('#ccc'); sp.set_linewidth(0.8)

    # Stats box
    n_warn = sum(1 for s in errat_scores if 95 <= s['error'] < 99.5)
    n_err  = sum(1 for s in errat_scores if s['error'] >= 99.5)
    ax.text(0.01, 0.97,
            f"Warning regions: {n_warn}\nError regions: {n_err}",
            transform=ax.transAxes, fontsize=8, va='top',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='white',
                      edgecolor='#ccc', alpha=0.9))

    plt.tight_layout(pad=1.0)
    return fig


def generate_bond_plot(bond_data, angle_data):
    """Generate bond geometry Z-score distribution."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5), facecolor='white')

    bond_z = [d['z'] for d in bond_data if abs(d['z']) < 10]
    angle_z = [d['z'] for d in angle_data if abs(d['z']) < 10]

    for ax, zs, label, color in [
        (ax1, bond_z,  'Bond lengths', '#2d6be4'),
        (ax2, angle_z, 'Bond angles',  '#1a9b8a'),
    ]:
        ax.set_facecolor('#f9fafb')
        if zs:
            bins = np.linspace(-6, 6, 30)
            counts, edges = np.histogram(zs, bins=bins)
            centers = (edges[:-1] + edges[1:]) / 2
            # Colour bars: green within ±2, yellow ±2-4, red >±4
            bar_colors = []
            for c in centers:
                if abs(c) <= 2:   bar_colors.append('#22c55e')
                elif abs(c) <= 4: bar_colors.append('#fbbf24')
                else:             bar_colors.append('#ef4444')
            ax.bar(centers, counts, width=0.38, color=bar_colors,
                   alpha=0.85, edgecolor='white', linewidth=0.4)

        ax.axvline(-2, color='#fbbf24', linewidth=1.2, linestyle='--', alpha=0.8)
        ax.axvline(+2, color='#fbbf24', linewidth=1.2, linestyle='--', alpha=0.8)
        ax.axvline(-4, color='#ef4444', linewidth=1.0, linestyle=':', alpha=0.7)
        ax.axvline(+4, color='#ef4444', linewidth=1.0, linestyle=':', alpha=0.7)
        ax.axvline(0,  color='#666',    linewidth=0.8, linestyle='-',  alpha=0.5)

        n_out = sum(1 for z in zs if abs(z) > 4)
        rms   = (sum(z**2 for z in zs) / len(zs))**0.5 if zs else 0
        ax.set_xlabel('Z-score', fontsize=10, fontweight='bold')
        ax.set_ylabel('Count', fontsize=10, fontweight='bold')
        ax.set_title(f"{label}\nRMSD={rms:.2f}  |  Outliers (|Z|>4): {n_out}",
                     fontsize=10, fontweight='bold', pad=6)
        ax.set_xlim(-7, 7)
        ax.tick_params(labelsize=8)
        for sp in ax.spines.values():
            sp.set_edgecolor('#ccc'); sp.set_linewidth(0.8)

        # Legend patches
        import matplotlib.patches as mp
        ax.legend(handles=[
            mp.Patch(color='#22c55e', label='Within ±2σ'),
            mp.Patch(color='#fbbf24', label='2–4σ'),
            mp.Patch(color='#ef4444', label='>4σ (outlier)'),
        ], fontsize=7.5, loc='upper left', framealpha=0.9)

    plt.tight_layout(pad=1.2)
    return fig


def generate_bfactor_plot(bfactor_data, title="B-factor Distribution"):
    """Generate per-residue B-factor plot."""
    fig, ax = plt.subplots(figsize=(10, 4), facecolor='white')
    ax.set_facecolor('#f9fafb')

    # Group by chain, colour differently
    chains = sorted(set(d['chain'] for d in bfactor_data))
    chain_colors = ['#2d6be4', '#1a9b8a', '#e07000', '#9b59b6', '#e74c3c']

    x_offset = 0
    tick_xs, tick_labels = [], []
    for ci, chain in enumerate(chains):
        chain_data = [d for d in bfactor_data if d['chain'] == chain]
        xs = list(range(x_offset, x_offset + len(chain_data)))
        ys = [d['bfactor'] for d in chain_data]
        col = chain_colors[ci % len(chain_colors)]
        ax.fill_between(xs, ys, alpha=0.2, color=col)
        ax.plot(xs, ys, color=col, linewidth=1.0, label=f"Chain {chain}")

        # Tick every 20 residues
        for j in range(0, len(chain_data), 20):
            tick_xs.append(x_offset + j)
            tick_labels.append(f"{chain}{chain_data[j]['resid']}")
        x_offset += len(chain_data) + 5

    # Mean line
    all_bf = [d['bfactor'] for d in bfactor_data]
    mean_bf = sum(all_bf) / len(all_bf) if all_bf else 0
    ax.axhline(mean_bf, color='#666', linewidth=1.0, linestyle='--',
               alpha=0.7, label=f"Mean = {mean_bf:.1f} Å²")

    ax.set_xticks(tick_xs)
    ax.set_xticklabels(tick_labels, rotation=45, ha='right', fontsize=7)
    ax.set_xlabel('Residue', fontsize=10, fontweight='bold')
    ax.set_ylabel('B-factor (Å²)', fontsize=10, fontweight='bold')
    ax.set_title(f"B-factor Distribution  |  Mean: {mean_bf:.1f} Å²  |  "
                 f"Max: {max(all_bf):.1f} Å²",
                 fontsize=11, fontweight='bold', pad=8)
    ax.legend(fontsize=8, framealpha=0.9)
    ax.tick_params(labelsize=8)
    for sp in ax.spines.values():
        sp.set_edgecolor('#ccc'); sp.set_linewidth(0.8)
    plt.tight_layout(pad=1.0)
    return fig


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
    resp = make_response(Response(HTML_PAGE, mimetype='text/html'))
    resp.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    resp.headers['Pragma'] = 'no-cache'
    resp.headers['Expires'] = '0'
    return resp


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
        full = extract_full_data(structure)
        residues  = full['residues']
        chi_data  = full['chi_data']
        omega_data= full['omega_data']

        if not residues:
            return jsonify({'error': 'No residues with phi/psi angles found'}), 400

        import base64

        def fig_to_b64(fig, dpi=150):
            buf = io.BytesIO()
            fig.savefig(buf, format='png', dpi=dpi, bbox_inches='tight',
                        facecolor='white', edgecolor='none')
            buf.seek(0)
            b64 = base64.b64encode(buf.read()).decode('utf-8')
            plt.close(fig)
            return b64

        # ── Main Ramachandran plot ──
        main_fig = generate_plot(residues, title=f"Ramachandran Plot — {title.split('— ')[-1]}")
        main_b64 = fig_to_b64(main_fig, dpi=150)

        # ── Sub-plots by residue type ──
        gly_res    = [r for r in residues if r['resname']=='GLY']
        pro_res    = [r for r in residues if r['resname']=='PRO']
        prepro_res = [r for r in residues if r.get('is_prepro')]
        beta_res   = [r for r in residues if r['resname'] in {'VAL','ILE','THR'}]
        general_res= [r for r in residues if classify_residue(r['resname'])=='general'
                      and not r.get('is_prepro') and r['resname'] not in {'VAL','ILE','THR'}]

        subplots_b64 = {}
        for key, subset, ttl, sub in [
            ('gly',    gly_res,     'Glycine',          'All φ/ψ allowed'),
            ('pro',    pro_res,     'Proline',           'Restricted φ'),
            ('prepro', prepro_res,  'Pre-Proline',       'Residues before Pro'),
            ('beta',   beta_res,    'β-Branched',        'Val, Ile, Thr'),
            ('general',general_res, 'General (Ala+14)',  'Remaining residues'),
        ]:
            if subset:
                f = generate_sub_plot(subset, ttl, sub)
                subplots_b64[key] = fig_to_b64(f, dpi=120)
            else:
                subplots_b64[key] = None

        # ── Chi1-Chi2 plot ──
        chi_b64 = None
        if chi_data:
            chi_fig = generate_chi_plot(chi_data)
            chi_b64 = fig_to_b64(chi_fig, dpi=130)

        # ── Summary ──
        summary = compute_summary(residues, chi_data, omega_data)

        # ── Phase 2 analyses ──
        struct = structure

        errat_scores, errat_overall = compute_errat(struct)
        errat_b64 = None
        if errat_scores:
            ef = generate_errat_plot(errat_scores, errat_overall)
            errat_b64 = fig_to_b64(ef, dpi=130)

        bond_data, angle_data = compute_bond_geometry(struct)
        bond_b64 = None
        if bond_data or angle_data:
            bf = generate_bond_plot(bond_data, angle_data)
            bond_b64 = fig_to_b64(bf, dpi=130)

        rotamer_stats = compute_rotamers(chi_data)

        clash_data = compute_clash_score(struct)

        bfactor_data = compute_bfactors(struct)
        bfactor_b64 = None
        if bfactor_data:
            bff = generate_bfactor_plot(bfactor_data)
            bfactor_b64 = fig_to_b64(bff, dpi=130)

        # Bond geometry stats for summary
        bond_z_vals = [d['z'] for d in bond_data if abs(d['z']) < 10]
        angle_z_vals = [d['z'] for d in angle_data if abs(d['z']) < 10]
        bond_rms  = round((sum(z**2 for z in bond_z_vals)  / len(bond_z_vals))**0.5,  2) if bond_z_vals  else 0
        angle_rms = round((sum(z**2 for z in angle_z_vals) / len(angle_z_vals))**0.5, 2) if angle_z_vals else 0
        bond_out  = sum(1 for z in bond_z_vals  if abs(z) > 4)
        angle_out = sum(1 for z in angle_z_vals if abs(z) > 4)

        summary['errat']    = {
            'overall': errat_overall,
            'badge': 'pass' if errat_overall >= 95 else ('warning' if errat_overall >= 85 else 'fail'),
            'n_warning': sum(1 for s in errat_scores if s['error'] >= 95),
            'n_total': len(errat_scores),
        }
        summary['bond']     = {
            'bond_rms': bond_rms, 'angle_rms': angle_rms,
            'bond_outliers': bond_out, 'angle_outliers': angle_out,
            'badge': 'pass' if bond_out == 0 and angle_out == 0 else
                     ('warning' if bond_out + angle_out < 5 else 'fail'),
        }
        summary['rotamer']  = rotamer_stats
        summary['clash']    = clash_data
        summary['bfactor']  = {
            'mean': round(sum(d['bfactor'] for d in bfactor_data) / len(bfactor_data), 1) if bfactor_data else 0,
            'max':  round(max((d['bfactor'] for d in bfactor_data), default=0), 1),
            'badge': 'pass',
        }

        # Stats for UI
        total = len(residues)
        outliers = [r for r in residues if is_outlier(r['phi'], r['psi'], classify_residue(r['resname']))]
        n_favored = total - len(outliers)

        return jsonify({
            'success': True,
            'plot_b64': main_b64,
            'subplots': subplots_b64,
            'chi_b64': chi_b64,
            'errat_b64': errat_b64,
            'bond_b64': bond_b64,
            'bfactor_b64': bfactor_b64,
            'residues': residues,
            'chi_data': chi_data,
            'omega_data': omega_data,
            'errat_scores': errat_scores[:200],
            'bond_data': bond_data[:200],
            'angle_data': angle_data[:200],
            'bfactor_data': bfactor_data[:200],
            'clash_data': clash_data,
            'rotamer_stats': rotamer_stats,
            'summary': summary,
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
        title    = data.get('title', 'Ramachandran Plot')
        dpi      = int(data.get('dpi', 600))
        dpi      = max(72, min(1200, dpi))   # clamp 72–1200

        fig = generate_plot(residues, title=title)
        buf = io.BytesIO()
        fig.savefig(buf, format='png', dpi=dpi, bbox_inches='tight',
                    facecolor='white', edgecolor='none')
        buf.seek(0)
        plt.close(fig)
        return send_file(buf, mimetype='image/png',
                         as_attachment=True,
                         download_name=f'ramachandran_{dpi}dpi.png')
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
        fig.savefig(img_buf, format='png', dpi=int(data.get('dpi', 300)), bbox_inches='tight',
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
        story.append(Paragraph("🧬  Ramachandran Plot Analysis", title_style))

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
        story.append(Paragraph("Generated by <b>RamaPlot</b> — Ramachandran Plot Analyzer  •  github.com/jobinjobzz/RamaPlot", footer_style))

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
