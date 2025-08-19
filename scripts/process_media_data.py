#!/usr/bin/env python3
import json
import requests
import urllib.request
from pathlib import Path
from datetime import datetime

# === CONFIGURATION ===
JSON_PATH        = Path("data/Template_for_Media_Processes.json")
OUTPUT_ROOT      = Path('.')
GITHUB_REPO_BASE = "https://github.com/marinedatacentre/1._Handbook/blob/main"

# === LOAD FORM JSON ===
if not JSON_PATH.exists():
    raise FileNotFoundError(f"JSON file not found: {JSON_PATH}")
with JSON_PATH.open("r", encoding="utf-8") as f:
    row = json.load(f)

# === SIMPLE GETTER ===
def get_value(key: str) -> str:
    v = row.get(key, "")
    if isinstance(v, list):
        return ", ".join(map(str, v)).strip()
    return str(v or "").strip()

# === MD ESCAPE ===
_SPECIAL_MD_CHARS = set(r"\`*_{}[]()#+-.!|")
def escape_md(text: str) -> str:
    return "".join(f"\\{c}" if c in _SPECIAL_MD_CHARS else c for c in text)

# === SECTION ROUTING ===
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

# === QIDs ===
TITLE_QID   = "r090df130b6a14e4da6842248a6fd9292"
NUMBER_QID  = "rb161d63d7baa4ffb9f61ac63846ca8c8"
AUTHOR_QID  = "r5bc371d4242c4f09b7b7980d18211809"
DATE_QID    = "submitDate"
REVIEW_QID  = "r66c909f82883482fa07d3462e89e01e1"
INFO_QID    = "r97dc9b3936644c09a527fade2a8c2ced"
PHOTO_QID   = "r072985e75ce540dc8129db3d105d0737"

# === EXTRACT METADATA ===
meta = {
    'title':  get_value(TITLE_QID),
    'number': get_value(NUMBER_QID),
    'author': get_value(AUTHOR_QID),
    'date':   get_value(DATE_QID),
    'period': get_value(REVIEW_QID) or "3 years",
    'info':   get_value(INFO_QID)
}

# === SET UP OUTPUT DIRS ===
section   = determine_section()
out_dir   = OUTPUT_ROOT / section
media_dir = out_dir / "media"
out_dir.mkdir(parents=True, exist_ok=True)
media_dir.mkdir(parents=True, exist_ok=True)

safe_num   = meta['number'].replace(' ', '_').replace('/', '-')
safe_title = meta['title'].replace(' ', '_').replace('/', '-')
md_file    = out_dir / f"{safe_num}_{safe_title}.md"

# === PARSE ALL UPLOADED FILES ===
files  = json.loads(get_value(PHOTO_QID) or '[]')
images = []  # list of (local_filename, remote_url)

for file_info in files:
    remote = file_info.get('link')
    orig   = file_info.get('name', '')
    if not remote or not orig:
        continue

    orig_stem = Path(orig).stem
    safe_orig = orig_stem.replace(' ', '_').replace('/', '-')
    ext       = Path(orig).suffix or ".jpg"

    local_name = f"{safe_num}_{safe_title}_{safe_orig}{ext}"
    images.append((local_name, remote))

# === DOWNLOAD EACH IMAGE INTO media/ ===
for local_name, remote_url in images:
    target = media_dir / local_name
    try:
        resp = requests.get(
            remote_url,
            headers={'Accept': 'application/vnd.github.v3.raw'},
            timeout=10
        )
        resp.raise_for_status()
        target.write_bytes(resp.content)
    except Exception:
        try:
            urllib.request.urlretrieve(remote_url, target)
        except Exception as e:
            print(f"⚠️ Warning: failed to download {remote_url}: {e}")

# === BUILD THE MARKDOWN ===
# stamp today as last_reviewed
today = datetime.utcnow().date().isoformat()

lines = [
    '---',
    f"title: {escape_md(meta['title'])}",
    f"author: {escape_md(meta['author'])}",
]
# normalize date
try:
    dt = datetime.fromisoformat(meta['date'])
    lines.append(f"date: {dt.isoformat()}")
except Exception:
    lines.append(f"date: {escape_md(meta['date'])}")
# existing review_period
lines.append(f"review_period: {escape_md(meta['period'])}")
# new last_reviewed field
lines.append(f"last_reviewed: {today}")
lines.append('---')
lines.append('')

lines.append('## Information')
info_raw   = meta['info'] or 'N/A'
info_lines = info_raw.splitlines()
header     = None
if info_lines and not info_lines[0].startswith('- '):
    header = info_lines[0].strip()
bullets = [l.strip()[2:].strip() for l in info_lines if l.strip().startswith('- ')]
if bullets:
    parts = []
    if header:
        parts.append(escape_md(header))
    parts.append(
        '<ul>' + ''.join(f"<li>{escape_md(b)}</li>" for b in bullets) + '</ul>'
    )
    lines.append(''.join(parts))
else:
    lines.append(escape_md(info_raw).replace("\n", "<br/>"))
lines.append('')

if images:
    title = "Uploaded Photo" + ("s" if len(images) > 1 else "")
    lines.append(f"## {title}")
    lines.append('')
    for local_name, _ in images:
        github_url = f"{GITHUB_REPO_BASE}/{section}/media/{local_name}"
        rel_path   = f"media/{local_name}"
        lines.append(f"[![Photo]({rel_path})]({github_url})")
    lines.append('')

# === WRITE OUT ===
md_file.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"✅ Created: {md_file}")
