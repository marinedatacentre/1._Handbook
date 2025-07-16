#!/usr/bin/env python3
import json
import base64
from pathlib import Path
from datetime import datetime

# === CONFIGURATION ===
JSON_PATH   = Path("data/Template_for_Media_Processes.json")  # replace with your actual JSON filename
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

# === ROUTING ===
def determine_section() -> str:
    # Branch-specific Section QIDs in priority order
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
TITLE_QID  = "r090df130b6a14e4da6842248a6fd9292"  # Title
NUMBER_QID = "rb161d63d7baa4ffb9f61ac63846ca8c8"  # Number
AUTHOR_QID = "r5bc371d4242c4f09b7b7980d18211809"  # Created by
DATE_QID   = "submitDate"                       # submission timestamp
INFO_QID   = "r97dc9b3936644c09a527fade2a8c2ced"  # General information textbox
PHOTO_QID  = "r072985e75ce540dc8129db3d105d0737"  # File upload (JSON-encoded array)

# === EXTRACT METADATA ===
meta = {
    'title':  get_value(TITLE_QID),
    'number': get_value(NUMBER_QID),
    'author': get_value(AUTHOR_QID),
    'date':   get_value(DATE_QID),
    'info':   get_value(INFO_QID)
}

# === FORMAT OUTPUT PATHS ===
out_dir = OUTPUT_ROOT / section
out_dir.mkdir(parents=True, exist_ok=True)

safe_num   = meta['number'].replace(' ', '_').replace('/', '-')
safe_title = meta['title'].replace(' ', '_').replace('/', '-')

# Markdown file
md_file = out_dir / f"{safe_num}_{safe_title}.md"
# Image file: take first entry in the JSON array
img_ext = '.jpg'
img_file = out_dir / f"{safe_num}_{safe_title}{img_ext}"

# === WRITE IMAGE ===
# Forms file-upload QID returns a JSON array with name/link/id
# We'll fetch the link URL and embed it rather than base64-decoding
import urllib.request
files = json.loads(get_value(PHOTO_QID) or '[]')
if files:
    file_info = files[0]
    img_url = file_info.get('link')
    # download the image
    try:
        data = urllib.request.urlopen(img_url).read()
        img_file.write_bytes(data)
    except Exception as e:
        print(f"⚠️ Failed to download image: {e}")
else:
    img_url = None

# === BUILD MARKDOWN ===
lines = [
    '---',
    f"title: {meta['title']}",
    f"author: {meta['author']}",
]
# normalize date
try:
    dt = datetime.fromisoformat(meta['date'])
    lines.append(f"date: {dt.isoformat()}")
except Exception:
    lines.append(f"date: {meta['date']}")
lines += [
    '---',
    '',
    '## Information',
    meta['info'] or 'N/A',
    ''
]
if img_url:
    rel = img_file.name
    lines += [
        '## Uploaded Photo',
        f"![Photo]({rel})",
        ''
    ]

# === WRITE MARKDOWN ===
md_file.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"✅ Created: {md_file}")
