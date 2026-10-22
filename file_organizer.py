
from pathlib import Path
import shutil


def organize_files(folder_path):
    folder = Path(folder_path)

    if not folder.is_dir():
        print("Error: Folder does not exist.")
        return

    file_count = 0

    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
        "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
        "Videos": [".mp4", ".mkv", ".avi", ".mov"],
        "Audio": [".mp3", ".wav", ".aac"],
        "Python Files": [".py"],
    }

    for file_path in folder.iterdir():
        if not file_path.is_file():
            continue

        extension = file_path.suffix.lower()
        folder_name = "Others"

        if not extension:
            folder_name = "No Extension"
        else:
            for category, extensions in file_types.items():
                if extension in extensions:
                    folder_name = category
                    break

        destination_folder = folder / folder_name
        destination_folder.mkdir(exist_ok=True)

        destination_path = destination_folder / file_path.name

        # Avoid overwriting existing files
        if destination_path.exists():
            print(f"Skipped: {file_path.name} (already exists)")
            continue

        try:
            shutil.move(str(file_path), str(destination_path))
            print(f"Moved: {file_path.name} -> {folder_name}")
            file_count += 1
        except OSError as error:
            print(f"Could not move {file_path.name}: {error}")

    print(f"\nOrganization complete! {file_count} files moved.")


folder_path = input("Enter the folder path to organize: ").strip()
folder_path = Path(folder_path).expanduser()

organize_files(folder_path)
