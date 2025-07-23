#!/usr/bin/env python3
import os
from datetime import datetime, timedelta
import frontmatter

# === CONFIGURATION ===
# Adjust root_dir if your markdown is not in top-level numbered folders
root_dir = '.'
flag_icon = '⚠️ '

def years_from_label(label: str):
    """Convert labels like '3 years' to integer years, or None for 'never'."""
    text = label.lower().strip()
    if text == 'never':
        return None
    try:
        return int(text.split()[0])
    except Exception:
        return None


def flag_title(title: str) -> str:
    """Prefix title with flag if not already present."""
    return title if title.startswith(flag_icon) else f"{flag_icon}{title}"


def unflag_title(title: str) -> str:
    """Remove leading flag from title."""
    if title.startswith(flag_icon):
        return title[len(flag_icon):].strip()
    return title


def process_file(path: str):
    """Load markdown, check review, update title if needed."""
    post = frontmatter.load(path)
    # Read metadata
    rp = post.metadata.get('review_period', 'never')
    years = years_from_label(rp)
    last_str = post.metadata.get('last_reviewed')

    # Determine new title
    title = post.metadata.get('title', '')
    new_title = title

    if years is None:
        # 'never' case: always unflag
        new_title = unflag_title(title)
    else:
        # Parse last_reviewed date
        try:
            last_date = datetime.fromisoformat(last_str).date()
        except Exception:
            # If missing/invalid, treat as due
            last_date = datetime.utcnow().date() - timedelta(days=years*365)
        # Compute if due
        if datetime.utcnow().date() >= last_date + timedelta(days=years*365):
            new_title = flag_title(title)
        else:
            new_title = unflag_title(title)

    # If title changed, write back
    if new_title != title:
        post.metadata['title'] = new_title
        # Write in binary to allow frontmatter.dump to write bytes
        with open(path, 'wb') as f:
            frontmatter.dump(post, f)
        print(f"Flag updated: {path}")
        return True
    return False


if __name__ == '__main__':
    changed = False
    for entry in os.listdir(root_dir):
        if entry[0].isdigit() and os.path.isdir(os.path.join(root_dir, entry)):
            for dirpath, _, files in os.walk(os.path.join(root_dir, entry)):
                for fname in files:
                    if fname.lower().endswith('.md'):
                        full_path = os.path.join(dirpath, fname)
                        if process_file(full_path):
                            changed = True

    if not changed:
        print("No flags needed.")
