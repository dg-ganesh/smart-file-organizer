# Smart File Organizer

A lightweight Python utility that automatically organizes files into folders based on their file type.

## Features

* Automatically scans the folder where the program is located.
* Creates folders for different file types.
* Moves files into their appropriate folders.
* Works without requiring user input.
* Can be packaged as a standalone Windows executable using PyInstaller.
* Includes a reverse utility to restore the original folder structure.

## Supported File Types

Examples include:

* Documents
* PDFs
* Images
* Videos
* Audio
* Archives
* Spreadsheets
* Presentations
* Source Code
* Others

## Project Structure

```text
Smart-File-Organizer/
│
├── arrange.py
├── reverse_arrange.py
├── README.md
├── requirements.txt
├── .gitignore
├── screenshots/
└── TestFiles/
```

## Requirements

* Python 3.14 or later

## Installation

Clone the repository:

```bash
git clone https://github.com/dg-ganesh/smart-file-organizer.git
```

Move into the project directory:

```bash
cd smart-file-organizer
```

## Running the Program

Using Python:

```bash
python arrange.py
```

To restore the original folder structure:

```bash
python reverse_arrange.py
```

## Creating a Standalone Executable

Install PyInstaller:

```bash
pip install pyinstaller
```

Build the executable:

```bash
pyinstaller --onefile arrange.py
```

The executable will be available inside the `dist` folder.

## Screenshots

Example screenshots are available in the `screenshots` folder.

## Future Improvements

* Custom file categories
* Configuration file support
* Logging
* Duplicate file detection
* File preview mode
* Undo functionality
* Drag-and-drop support
* Cloud storage integration

## License

This project is licensed under the MIT License.

## Author

**Ganesh DG**

GitHub: https://github.com/dg-ganesh
