from pathlib import Path
import csv
import hashlib
from datetime import datetime

ROOT = Path(r"research_corpus\Kinetic Economy")
OUT = ROOT / "_inventory"
OUT.mkdir(exist_ok=True)

MANIFEST = OUT / "research_manifest.csv"
DUPES = OUT / "duplicate_report.csv"
SUMMARY = OUT / "corpus_summary.md"


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


files = [
    p for p in ROOT.rglob("*")
    if p.is_file() and "_inventory" not in p.parts
]

rows = []
seen = {}

for i, path in enumerate(sorted(files), start=1):
    checksum = sha256_file(path)
    source_id = f"codex_src_{i:06d}"
    rel_path = path.relative_to(ROOT)

    row = {
        "source_id": source_id,
        "original_filename": path.name,
        "relative_path": str(rel_path),
        "file_type": path.suffix.lower().replace(".", ""),
        "file_size_bytes": path.stat().st_size,
        "last_modified": datetime.fromtimestamp(path.stat().st_mtime).isoformat(timespec="seconds"),
        "checksum_sha256": checksum,
        "status": "inventory_complete",
    }
    rows.append(row)
    seen.setdefault(checksum, []).append(row)

with open(MANIFEST, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys() if rows else [])
    writer.writeheader()
    writer.writerows(rows)

dupes = [group for group in seen.values() if len(group) > 1]

with open(DUPES, "w", newline="", encoding="utf-8") as f:
    fieldnames = rows[0].keys() if rows else []
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for group in dupes:
        writer.writerows(group)

type_counts = {}
for row in rows:
    type_counts[row["file_type"]] = type_counts.get(row["file_type"], 0) + 1

with open(SUMMARY, "w", encoding="utf-8") as f:
    f.write("# Research Corpus Inventory Summary\n\n")
    f.write(f"Total files: {len(rows)}\n\n")
    f.write("## File Types\n\n")
    for file_type, count in sorted(type_counts.items()):
        f.write(f"- {file_type or 'no_extension'}: {count}\n")
    f.write(f"\n## Duplicate Groups\n\n")
    f.write(f"Duplicate groups found: {len(dupes)}\n")

print(f"Manifest written to: {MANIFEST}")
print(f"Duplicate report written to: {DUPES}")
print(f"Summary written to: {SUMMARY}")
