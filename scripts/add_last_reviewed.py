#!/usr/bin/env python3
import os
import frontmatter
from git import Repo
from datetime import date

# Initialize GitPython repo at the workflow checkout directory
repo = Repo(os.getcwd())

def get_created_date(path):
    """
    Returns the ISO date of the first commit that added this file,
    or today’s date if Git history isn’t available.
    """
    commits = list(repo.iter_commits(paths=path, reverse=True, max_count=1))
    if not commits:
        return date.today().isoformat()
    # committed_datetime is a datetime; take the date portion
    return commits[0].committed_datetime.date().isoformat()

def process_folder(folder):
    """
    Walks the given folder and adds `last_reviewed` to any .md
    file missing it in front-matter.
    """
    for dirpath, _, filenames in os.walk(folder):
        for fn in filenames:
            if not fn.lower().endswith('.md'):
                continue

            full_path = os.path.join(dirpath, fn)
            post = frontmatter.load(full_path)

            if 'last_reviewed' in post.metadata:
                continue  # already seeded

            created = get_created_date(full_path)
            post.metadata['last_reviewed'] = created

            with open(full_path, 'w', encoding='utf-8') as f:
                frontmatter.dump(post, f)

            print(f"Added last_reviewed: {created} → {full_path}")

if __name__ == "__main__":
    # scan every top-level entry; if it's a folder whose name starts with a digit, process it
    for entry in os.listdir('.'):
        if os.path.isdir(entry) and entry[0].isdigit():
            process_folder(entry)
