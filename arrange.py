from pathlib import Path
import shutil
import sys

# =============================================================================
# Smart File Organizer
# Version : 2.1
# Purpose : Organize files in the folder where this program is located
# =============================================================================

print("=" * 80)
print("SMART FILE ORGANIZER")
print("=" * 80)

# -------------------------------------------------------------------------
# Determine the folder to organize
# -------------------------------------------------------------------------

if getattr(sys, "frozen", False):
    # Running as a PyInstaller executable
    target_folder = Path(sys.executable).parent
else:
    # Running as a Python script
    target_folder = Path(__file__).parent

# -------------------------------------------------------------------------
# File Extension Mapping
# -------------------------------------------------------------------------

file_types = {
    ".pdf": "PDF",

    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",

    ".doc": "Word",
    ".docx": "Word",

    ".xls": "Excel",
    ".xlsx": "Excel",

    ".csv": "CSV",
    ".parquet": "Data",

    ".ppt": "PowerPoint",
    ".pptx": "PowerPoint",

    ".txt": "Text",

    ".json": "JSON",

    ".zip": "Zip",

    ".mp4": "Video",
    ".mov": "Video",

    ".exe": "Applications",

    ".url": "Shortcuts",

    ".py": "Python"
}

# -------------------------------------------------------------------------
# Read all files except this program
# -------------------------------------------------------------------------

if getattr(sys, "frozen", False):
    program_name = Path(sys.executable).name
else:
    program_name = Path(__file__).name

files = [
    file
    for file in target_folder.iterdir()
    if file.is_file() and file.name != program_name
]

print(f"Folder : {target_folder}")
print(f"Files  : {len(files)}")
print("-" * 80)

moved = 0
duplicates = 0

# -------------------------------------------------------------------------
# Organize Files
# -------------------------------------------------------------------------

for file in files:

    extension = file.suffix.lower()

    destination_folder_name = file_types.get(extension, "Others")

    destination_folder = target_folder / destination_folder_name

    # Create destination folder if it does not exist
    destination_folder.mkdir(exist_ok=True)

    destination_file = destination_folder / file.name

    # Handle duplicate filenames
    if destination_file.exists():

        counter = 1

        while True:

            new_name = f"{file.stem}_{counter}{file.suffix}"

            destination_file = destination_folder / new_name

            if not destination_file.exists():
                break

            counter += 1

        duplicates += 1

    shutil.move(str(file), str(destination_file))

    moved += 1

    print(f"{file.name:<60} --> {destination_folder_name}")

# -------------------------------------------------------------------------
# Summary
# -------------------------------------------------------------------------

print("-" * 80)
print("Completed Successfully")
print("-" * 80)

print(f"Files Processed : {moved}")
print(f"Duplicate Files : {duplicates}")

input("\nPress Enter to Exit...")