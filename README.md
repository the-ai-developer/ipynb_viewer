# IPYNB Viewer

IPYNB Viewer is a command-line tool designed to display the contents of Jupyter Notebook files (`.ipynb`) directly in your terminal. This tool extracts code cells and their outputs, providing a convenient way to review notebook contents without needing a Jupyter environment.

## Features

- Parses Jupyter Notebook files.
- Displays code cells and their outputs.
- Colorful and formatted terminal output.

## Installation

### Prerequisites

Ensure you have Python 3.6 or above installed.

### Using apt (Recommended for Linux/Termux)

1. Install `ipynb_viewer`:
    ```sh
    sudo apt-get install ipynb-viewer
    ```

### Manual Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/the-ai-developer/ipynb_viewer.git
    cd ipynb_viewer
    ```

2. Install the package using pip:
    ```sh
    pip install .
    ```

## Usage

Once installed, you can use the `ipynb_viewer` command followed by the path to a Jupyter Notebook file to display its contents.

```sh
ipynb_viewer /path/to/notebook.ipynb
```
## Example
```sh
ipynb_viewer example_notebook.ipynb
```
This command will display the input and output cells from the example_notebook.ipynb file in the terminal.

## Development
### Setting Up the Development Environment
1. Clone the repository:

```sh
git clone https://github.com/the-ai-developer/ipynb_viewer.git
cd ipynb_viewer
```
2. Install dependencies:

```sh
pip install -r requirements.txt
```

3. Run the tool locally:

```sh
python -m ipynb_viewer.main /path/to/notebook.ipynb
```

## Building the Debian Package
1. Install necessary tools:

```sh
sudo apt-get install dh-make devscripts build-essential lintian
```
2. Create Debian package files:

```sh
cd ipynb_viewer
dh_make --createorig -p ipynb-viewer_1.0
```
3. Edit the debian/control file to specify dependencies and metadata.

4. Build the package:

```sh
dpkg-buildpackage -us -uc
```
## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
Made with 💕 by PrinceTheProgrammer . . .