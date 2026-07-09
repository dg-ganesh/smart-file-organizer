from pathlib import Path
import shutil

# ==========================================================
# Smart File Organizer - Restore Utility
# Moves files back to TestFiles and removes created folders
# ==========================================================

project_folder = Path(__file__).parent
test_folder = project_folder / "TestFiles"

print("=" * 80)
print("RESTORE FILES")
print("=" * 80)

restored = 0
removed_folders = 0

# Go through everything inside TestFiles
for item in test_folder.iterdir():

    # Ignore files already in the root TestFiles folder
    if item.is_file():
        continue

    # Process only folders
    if item.is_dir():

        print(f"\nChecking folder : {item.name}")

        # Move every file back to TestFiles
        for file in item.iterdir():

            if file.is_file():

                destination = test_folder / file.name

                # Handle duplicate names
                if destination.exists():

                    counter = 1

                    while True:

                        new_name = (
                            f"{file.stem}_{counter}"
                            f"{file.suffix}"
                        )

                        destination = test_folder / new_name

                        if not destination.exists():
                            break

                        counter += 1

                shutil.move(str(file), str(destination))

                restored += 1

                print(f"Restored : {file.name}")

        # Remove the folder if it's now empty
        if not any(item.iterdir()):
            item.rmdir()
            removed_folders += 1
            print(f"Removed folder : {item.name}")

print("\n" + "=" * 80)
print("Restore Complete")
print("=" * 80)
print(f"Files Restored : {restored}")
print(f"Folders Removed : {removed_folders}")