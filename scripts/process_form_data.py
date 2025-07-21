#!/usr/bin/env python3
import json
from pathlib import Path
from datetime import datetime

# === CONFIGURATION ===
JSON_PATH = Path("data/Template for Processes.json")  # raw JSON filepath

# === LOAD JSON ===nif not JSON_PATH.exists():
    raise FileNotFoundError(f"JSON not found: {JSON_PATH}")
with JSON_PATH.open("r", encoding="utf-8") as f:
    row = json.load(f)

# === HELPER ===
def get_value(key: str) -> str:
    val = row.get(key, "")
    if isinstance(val, list):
        return ", ".join(map(str, val)).strip()
    return str(val or "").strip()

# === ESCAPE Markdown helper ===
_SPECIAL_MD_CHARS = set(r"\`*_{}[]()#+-.!|")
def escape_md(text: str) -> str:
    """Backslash-escape all Markdown-special characters in text."""
    return "".join(f"\\{c}" if c in _SPECIAL_MD_CHARS else c for c in text)

# === SECTION FOLDER ===
def determine_section() -> str:
    """Choose subfolder based on known Section/Category QIDs."""
    keys = [
        "r193faaedd19c49669e0600e0d11edfca",
        "rde080b09b05a47deb4c1111ff7ffc068",
        "r3a4399885e004123ad9c270fa3509b3a",
        "r1198559f25ba43629596c31ea3496e27",
    ]
    for qid in keys:
        sec = get_value(qid)
        if sec:
            return sec
    return "Uncategorized"

section = determine_section()

# === METADATA KEYS ===
meta = {
    'title':   get_value("r090df130b6a14e4da6842248a6fd9292"),
    'number':  get_value("rb161d63d7baa4ffb9f61ac63846ca8c8"),
    'author':  get_value("r5bc371d4242c4f09b7b7980d18211809"),
    'period':  get_value("r66c909f82883482fa07d3462e89e01e1") or "3 years",
    'purpose': (
        get_value("rb84d93fdf65d4fa89c1dc0796adc1607")
        or get_value("rba00b055bbf9454f83bec1ec4f37c0c8")
        or get_value("rc94139595a2c485c9a5cde963d202637")
    ),
    'date':    get_value("submitDate"),
}

# === STATIC STEP QID PAIRS ===
STEP_QIDS = [
    ("r97dc9b3936644c09a527fade2a8c2ced", "red79e9ae2dd9425094c408007e8b418f"),
    ("r7550fae0cae6497b9f5dd065a99619f1", "r2429caa9d171400e9402ac4a1f3711b8"),
    # ... (other 18 pairs unchanged)
]

# === OUTPUT PATH ===
out_dir = Path(section)
out_dir.mkdir(parents=True, exist_ok=True)
filename = f"{meta['number'].replace(' ','_')}_{meta['title'].replace(' ','_')}.md"
out_file = out_dir / filename

# === BUILD MARKDOWN ===
lines = [
    '---',
    f"title: {escape_md(meta['title'])}",
    f"author: {escape_md(meta['author'])}",
]
try:
    dt = datetime.fromisoformat(meta['date'])
    lines.append(f"date: {dt.isoformat()}")
except ValueError:
    lines.append(f"date: {escape_md(meta['date'])}")
lines += [
    f"review_period: {escape_md(meta['period'])}",
    '---',
    '',
    '## Purpose',
    escape_md(meta['purpose'] or 'N/A'),
    '',
    '## Steps',
    '',
    '| Step | Major Activity | References, Forms and Details |',
    '|------|----------------|-------------------------------|',
]

# === ENUMERATE STEPS WITH BULLETED LIST ===
for idx, (maj_q, det_q) in enumerate(STEP_QIDS, start=1):
    maj_raw = get_value(maj_q)
    if maj_raw:
        det_raw = get_value(det_q)
        # convert lines prefixed with '-' into list items
        items = []
        for line in maj_raw.splitlines():
            stripped = line.strip()
            if stripped.startswith('- '):
                items.append(stripped[2:].strip())
            elif stripped:
                items.append(stripped)
        # build HTML list
        maj_html = "<ul>" + "".join(f"<li>{escape_md(item)}</li>" for item in items) + "</ul>"
        det = escape_md(det_raw).replace("\n", "<br/>") if det_raw else 'N/A'
        lines.append(f"| {idx} | {maj_html} | {det} |")

# === WRITE FILE ===
out_file.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"✅ Created: {out_file}")
