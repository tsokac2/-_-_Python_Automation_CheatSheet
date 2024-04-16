<h1 align="center">Working with Computer Files and Folders</h1>

### Overview of the Section
* **[Python Pathlib Library](#path-lib)**
* **[Add Prefix to Files and Folder](#prefix)**
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