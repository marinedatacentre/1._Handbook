# === SET UP OUTPUT DIRS ===
section   = determine_section()
out_dir   = OUTPUT_ROOT / section
media_dir = out_dir / "media"
out_dir.mkdir(parents=True, exist_ok=True)
media_dir.mkdir(parents=True, exist_ok=True)

# ensure media/ is kept even if empty so it's visible in GitHub
gitkeep = media_dir / ".gitkeep"
if not gitkeep.exists():
    gitkeep.write_text("", encoding="utf-8")

safe_num   = meta['number'].replace(' ', '_').replace('/', '-')
safe_title = meta['title'].replace(' ', '_').replace('/', '-')
md_file    = out_dir / f"{safe_num}_{safe_title}.md"

# === PARSE ALL UPLOADED FILES ===
raw_files = get_value(PHOTO_QID) or '[]'
try:
    files = json.loads(raw_files)
except Exception:
    files = []  # not JSON → nothing to download

images = []  # list of (local_filename, remote_url)

for file_info in files:
    # accept various shapes
    remote = file_info.get('link') or file_info.get('url') or file_info.get('href')
    orig   = file_info.get('name') or file_info.get('filename') or ''
    if not remote:
        continue

    # name fallback
    if not orig:
        orig = Path(remote).name.split('?')[0]  # strip query if present

    orig_stem = Path(orig).stem
    safe_orig = orig_stem.replace(' ', '_').replace('/', '-')
    ext       = Path(orig).suffix or ".jpg"

    local_name = f"{safe_num}_{safe_title}_{safe_orig}{ext}"
    images.append((local_name, remote))

print(f"[media] Found {len(images)} image(s) to download into {media_dir}")

# === DOWNLOAD EACH IMAGE INTO media/ ===
for local_name, remote_url in images:
    target = media_dir / local_name
    try:
        resp = requests.get(
            remote_url,
            headers={
                # try raw/octet just in case the host is picky
                'Accept': 'application/octet-stream,application/vnd.github.v3.raw;q=0.9,*/*;q=0.8'
            },
            timeout=20
        )
        resp.raise_for_status()
        target.write_bytes(resp.content)
        print(f"[media] downloaded → {target}")
    except Exception as e1:
        # fallback if requests fails
        try:
            urllib.request.urlretrieve(remote_url, target)
            print(f"[media] urlretrieve fallback → {target}")
        except Exception as e2:
            print(f"⚠️ [media] failed: {remote_url}\n   requests: {e1}\n   urlretrieve: {e2}")
