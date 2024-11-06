# Custom Command Directory

This repository contains a collection of Python scripts that provide various command-line functionalities, mimicking Unix-like commands and adding new utilities for convenience. Each script serves a specific purpose and can be used individually.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Scripts Overview](#scripts-overview)
- [Dependencies](#dependencies)
- [License](#license)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/nadeeshafdo/HandyCLI.git
   ```
   
2. Navigate into the directory:
   ```bash
   cd your-repo-name
   ```

3. Ensure you have Python installed (Python 3.x is recommended).

4. (Optional) Create a virtual environment to manage dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

## Usage

Each script can be run from the command line. To see how to use a specific script, you can run it without arguments, and it will display the usage instructions. For example:

```bash
python touch.py <filename>
```

Replace `<filename>` with the name of the file you want to create or update.

## Scripts Overview

Here’s a brief overview of the available scripts:

- **cat.py**: Display the content of files.
- **edit-path.py**: Modify the system's PATH variable.
- **ip.py**: Display your current IP address.
- **ls.py**: List files in a directory (similar to Unix `ls`).
- **open.py**: Open files or directories using the default application.
- **power.py**: Power-related commands (shutdown, restart).
- **proxy.py**: Set proxy configurations for your system.
- **pwc.py**: Print working directory.
- **rm-all.py**: Remove all files in a specified directory.
- **sudo.py**: Execute commands with elevated privileges.
- **temp-clean.py**: Clean up temporary files.
- **touch.py**: Create an empty file or update the timestamp of an existing file.
- **find.py**: Search for files or directories based on a pattern.
- **zipdir.py**: Compress a directory into a ZIP file.
- **serve.py**: Start a simple HTTP server.
- **mv.py**: Move or rename files and directories.
- **diff.py**: Compare two files and show differences.
- **watch.py**: Monitor a file or directory for changes.
- **backup.py**: Create a backup of a file or directory.
- **size.py**: Display the size of a file or directory.
- **alias.py**: Create shortcuts for commands.
- **sysinfo.py**: Display system information.
- **convert.py**: Convert files between formats (e.g., images).
- **grep.py**: Search for text patterns in files.
- **monitor.py**: Monitor system performance metrics (CPU, Memory, Disk).
- **scrape.py**: Basic web scraping utility.
- **uuidgen.py**: Generate a unique UUID.

## Dependencies

Some scripts require additional Python libraries. You can install the required libraries using pip:

```bash
pip install psutil requests beautifulsoup4 pillow
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
