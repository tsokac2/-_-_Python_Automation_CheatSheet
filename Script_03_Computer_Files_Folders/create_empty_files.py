from pathlib import Path
root_dir = Path("Files_3")

for i in range(10, 21):
    filename = str(i) + '.txt'
    filepath = root_dir / Path(filename)
    filepath.touch()