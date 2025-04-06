import os
import time
import threading
from queue import Queue, Empty
from typing import List, Dict, Set
from pathlib import Path
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskID
from rich.tree import Tree
from rich import print as rprint
from rich.panel import Panel
from rich.prompt import Prompt
from rich.syntax import Syntax

# Default ignore patterns
DEFAULT_IGNORE_PATTERNS = {
    'directories': {
        '.git', 'node_modules', '__pycache__', 'venv', 'env', 
        'build', 'dist', '.idea', '.vscode', 'coverage'
    },
    'files': {
        '*.pyc', '*.pyo', '*.pyd', '*.so', '*.dll', '*.dylib',
        '*.egg-info', '*.egg', '*.whl', '*.DS_Store', 'Thumbs.db',
        '*.log', '*.pot', '*.class', '*.jar', '*.war'
    }
}

console = Console()

class ProjectMapper:
    def __init__(self):
        self.file_queue = Queue()
        self.content_map = {}
        self.ignore_patterns = DEFAULT_IGNORE_PATTERNS
        self.lock = threading.Lock()

    def should_ignore(self, path: Path) -> bool:
        """Check if a path should be ignored based on patterns."""
        if path.name in self.ignore_patterns['directories'] and path.is_dir():
            return True
        
        for pattern in self.ignore_patterns['files']:
            if path.match(pattern):
                return True
        
        return False

    def scan_directory(self, directory: Path, progress: Progress, task: TaskID):
        """Scan directory and add files to queue."""
        try:
            total_items = sum(1 for _ in directory.rglob('*'))
            progress.update(task, total=total_items)
            
            for item in directory.rglob('*'):
                if not self.should_ignore(item):
                    if item.is_file():
                        self.file_queue.put(item)
                    progress.advance(task)
                    
        except Exception as e:
            console.print(f"[red]Error scanning directory: {e}[/red]")

    def process_file(self, progress: Progress, task: TaskID):
        """Process files from the queue."""
        while True:
            try:
                try:
                    file_path = self.file_queue.get_nowait()
                except Empty:
                    break

                try:
                    content = file_path.read_text(encoding='utf-8')
                    with self.lock:
                        self.content_map[file_path] = content
                except Exception as e:
                    console.print(f"[yellow]Warning: Could not read {file_path}: {e}[/yellow]")
                
                progress.advance(task)
                self.file_queue.task_done()
            except Exception as e:
                console.print(f"[red]Error processing file: {e}[/red]")
                break

    def generate_tree_text(self, directory: Path, prefix="") -> List[str]:
        """Generate a text representation of the directory tree."""
        tree_lines = []
        items = sorted(list(directory.iterdir()))
        
        for i, item in enumerate(items):
            if self.should_ignore(item):
                continue
                
            is_last = i == len(items) - 1
            current_prefix = prefix + ("└── " if is_last else "├── ")
            next_prefix = prefix + ("    " if is_last else "│   ")
            
            if item.is_dir():
                tree_lines.append(f"{current_prefix}📁 {item.name}")
                tree_lines.extend(self.generate_tree_text(item, next_prefix))
            else:
                tree_lines.append(f"{current_prefix}📄 {item.name}")
                
        return tree_lines

    def generate_markdown(self, directory: Path) -> str:
        """Generate markdown content from the mapped files."""
        markdown = ["# Project Documentation\n\n## Directory Structure\n\n"]
        
        # Add tree structure
        tree_text = self.generate_tree_text(directory)
        markdown.append("```\n")
        markdown.extend(tree_text)
        markdown.append("\n```\n\n## File Contents\n\n")
        
        # Add file contents
        for file_path, content in sorted(self.content_map.items()):
            rel_path = file_path.relative_to(directory)
            extension = file_path.suffix.lstrip('.')
            markdown.extend([
                f"### {rel_path}\n\n",
                f"```{extension}\n{content}\n```\n\n"
            ])
            
        return '\n'.join(markdown)

    def map_project(self, directory_path: str, num_threads: int = 4):
        """Main method to map the project."""
        try:
            directory = Path(directory_path).resolve()
            
            if not directory.exists():
                console.print("[red]Error: Directory does not exist![/red]")
                return
                
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            ) as progress:
                # Scan directory
                scan_task = progress.add_task("[cyan]Scanning directory...", total=None)
                self.scan_directory(directory, progress, scan_task)
                
                # Process files
                total_files = self.file_queue.qsize()
                if total_files == 0:
                    console.print("[yellow]No files found to process.[/yellow]")
                    return

                process_task = progress.add_task("[green]Processing files...", total=total_files)
                
                threads = []
                for _ in range(min(num_threads, total_files)):
                    thread = threading.Thread(
                        target=self.process_file,
                        args=(progress, process_task)
                    )
                    thread.daemon = True  # Make threads daemon so they exit when main thread exits
                    thread.start()
                    threads.append(thread)
                    
                # Wait for all files to be processed
                self.file_queue.join()
                
                # Generate documentation
                doc_task = progress.add_task("[yellow]Generating documentation...", total=None)
                markdown_content = self.generate_markdown(directory)
                
                # Save to file
                output_file = directory / 'README.md'
                output_file.write_text(markdown_content, encoding='utf-8')
                progress.update(doc_task, completed=True)
                
                console.print(
                    Panel.fit(
                        f"[bold green]Documentation generated successfully![/bold green]\n"
                        f"[blue]Output file:[/blue] {output_file}",
                        title="Success",
                        border_style="green"
                    )
                )
        except Exception as e:
            console.print(f"[red]Error: {str(e)}[/red]")

def main():
    console.print(
        Panel.fit(
            "[bold blue]Project Mapper[/bold blue]\n"
            "Maps your project structure and generates comprehensive documentation",
            title="Welcome",
            border_style="blue"
        )
    )
    
    directory = Prompt.ask(
        "\n[cyan]Enter the project directory path[/cyan]",
        default=str(Path.cwd())
    )
    
    threads = Prompt.ask(
        "[cyan]Enter the number of processing threads[/cyan]",
        default="4"
    )
    
    mapper = ProjectMapper()
    mapper.map_project(directory, int(threads))

if __name__ == "__main__":
    main()