from pathlib import Path
from markdown import markdown
from weasyprint import HTML

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "blue print plan" / "BLUEPRINT-PLAN.md"
OUT = ROOT / "blue print plan" / "BLUEPRINT-PLAN.pdf"

md = SRC.read_text(encoding="utf-8")
html_body = markdown(md, extensions=["tables", "fenced_code", "toc"])

html = f"""<!doctype html>
<html>
<head>
<meta charset="utf-8">
<style>
@page {{
  size: A4;
  margin: 18mm 16mm 18mm 16mm;
}}
body {{
  font-family: Arial, Helvetica, sans-serif;
  color: #172536;
  font-size: 10pt;
  line-height: 1.45;
}}
h1 {{ color: #10243B; font-size: 21pt; margin-bottom: 8pt; }}
h2 {{ color: #183D5D; font-size: 15pt; border-bottom: 1px solid #b6c7d1; padding-bottom: 4pt; margin-top: 18pt; }}
h3 {{ color: #0E6C86; font-size: 12pt; margin-top: 12pt; }}
table {{ width: 100%; border-collapse: collapse; margin: 8pt 0 12pt 0; font-size: 8.5pt; }}
th {{ background: #183D5D; color: white; text-align: left; }}
td, th {{ border: 1px solid #b7c6cf; padding: 5pt; vertical-align: top; }}
tr:nth-child(even) td {{ background: #f5f8fa; }}
code {{ background: #eef3f6; padding: 1pt 3pt; }}
pre {{ background: #f2f5f7; border: 1px solid #d3dde3; padding: 7pt; font-size: 8pt; white-space: pre-wrap; }}
blockquote {{ border-left: 4px solid #0E6C86; padding-left: 10pt; color: #355264; }}
li {{ margin-bottom: 3pt; }}
</style>
</head>
<body>
{html_body}
</body>
</html>"""

HTML(string=html).write_pdf(str(OUT))
print(OUT)
