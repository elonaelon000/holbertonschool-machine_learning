# Matplotlib

Plotting exercises for the Holberton machine learning programme.
This project covers drawing charts from numerical data and formatting
their axes, labels, titles, and legends.

## Requirements

The project environment specified by Holberton is:

- Ubuntu 20.04 LTS and Python 3.9
- NumPy 1.25.2
- Matplotlib 3.8.3
- pycodestyle 2.11.1

Install the Python packages in your working environment:

```bash
python3 -m pip install --user numpy==1.25.2 matplotlib==3.8.3 \
    Pillow==10.3.0 pycodestyle==2.11.1
```

On Ubuntu, the Tk plotting backend can be installed with:

```bash
sudo apt-get install python3-tk
```

## Tasks

- `0-line.py`: plots the cubes of numbers from 0 through 10 as a solid red
  line, with the x-axis limited to that range.
- `0-main.py`: calls the `line()` function to display the graph.
- `1-scatter.py`: plots men's heights and weights as magenta points, with
  axis labels and a title.
- `1-main.py`: calls the `scatter()` function to display the graph.
- `2-change_scale.py`: plots carbon-14 decay with a logarithmic y-axis
  and time ranging from 0 to 28,650 years.
- `2-main.py`: calls the `change_scale()` function to display the graph.
- `3-two.py`: compares carbon-14 and radium-226 decay using two line styles
  and a legend.
- `3-main.py`: calls the `two()` function to display the graph.
- `4-frequency.py`: groups student grades into ten-point bins from 0 to 100,
  with black bar outlines.
- `4-main.py`: calls the `frequency()` function to display the histogram.
- `5-all_in_one.py`: combines the five previous graphs in a 3-by-2 grid,
  with the histogram spanning the bottom row.
- `5-main.py`: calls the `all_in_one()` function to display the figure.
- `6-bars.py`: stacks four kinds of fruit for Farrah, Fred, and Felicia,
  with a different color for each fruit.
- `6-main.py`: calls the `bars()` function to display the chart.

## Running a task

From the repository root:

```bash
cd math/plotting
./0-main.py
./1-main.py
./2-main.py
./3-main.py
./4-main.py
./5-main.py
./6-main.py
```

Plot windows need a graphical environment. Check the code style with:

```bash
pycodestyle *.py
```

## File conventions

Python files start with `#!/usr/bin/env python3`, have module and function
docstrings, end with a newline, and are executable. Each task uses the imports
allowed in its instructions and follows pycodestyle.
