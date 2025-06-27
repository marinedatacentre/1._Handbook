import os
import pandas as pd
from pathlib import Path

# === CONFIG ===
EXCEL_PATH = "data/Template for Processes.xlsx"
OUTPUT_DIR = Path("handbook.md")

# === LOAD DATA ===
df = pd.read_excel(EXCEL_PATH)

# Normalize column headers (fix weird non-breaking spaces)
df.columns = [col.replace("\xa0", " ").strip() for col in df.columns]

for index, row in df.iterrows():
    folder_type = str(row.get("Pick a Folder", "")).strip()
    section = str(row.get("Section/Category", "")).strip()
    process_title = str(row.get("Process Title", "")).strip()
    process_number = str(row.get("Process Number", "")).strip()
    created_by = str(row.get("Created by", "")).strip()
    review_period = str(row.get("Review Period", "")).strip()
    purpose = str(row.get("Purpose", "")).strip()

    # File & folder paths
    filename = f"{process_number} - {process_title}.md".replace("/", "-")
    folder_path = OUTPUT_DIR / section
    file_path = folder_path / filename

    if file_path.exists():
        continue

    # === BUILD MARKDOWN ===
    md = f"""---
title: {process_title}
author: {created_by}
date: {row.get('Start time', '')}
review_period: {review_period or '3 years'}
---

## Purpose
{purpose}

## Steps

| Step | Major Activity | References, Forms and Details |
|------|----------------|-------------------------------|
"""

    for i in range(1, 21):
        major = str(row.get(f"Step {i}: Major Activity", "")).strip()
        detail = str(row.get(f"Step {i}: References, Forms and Details", "")).strip()

        if major and major.lower() != "nan":
            clean_major = major.replace("|", "\\|")  # Escape pipes
            clean_detail = (detail or "N/A").replace("|", "\\|")
            md += f"| {i} | {clean_major} | {clean_detail} |\n"
