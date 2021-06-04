# Simple Qt Calculator
A simple Qt calculator made with Python and PySide2 bindings. 

All dependencies and basic project information can be found in `pyproject.toml`.

## Image preview
![Image of the app window]()

## Gif
![Gif of the app working]()

## How to use

- Clone the repository or download the zip file;
- Extract the content;
- Check if PySide2 is available on your system;
- Run the `main.py` file.

### Some considerations

This project is made from two different projects that I created at different times. `main.py` contains the graphical part of the program and formerly contained simple calculation logic which I ended up replacing with a robust logic. The new logic is contained in `calculator.py`. `main.py` and `calculator.py` can be used separately.