import sys
import os
from rich.console import Console
from rich.markdown import Markdown
from rich.syntax import Syntax
from rich.panel import Panel

def read_markdown_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"[bold red]Error:[/bold red] The file '{file_path}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"[bold red]Error:[/bold red] An unexpected error occurred: {e}")
        sys.exit(1)

def render_markdown(content):
    console = Console()
    markdown = Markdown(content)
    console.print(markdown)

def main():
    if len(sys.argv) != 2:
        print("Usage: python md.py <path_to_markdown_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    if not os.path.isfile(file_path):
        print(f"[bold red]Error:[/bold red] '{file_path}' is not a valid file.")
        sys.exit(1)

    content = read_markdown_file(file_path)
    render_markdown(content)

if __name__ == "__main__":
    main()