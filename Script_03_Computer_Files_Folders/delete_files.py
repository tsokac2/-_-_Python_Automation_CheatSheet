from pathlib import Path

root_dir = Path("Files_3")

for path in root_dir.glob("*.zip"):
    with open(path, 'wb') as file:
        file.write(b'')
    path.unlink()