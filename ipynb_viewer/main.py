import pyfiglet
import sys
import json
import os

def parse_ipynb(filename):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")
        sys.exit(1)

    cells = []
    for cell in data.get('cells', []):
        if cell.get('cell_type') == 'code':
            input_text = cell.get('source', [])
            output = []
            for output_cell in cell.get('outputs', []):
                output.append(''.join(output_cell.get('text', '')))
            cells.append({'input': input_text, 'output': output})
    return cells

def display_cells(cells):
    for cell in cells:
        print("\033[1;36mInput:\033[0m")
        input_text = ''.join(cell['input'])
        print(input_text, "\n")
        print("\033[1;35mOutput:\033[0m")
        if cell['output']:
            output_text = '\n'.join(str(item) for item in cell['output'])
            print(output_text)
        else:
            print("No output generated.")
        print(("-" * 50).center(50))

blue_color = "\033[1;34m"
green_color = "\033[92m"
reset = "\033[0m"

def main():
    if len(sys.argv) != 2:
        print("Usage: ipynb_viewer <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    if not os.path.isfile(filename):
        print(f"Error: The file '{filename}' does not exist.")
        sys.exit(1)

    ascii_banner1 = pyfiglet.figlet_format("IPYNB")
    ascii_banner2 = pyfiglet.figlet_format("Viewer")
    banner = f"{blue_color}{ascii_banner1}{reset}{blue_color}{ascii_banner2}{reset}"
    print(f"{banner}{green_color}[-->] Made With 💕 By @PrinceTheProgrammer....\n{reset}")
    print(("-" * 50).center(50))

    cells = parse_ipynb(filename)
    display_cells(cells)

if __name__ == "__main__":
    main()
