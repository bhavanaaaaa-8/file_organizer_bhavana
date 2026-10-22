# Automatic File Organizer

## Description
The Automatic File Organizer is a Python script that scans a specified folder and automatically organizes files into subfolders based on their file extensions. It uses `pathlib` for readable filesystem operations and `shutil` to move files.

## Features
- Organizes files into categories such as Images, Documents, Videos, Audio, and Python Files.
- Places unknown file types into an `Others` folder.
- Places files without extensions into a `No Extension` folder.
- Creates category folders automatically when needed.
- Skips directories and avoids overwriting existing files.
- Handles invalid folder paths and file-moving errors.

## Technologies Used
- Python 3
- `pathlib` — filesystem path handling
- `shutil` — moving files

## How to Run

1. Install Python 3 on your computer.
2. Download or clone this repository.
3. Open a terminal in the project directory.
4. Run the script:

   ```bash
   python file_organizer.py
   ```

5. Enter the folder path you want to organize when prompted.

## Example

**Before:**
```text
Downloads/
├── photo.jpg
├── notes.pdf
├── song.mp3
└── video.mp4
```

**After:**
```text
Downloads/
├── Images/
│   └── photo.jpg
├── Documents/
│   └── notes.pdf
├── Audio/
│   └── song.mp3
└── Videos/
    └── video.mp4
```

## Important Note
The script moves files instead of copying them. Test it on a sample folder before running it on important files.

## Future Improvements
- Add a dry-run mode to preview changes before moving files.
- Support additional file extensions.
- Generate a log file of organized files.
- Allow users to customize file categories.

## License
This project is available for educational and personal use.
