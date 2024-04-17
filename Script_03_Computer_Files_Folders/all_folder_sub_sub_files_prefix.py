from pathlib import Path

root_dir = Path('Files_2')

for path in root_dir.glob('**/*'):
    if path.is_file():
        path_parts = path.parts
        subfolders = path.parts[1:-1]

        new_filename = "-".join(subfolders) + '-' + path.name + path.name
        print(new_filename)
        new_filepath = path.with_name(new_filename)
        path.rename(new_filepath) 
