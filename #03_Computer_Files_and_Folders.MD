<h1 align="center">Working with Computer Files and Folders</h1>

### Overview of the Section
* **[Python Pathlib Library](#path-lib)**
* **[Add Prefix to Files and Folder](#prefix)**
* **[Create Empty Files](#empty-files)**
* **[Create Archive from Files](#archive-files)**
* **[Delete Files](#delete-files)**

#
### <a name="path-lib">Python Pathlib Library</a>

**What is Pathlib?**
- A standard Python library for working with file and directory paths.
- Introduced in Python version 3.4.
- Recommended way to handle paths instead of using strings.

**How to use Pathlib**:
- Import the ``pathlib`` library:
    ```
    from pathlib import Path
    ```
- Create a Path object by passing a string path:
    ```
    p1 = Path("files/abc.txt")
    ```
- Check if a path exists:
    ```
    if p1.exists():
        # Do something if the path exists
    ```
- Create a new file (if it doesn't exist):
    ```
    p1.write_text("Contents three")
    ```
- Get specific parts of a path:
    ```
    # Get filename
    p1.name

    # Get filename without extension
    p1.stem

    # Get extension
    p1.suffix
    ```
- Get a list of files and directories in a path:
    ```
    for item in p2.iterdir():
        print(item)
    ```
The methods used to interact with paths are:
- ``exists()`` - Check if a path exists
- ``write_text()`` - Write text to a file
- ``name`` - Get filename
- ``stem`` - Get filename without extension
- ``suffix`` - Get extension
- ``iterdir()`` - Get an iterator of files and directories within a path

**[Back To The Top](#Overview-of-the-Section)**
#

### <a name="prefix">Add Prefix to Files and Folder</a>

**Working with Paths**:
Use pathlib.Path to create path objects from file/directory paths (instead of raw strings).

**Important code**:
```
from pathlib import Path
```

**Renaming Files**:
- Be mindful of the current working directory when creating new file paths.
- Use ``path.with_name(new_name)`` to create a new path object with the desired filename for the existing path.

**Important code**:
```
new_file_path = path.with_name(new_file_name)
```

**Correct approach to renaming**:
```
for path in file_paths:
  new_file_name = f"new-+{path.stem}{path.suffix}"
  new_file_path = path.with_name(new_file_name)
  path.rename(new_file_path)
```
**[Back To The Top](#Overview-of-the-Section)**
#

### <a name="empty-files">Create Empty Files</a>

**Creating many empty files**:

- This script creates empty files inside a directory called "files".
- It uses a loop (for i in range(10, 21)) to iterate through a range of numbers.
- Inside the loop:
    - Constructs a filename string by combining the number (i) with ".txt" extension (adjust the extension as needed).
    - Creates a file path object by combining the root directory ("files/") with the filename string.
    - Uses the os.path.join function (not explicitly mentioned in the text but implied) to create the file path.
    - Creates the empty file using the path.touch() method.

**Important code**:
```
# Assuming you have imported the os module
# Loop to iterate through a range of numbers (10 to 20)

for i in range(10, 21):
  # Construct filename string
  filename = str(i) + ".txt"  # Adjust the extension as needed

  # Create file path object
  filepath = os.path.join("files", filename)

  # Create the empty file
  path.touch(filepath)
```

**Note**:

- The text mentions ``os.path`` module but not ``os.path.join`` function explicitly. However, ``os.path.join`` is commonly used for creating file paths.
- This code creates 20 files named _"10.txt"_ to _"20.txt"_. You can modify the loop and filename construction to create files with different names.

**[Back To The Top](#Overview-of-the-Section)**
#
### <a name="archive-files">Create Archive from Files</a>

**Creating a ZIP file**:

- Libraries: pathlib (for working with file paths) and zipfile (for creating ZIP files).
- Important code:
    - ``zip = zipfile.ZipFile(archive_path, 'w')`` # Creates a ZIP file object named ``archive_path`` in write mode ('w').
    - ``zip.write(file_path)`` # Adds a file ``(file_path)`` to the ZIP archive.

**Iterating through files and adding them to the ZIP**:
- Use glob to find all files with a specific extension (e.g., .txt).
- Loop through each file and add it to the ZIP using zip.write(file_path).

**Deleting original files after adding them to the ZIP (Optional)**:
- Use path.unlink() to delete a file after adding it to the ZIP.

**Note**:
- The text uses uppercase and lowercase for ``zipfile`` inconsistently. The correct import is ``from zipfile import ZipFile``.

**[Back To The Top](#Overview-of-the-Section)**
#
### <a name="delete-files">Delete Files</a>

**Goal**: This script aims to securely delete files by overwriting their contents and then deleting them.

**Important concepts**:
- ``glob`` module (use with caution): Used to iterate through files in a directory, but be cautious as it can also process subfolders.
- ``os.path.join(root, file):`` This constructs the full path to each file within the root directory.
- ``open(path, 'wb'):`` Opens a file in write binary mode ('wb'). This allows overwriting of any file type (text or binary).
- ``file.write(b''):`` Writes an empty byte sequence to the opened file, effectively erasing its contents.
- ``os.unlink(path):`` Deletes the specified file.

**Code snippet (important parts)**:
```
import os

# Replace 'path/to/your/directory' with the actual directory containing your files
root = 'path/to/your/directory'

# Loop through all CSV files in the root directory
for file in glob.glob(os.path.join(root, "*.csv")):
  with open(file, 'wb') as f:
    f.write(b'')  # Write empty bytes to erase content
  os.unlink(file)  # Delete the file
```
**Warning**:
- Be extra cautious while using ``glob`` as it can process subfolders potentially deleting unintended files.
- This script permanently deletes files. Make sure you have backups before running it.

**[Back To The Top](#Overview-of-the-Section)**