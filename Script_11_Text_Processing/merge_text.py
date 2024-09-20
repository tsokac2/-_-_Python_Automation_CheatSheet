# Merge CSV Files Excluding the Header
from pathlib import Path
files_dir = Path('files')

merged = ''
for index, filepath in enumerate(files_dir.iterdir()):
    with open(filepath, 'r') as file:
        content = file.readlines()
        new_content = content[1:]
    if index == 0:
        content = ''.join(content)    
        merged = merged + content + '\n'
    else:
        new_content = ''.join(new_content)
        merged = merged + new_content + '\n'

with open('merged.csv', 'w') as file:
    file.write(merged)

# Merge TXT and CSV Files
# from pathlib import Path
# files_dir = Path('files')

# merged = ''
# for filepath in files_dir.iterdir():
#     with open(filepath, 'r') as file:
#         content = file.read()
#     merged = merged + content + '\n'

# with open('merged.csv', 'w') as file:
#     file.write(merged)