"""Wraps src/body.html into a full HTML document at public/index.html for Firebase Hosting / App Engine."""
from pathlib import Path

root = Path(__file__).parent
body = (root / "src" / "body.html").read_text(encoding="utf-8")

head = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="Ashgrove Reduction Surgery: breast reduction for women and men in Pasadena, California. Wise-pattern, vertical, liposuction and male breast reduction.">
<meta property="og:title" content="Ashgrove Reduction Surgery">
<meta property="og:description" content="Relief you can measure in grams.">
<meta property="og:type" content="website">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<style>[hidden]{display:none!important}img{max-width:100%}body{margin:0}</style>
"""

# Split the artifact body at the first <svg> sprite: everything before it belongs in <head>.
split_at = body.index('<svg width="0"')
html = head + body[:split_at] + "</head>\n<body>\n" + body[split_at:] + "\n</body>\n</html>\n"

out = root / "public"
out.mkdir(exist_ok=True)
(out / "index.html").write_text(html, encoding="utf-8")
print(f"Wrote {out / 'index.html'} ({len(html):,} bytes)")
