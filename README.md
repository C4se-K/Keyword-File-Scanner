# Keyword File Scanner

A command-line Python tool for scanning directories, counting files, and detecting keyword occurrences both in file names and in file contents.
As it processes files, it also displays a simple real-time progress graph in the terminal.

Features

Recursively walks a directory

Counts total files

Detects keyword matches in:

file names

file contents (first 250 lines)

Tracks total keyword occurrences over time

Displays a live, text-based progress graph while scanning

Prints summary statistics at the end

Requirements

Python 3.8 or later

Windows, macOS, or Linux terminal

No external packages are required.

Installation

Clone the repository:

git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>


(Optional) Create a virtual environment:

python -m venv venv
venv\Scripts\activate    # Windows
# or
source venv/bin/activate # macOS/Linux

Usage

Run the script directly with Python:

python scan.py --path "C:\your\directory" --keyword hello


Example:

```bash python scan.py --path "C:\dev" --keyword error```

Arguments
Flag	Description	Example
--path	Root directory to scan	--path "C:\dev"
--keyword	Keyword to search for	--keyword test

The tool automatically counts files, scans them, displays real-time progress, and prints a summary after completion.

### Output Example

During scanning, you’ll see a live progress graph:
#todo
L_______________________________________
0         1000         2000         4000
files scanned: 1438 / 5820

keyword: test occurrences so far: 57


And at the end:

5820  48  19


Where the three numbers are:

Total files scanned

Files with keyword in their name

Files with keyword in their content

## Planned Enhancements

Build a standalone Windows .exe using PyInstaller

Add configuration flags (e.g., max content lines, file type filters)

Add optional JSON or CSV output

Improve graph scaling and readability
