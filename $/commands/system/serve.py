import socketserver
import os
import http.server
import argparse
import logging
from urllib.parse import unquote
import random
import subprocess

def run(port=None, directory=None, react=False):
    if port is None:
        port = random.randint(8000, 9000)
    
    if react:
        subprocess.run(['npm', 'run', 'build'], cwd=directory, check=True)
        directory = os.path.join(directory, 'build')

    os.chdir(directory)
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        logging.info(f"Serving at http://localhost:{port}")
        httpd.serve_forever()

def show_help():
    help_text = """
    Simple HTTP Server - Usage Guide
    ==============================
    
    This server allows you to serve static files or React applications over HTTP.
    
    Basic Usage:
        python serve.py [options]
    
    Options:
        -h, --help          Show this help message
        -p, --port PORT     Specify port number (default: random port)
        -d, --directory DIR Specify directory to serve (default: current directory)
        -r, --react         Build and serve a React application
    
    Examples:
        1. Serve current directory on random port:
           python serve.py
        
        2. Serve specific directory on port 8000:
           python serve.py -p 8000 -d /path/to/directory
        
        3. Build and serve a React application:
           python serve.py -r -d /path/to/react/app
    """
    print(help_text)
    exit(0)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Simple HTTP Server")
    parser.add_argument('-p', '--port', type=int, help='Port to serve on (default: random port)')
    parser.add_argument('-d', '--directory', type=str, default=os.getcwd(), help='Directory to serve (default: current working directory)')
    parser.add_argument('-r', '--react', action='store_true', help='Serve a React.js application (default: False)')
    parser.add_argument('--help-menu', action='store_true', help='Show detailed help menu')
    args = parser.parse_args()

    if args.help_menu:
        show_help()

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    run(port=args.port, directory=args.directory, react=args.react)