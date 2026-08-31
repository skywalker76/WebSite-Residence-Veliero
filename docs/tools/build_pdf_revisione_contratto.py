# -*- coding: utf-8 -*-
"""PDF per il cliente: HTML impaginato per la stampa -> Chrome headless -> numeri di pagina e metadati con PyMuPDF.
Usa lo stesso contenuto di build_revisione.py (unica sorgente)."""
import html, subprocess, sys, shutil
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from build_revisione import (TITOLO, SOTTOTITOLO, META, SINTESI, ROWS, B2B_INTRO, B2B, DECISIONI, LEGALE,
                             VALUTAZIONE, RIFERIMENTI, TAG_RE, kind, REPO, DOWNLOADS)

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
OUT_NAME = "Revisione Contratto Long Stay Veliero 31-8-26.pdf"

def h(s): return html.escape(s, quote=False)
def pill(m): return '<span class="pill %s">%s</span>' % ("pl" if m.group(1) == "LEGALE" else "pp", m.group(1))
def rich(t): return TAG_RE.sub(pill, h(t))

def items(lst):
    out = []
    for s in lst:
        k, t = kind(s)
        if k == "quote": out.append('<p class="q">«%s»</p>' % rich(t))
        elif k == "clause": out.append('<p class="cl">%s</p>' % rich(t))
        else: out.append('<p>%s</p>' % rich(t))
    return "".join(out)

CSS = """
@page { size: A4 landscape; margin: 14mm 16mm 16mm 16mm; }
:root{ --navy:#0D5A8A; --primary:#1875AB; --gold:#9A7209; --gold-bg:#FFF6D6; --ink:#1F2A36; --muted:#5B6B7A;
       --rule:#D6DEE6; --era:#F3F6F9; --new:#EEF5FB; --tint:#E8F1F8; }
*{ box-sizing:border-box; }
html,body{ margin:0; padding:0; background:#fff; color:var(--ink);
  font-family: Raleway, "Segoe UI", Arial, sans-serif; font-weight:500; font-size:10pt; line-height:1.42; font-variant-numeric: lining-nums tabular-nums; }
b,strong,th{ font-weight:700; }
h1,h2,h3{ font-family:"Playfair Display", Georgia, "Times New Roman", serif; color:var(--navy); margin:0; }
.eyebrow{ font-family: Montserrat, "Segoe UI", Arial, sans-serif; font-weight:700; font-size:8pt; letter-spacing:.16em; text-transform:uppercase; color:var(--primary); }

/* ---------- copertina */
.cover{ height:179mm; position:relative; break-after:page; page-break-after:always; overflow:visible; }
.cover .band{ display:none; }
.cover .band:after{ content:""; position:absolute; right:-2mm; top:0; bottom:0; width:2mm; background:#F5E082; }
.cover .body{ position:absolute; left:14mm; top:12mm; right:0; }
.cover h1{ font-size:30pt; line-height:1.08; max-width:190mm; margin:5mm 0 3mm; text-wrap:balance; }
.cover .sub{ font-size:12pt; color:var(--muted); margin:0 0 8mm; max-width:190mm; }
.meta{ border:1px solid var(--rule); border-radius:3px; overflow:hidden; max-width:225mm; }
.meta .r{ display:flex; border-top:1px solid var(--rule); }
.meta .r:first-child{ border-top:0; }
.meta .k{ width:42mm; flex:none; padding:2.3mm 4mm; background:var(--tint); font-family:Montserrat,"Segoe UI",Arial,sans-serif; font-weight:700; font-size:7.5pt; letter-spacing:.08em; text-transform:uppercase; color:var(--navy); }
.meta .v{ padding:2.3mm 4mm; font-size:9pt; }
.cover .sign{ position:absolute; left:14mm; bottom:0; font-size:9pt; color:var(--muted); }
.cover .sign b{ color:var(--navy); font-family:Montserrat,"Segoe UI",Arial,sans-serif; letter-spacing:.06em; }

/* ---------- sezioni */
section.page{ break-before:page; page-break-before:always; }
h2{ font-size:20pt; margin:0 0 5mm; padding-bottom:2.5mm; border-bottom:1.5px solid var(--navy); }
h2 span{ font-family:Montserrat,"Segoe UI",Arial,sans-serif; font-size:7.5pt; letter-spacing:.14em; text-transform:uppercase; color:var(--primary); display:block; margin-bottom:1mm; }
.prose{ max-width:258mm; font-size:9.2pt; margin:0 0 2.5mm; }
ol.sint{ list-style:none; margin:0; padding:0; columns:2; column-gap:10mm; column-fill:balance; }
ol.sint li{ break-inside:avoid; display:flex; gap:3.5mm; padding:2mm 0; border-top:1px solid var(--rule); font-size:9pt; }
ol.sint li:first-child{ border-top:0; }
ol.sint .n{ flex:none; width:9mm; font-family:"Playfair Display",Georgia,serif; font-size:17pt; font-weight:700; color:var(--primary); line-height:1; padding-top:.5mm; }
.legend{ display:flex; gap:10mm; margin:3mm 0 0; font-size:9pt; color:var(--muted); }
.pill{ display:inline-block; font-family:Montserrat,"Segoe UI",Arial,sans-serif; font-weight:700; font-size:6.5pt; letter-spacing:.1em; padding:.4mm 2mm; border-radius:6mm; vertical-align:middle; margin-left:1mm; line-height:1.5; }
.pl{ background:var(--tint); color:var(--navy); border:1px solid var(--primary); }
.pp{ background:var(--gold-bg); color:var(--gold); border:1px solid var(--gold); }

/* ---------- tabella a tre colonne */
table.rev{ width:100%; border-collapse:collapse; table-layout:fixed; font-size:8.7pt; }
table.rev thead th{ background:var(--navy); color:#fff; font-family:Montserrat,"Segoe UI",Arial,sans-serif; font-size:7.5pt; letter-spacing:.12em; text-transform:uppercase; text-align:left; padding:2.4mm 3mm; }
table.rev thead th+th{ border-left:1px solid rgba(255,255,255,.25); }
table.rev col.c1{ width:30%; } table.rev col.c2{ width:37%; } table.rev col.c3{ width:33%; }
table.rev tr.t td{ background:var(--tint); border:1px solid var(--rule); border-bottom:0; padding:2mm 3mm; font-family:"Playfair Display",Georgia,serif; font-size:11.5pt; color:var(--navy); break-after:avoid; page-break-after:avoid; }
table.rev tr.c td{ border:1px solid var(--rule); padding:2.4mm 3mm 1mm; vertical-align:top; }
table.rev tr.c td.era{ background:var(--era); } table.rev tr.c td.new{ background:var(--new); }
table.rev td p{ margin:0 0 1.8mm; }
table.rev td p.q{ color:#4A5A68; font-style:italic; }
table.rev td p.cl{ background:#fff; border-left:2px solid var(--primary); padding:1.4mm 2.2mm; font-style:italic; margin-bottom:2mm; }
table.rev tr{ break-inside:auto; }
.tblnote{ font-size:8.5pt; color:var(--muted); margin:2mm 0 4mm; }

/* ---------- altre tabelle */
table.pl2{ width:100%; border-collapse:collapse; font-size:8.2pt; table-layout:fixed; }
table.pl2 th, table.pl2 td{ border:1px solid var(--rule); padding:1.4mm 2.4mm; vertical-align:top; text-align:left; }
table.pl2 thead th{ background:var(--navy); color:#fff; font-family:Montserrat,"Segoe UI",Arial,sans-serif; font-size:7.5pt; letter-spacing:.12em; text-transform:uppercase; }
table.pl2 tbody th{ background:var(--tint); color:var(--navy); font-weight:600; width:30mm; }
table.pl2.dec tbody th{ background:var(--gold-bg); color:var(--gold); width:40mm; }
table.pl2 tr{ break-inside:avoid; page-break-inside:avoid; }
td.score{ font-family:"Playfair Display",Georgia,serif; font-size:17pt; font-weight:700; color:var(--navy); text-align:center; width:20mm; }
ol.leg{ margin:0; padding-left:5mm; max-width:210mm; font-size:8.6pt; line-height:1.35; } ol.leg li{ margin:1mm 0; padding-left:1mm; }
ul.refs{ margin:0; padding-left:5mm; font-size:8.3pt; max-width:240mm; } ul.refs li{ margin:1.2mm 0; overflow-wrap:anywhere; }
ul.refs a{ color:var(--primary); text-decoration:none; }
h2{ break-inside:avoid; page-break-inside:avoid; break-after:avoid; page-break-after:avoid; }
h2.sub2{ font-size:13pt; margin:6mm 0 3mm; } ol.two-col{ columns:2; column-gap:12mm; max-width:none; } ol.two-col li{ break-inside:avoid; } table.val td.score{ font-size:15pt; }
.closing{ margin-top:6mm; font-size:8.5pt; color:var(--muted); font-style:italic; }
"""

def build_print_html():
    meta = "".join('<div class="r"><div class="k">%s</div><div class="v">%s</div></div>' % (h(k), rich(v)) for k, v in META)
    sint = "".join('<li><span class="n">%02d</span><span>%s</span></li>' % (i, h(s)) for i, s in enumerate(SINTESI, 1))
    rows = []
    for r in ROWS:
        pills = "".join('<span class="pill %s">%s</span>' % ("pl" if t == "LEGALE" else "pp", t) for t in r["tags"])
        rows.append('<tr class="t"><td colspan="3">%s %s</td></tr><tr class="c"><td class="era">%s</td><td class="new">%s</td><td class="why">%s</td></tr>'
                    % (h(r["titolo"]), pills, items(r["era"]), items(r["proposta"]), items(r["perche"])))
    b2b = "".join('<tr><th>%s</th><td>%s</td><td>%s</td></tr>' % (h(a), h(b), h(c)) for a, b, c in B2B)
    dec = "".join('<tr><th>%s</th><td>%s</td></tr>' % (h(a), h(b)) for a, b in DECISIONI)
    leg = "".join('<li>%s</li>' % h(s) for s in LEGALE)
    val = "".join('<tr><th>%s</th><td class="score">%s</td><td>%s</td></tr>' % (h(a), h(b), h(c)) for a, b, c in VALUTAZIONE)
    refs = "".join('<li>%s%s</li>' % (h(t), (' — <a href="%s">%s</a>' % (u, h(u))) if u else "") for t, u in RIFERIMENTI)
    return f"""<!doctype html><html lang="it"><head><meta charset="utf-8"><title>{h(TITOLO)}</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Raleway:ital,wght@0,500;0,600;0,700;1,500&family=Montserrat:wght@700&display=block">
<style>{CSS}</style></head><body>

<div class="cover"><div class="band"></div><div class="body">
  <div class="eyebrow">Residence Veliero &amp; Altamarea · San Mauro Mare</div>
  <h1>{h(TITOLO)}</h1>
  <p class="sub">{h(SOTTOTITOLO)}</p>
  <div class="meta">{meta}</div>
</div>
  <div class="sign"><b>NEXAFRONTIERS</b> &nbsp;·&nbsp; revisione consulenziale &nbsp;·&nbsp; 31 agosto 2026 &nbsp;·&nbsp; riservato a Paolo e Marco Masini</div>
</div>

<section class="page">
  <h2><span>Prima di tutto</span>Sintesi in dieci punti</h2>
  <ol class="sint">{sint}</ol>
</section>

<section class="page">
  <h2><span>Il cuore del documento</span>Revisione articolo per articolo</h2>
  <p class="tblnote">Tre colonne per ogni articolo: <b>Com'era</b> cita la bozza del 31/08 (in corsivo il testo letterale); <b>Come dovrebbe essere</b> propone il testo — nei riquadri le clausole pronte da incollare, tra parentesi quadre i dati da inserire; <b>Perché</b> motiva ogni cambiamento con la fonte.
  &nbsp; <span class="pill pl">LEGALE</span> da validare con un avvocato del settore ricettivo &nbsp; <span class="pill pp">PROPRIETÀ</span> decisione dei titolari, non del contratto.</p>
  <table class="rev"><colgroup><col class="c1"><col class="c2"><col class="c3"></colgroup>
  <thead><tr><th>Com'era — bozza del 31/08</th><th>Come dovrebbe essere</th><th>Perché</th></tr></thead>
  <tbody>{"".join(rows)}</tbody></table>
</section>

<section class="page">
  <h2><span>La priorità del piano del 31/08</span>La variante aziendale (contratto quadro B2B)</h2>
  <p class="prose">{h(B2B_INTRO)}</p>
  <table class="pl2"><colgroup><col style="width:30mm"><col style="width:47%"><col></colgroup>
  <thead><tr><th>Voce</th><th>Come dovrebbe essere</th><th>Perché</th></tr></thead><tbody>{b2b}</tbody></table>
</section>

<section class="page">
  <h2><span>Cosa serve per chiudere</span>Decisioni della proprietà prima della firma</h2>
  <table class="pl2 dec"><tbody>{dec}</tbody></table>
  <h2 class="sub2"><span>Otto punti</span>Da far validare dal legale</h2>
  <ol class="leg two-col">{leg}</ol>
  <h2 class="sub2"><span>Giudizio</span>Valutazione</h2>
  <table class="pl2 val"><colgroup><col style="width:70mm"><col style="width:20mm"><col></colgroup><tbody>{val}</tbody></table>
</section>

<section style="margin-top:8mm; break-inside:avoid">
  <h2><span>Per verificare</span>Riferimenti</h2>
  <ul class="refs">{refs}</ul>
  <p class="closing">Revisione consulenziale a cura di NexaFrontiers, 31/08/2026. Non sostituisce il parere di un avvocato del settore ricettivo: le clausole marcate LEGALE vanno validate prima di ogni uso.</p>
</section>
</body></html>"""

def stamp(pdf_in, pdf_out):
    import fitz
    d = fitz.open(pdf_in); n = d.page_count
    for i, page in enumerate(d, 1):
        if i == 1:
            r = page.rect
            page.draw_rect(fitz.Rect(0, 0, 34, r.height), color=None, fill=(0.05, 0.35, 0.54))
            page.draw_rect(fitz.Rect(34, 0, 39, r.height), color=None, fill=(0.96, 0.88, 0.51))
            continue
        txt = f"Pagina {i} di {n}"
        w = fitz.get_text_length(txt, fontname="helv", fontsize=7.5)
        r = page.rect
        page.insert_text((r.width - 45 - w, r.height - 24), txt, fontsize=7.5, fontname="helv", color=(0.36, 0.42, 0.47))
        page.insert_text((45, r.height - 24), "Residence Veliero & Altamarea  ·  Revisione della bozza di contratto Long Stay  ·  NexaFrontiers, 31/08/2026", fontsize=7.5, fontname="helv", color=(0.36, 0.42, 0.47))
    d.set_metadata({"title": TITOLO + " — Residence Veliero", "author": "NexaFrontiers", "subject": SOTTOTITOLO,
                    "keywords": "Residence Veliero, contratto, long stay, RTA", "creator": "NexaFrontiers", "producer": "NexaFrontiers"})
    d.save(pdf_out, garbage=3, deflate=True); d.close(); return n

if __name__ == "__main__":
    here = Path(__file__).parent
    html_path = here / "revisione_print.html"; html_path.write_text(build_print_html(), encoding="utf-8")
    raw = here / "revisione_raw.pdf"
    cmd = [CHROME, "--headless=new", "--disable-gpu", f"--user-data-dir={here / 'chrome-profile'}", "--no-pdf-header-footer", "--virtual-time-budget=15000",
           "--run-all-compositor-stages-before-draw", f"--print-to-pdf={raw}", html_path.as_uri()]
    subprocess.run(cmd, check=True, capture_output=True, timeout=120)
    final = here / OUT_NAME
    n = stamp(raw, final)
    for dest in (DOWNLOADS / OUT_NAME, REPO / "docs" / "Revisione_Contratto_Long_Stay_Veliero_20260831.pdf"):
        shutil.copyfile(final, dest); print(f"{dest.stat().st_size:>8} B  {dest}")
    print("pagine:", n)
