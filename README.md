# HandyCLI

HandyCLI is a simple Python-based command-line utility that allows you to execute custom Python scripts from a specific directory using just their names and arguments, making it easier to manage and run your favorite scripts from the command line.

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
   cd HandyCLI
   ```

3. Ensure you have Python installed (Python 3.x is recommended).

4. (Optional) Create a virtual environment to manage dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

## Usage

HandyCLI allows you to execute Python scripts located in the `commands` directory using their names as commands.

### Running a Command

To run a command, use the following syntax:

```bash
python $.py <command> [arguments...]
```

For example, if you have a script called `proxy.py` in the `commands` directory, you can run it like this:

```bash
python $.py proxy
```

To pass arguments to the script, just include them after the command:

```bash
python $.py proxy import
```

### What Happens:

- **No Arguments:** If no arguments are passed, the command will default to executing the script with the `show` argument (or any default argument specified).
- **Invalid Command:** If the specified command doesn't exist in the `commands` directory, it will print an error message:
  ```
  '<command>' is not recognized as an internal or external command, 
  operable program or batch file.~HandyCLI
  ```

### Example

If you want to use the `proxy.py` script:

```bash
python $.py proxy import
```

If `proxy.py` exists and expects arguments, it will run with `import` as an argument. If no arguments are passed, it defaults to `show` (if specified).

## Scripts Overview

HandyCLI supports a collection of Python scripts located in the `commands` directory. Here's an overview of the available scripts:

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
```