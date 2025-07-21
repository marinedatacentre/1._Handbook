#!/usr/bin/env python3
import json
from pathlib import Path
from datetime import datetime

# === CONFIGURATION ===
JSON_PATH   = Path("data/Template_for_Media_Processes.json")  # raw JSON filepath
OUTPUT_ROOT = Path('.')

# === LOAD JSON ===
if not JSON_PATH.exists():
    raise FileNotFoundError(f"JSON file not found: {JSON_PATH}")
with JSON_PATH.open("r", encoding="utf-8") as f:
    row = json.load(f)

# === HELPER ===
def get_value(key: str) -> str:
    v = row.get(key, "")
    if isinstance(v, list):
        return ", ".join(map(str, v)).strip()
    return str(v or "").strip()

# === ESCAPE Markdown helper ===
_SPECIAL_MD_CHARS = set(r"\`*_{}[]()#+-.!|")
def escape_md(text: str) -> str:
    """Backslash-escape all Markdown-special characters in text."""
    return "".join(f"\\{c}" if c in _SPECIAL_MD_CHARS else c for c in text)

# === ROUTING ===
def determine_section() -> str:
    keys = [
        "r193faaedd19c49669e0600e0d11edfca",  # Handbook
        "rde080b09b05a47deb4c1111ff7ffc068",  # Handbook Companion
        "r3a4399885e004123ad9c270fa3509b3a",  # Project Specific Processes
        "r1198559f25ba43629596c31ea3496e27"   # Data Repository
    ]
    for qid in keys:
        sec = get_value(qid)
        if sec:
            return sec
    return "Uncategorized"

section = determine_section()

# === METADATA QIDs ===
TITLE_QID   = "r090df130b6a14e4da6842248a6fd9292"  # Title
NUMBER_QID  = "rb161d63d7baa4ffb9f61ac63846ca8c8"  # Number
AUTHOR_QID  = "r5bc371d4242c4f09b7b7980d18211809"  # Created by
DATE_QID    = "submitDate"                       # submission timestamp
REVIEW_QID  = "r66c909f82883482fa07d3462e89e01e1"  # Review Period
INFO_QID    = "r97dc9b3936644c09a527fade2a8c2ced"  # Information textbox
PHOTO_QID   = "r072985e75ce540dc8129db3d105d0737"  # File upload JSON array

# === EXTRACT METADATA ===
meta = {
    'title':  get_value(TITLE_QID),
    'number': get_value(NUMBER_QID),
    'author': get_value(AUTHOR_QID),
    'date':   get_value(DATE_QID),
    'period': get_value(REVIEW_QID) or "3 years",
    'info':   get_value(INFO_QID)
}

# === PREPARE OUTPUT PATH ===
out_dir = OUTPUT_ROOT / section
out_dir.mkdir(parents=True, exist_ok=True)

safe_num   = meta['number'].replace(' ', '_').replace('/', '-')
safe_title = meta['title'].replace(' ', '_').replace('/', '-')

md_file    = out_dir / f"{safe_num}_{safe_title}.md"

# === PARSE IMAGE URL ===
files = json.loads(get_value(PHOTO_QID) or '[]')
img_url = files[0].get('link') if files else None

# === BUILD MARKDOWN ===
lines = [
    '---',
    f"title: {escape_md(meta['title'])}",
    f"author: {escape_md(meta['author'])}",
]
# Date normalization
try:
    dt = datetime.fromisoformat(meta['date'])
    lines.append(f"date: {dt.isoformat()}")
except Exception:
    lines.append(f"date: {escape_md(meta['date'])}")
# Review period
lines.append(f"review_period: {escape_md(meta['period'])}")
# Close front-matter
lines.append('---')

# Body
lines.append('')
lines.append('## Information')

# === RENDER INFO WITH OPTIONAL HEADER + BULLETS ===
info_raw = meta['info'] or 'N/A'
info_lines = info_raw.splitlines()
# Detect header line (first line without '- ')
header = None
if info_lines and not info_lines[0].strip().startswith('- '):
    header = info_lines[0].strip()
# Extract bullet items
bullet_items = [
    line.strip()[2:].strip()
    for line in info_lines
    if line.strip().startswith('- ')
]
# Build HTML or plain text
if bullet_items:
    parts = []
    if header:
        parts.append(escape_md(header))
    parts.append(
        '<ul>' + ''.join(f"<li>{escape_md(item)}</li>" for item in bullet_items) + '</ul>'
    )
    lines.append(''.join(parts))
else:
    # plain text with line-breaks
    escaped = escape_md(info_raw)
    lines.append(escaped.replace("\n", "<br/>"))

lines.append('')

# Images
img_filename = f"{safe_num}_{safe_title}.jpg"
if img_filename and (out_dir / img_filename).exists():
    lines.extend([  
        '## Uploaded Photo',
        f"![Photo]({img_filename})",
        ''
    ])

# === WRITE FILE ===
md_file.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"✅ Created: {md_file}")
