from pathlib import Path
import zipfile

root_dir = Path("Files_3")
archive_path = Path('archive.zip')

with zipfile.ZipFile(archive_path, 'w') as zf:
    for path in root_dir.rglob("*.txt"):
        zf.write(path)