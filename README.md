# Keyword File Scanner

This is a simple command-line tool that walks a directory tree, counts how many files it contains, and searches each file for a given keyword. It reports matches found in filenames and in file contents, and prints a live progress display in the terminal as it scans.

## Features

- Recursively scans all files under a specified root directory  
- Counts total files before scanning  
- Detects keyword matches in:
  - **File names**
  - **File contents** (up to the first 250 lines per file)
- Tracks total occurrences of the keyword across all files  
- Shows a live progress graph while scanning  

## Requirements

- Python 3.8 or later
- Windows, macOS, or Linux
- No external dependencies beyond the Python standard library

## Usage

Run the script from a terminal:

```bash
python scan.py --path "C:\path\to\search" --keyword hello
```

Example (Linux/Mac):

```bash
python3 scan.py --path ~/projects --keyword TODO
```

## Command Line Arguments

| Argument       | Description                                  | Required |
|----------------|----------------------------------------------|----------|
| `--path`       | Root directory to scan                       | Yes      |
| `--keyword`    | Keyword (case-insensitive) to search for     | Yes      |

## Output

During the scan you’ll see a live text display that updates with:

- Number of files processed vs total  
- Keyword occurrences so far  
- A simple visual marker showing progress  

At the end, the script prints a summary:

```
<total_files> <matched_file_names> <matched_file_content>
```

## Notes

- The script is **not yet packaged as a Windows `.exe`**, but it is structured so it can be built with PyInstaller when desired.
- Files are read in text mode with ignored decode errors, so binary files are skipped safely.
- Only the first 250 lines of each file are inspected to keep scanning fast.

## Future Enhancements

- Windows `.exe` packaging  
- Optional logging to a file  
- Configurable scan depth and line-limit  
- Colorized terminal output  
