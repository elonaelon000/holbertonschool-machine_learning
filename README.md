# Holberton School Machine Learning

This is where I keep my projects and exercises from the Holberton School
Machine Learning programme. I add to it as we cover new topics in class,
starting with Python, maths, and working with data.

## The programme

The programme is split into three trimesters. The first builds the foundations
for understanding data, and the next two move into machine learning and
building applications with AI.

| Trimester | Focus |
| --- | --- |
| Data Analyst | Working with datasets, analysing results, and presenting findings |
| Machine Learning Engineer | Building, training, and evaluating models |
| AI Engineer | Developing applications that use those models |

## Finding a project

Projects are grouped by topic. Each project has its own folder and a README
explaining the exercises and how to run them.

| Folder | What it covers |
| --- | --- |
| [math/linear_algebra](math/linear_algebra/) | Vectors, matrices, and NumPy operations |
| [math/plotting](math/plotting/) | Charts and data visualisation with Matplotlib |
| [pipeline/pandas](pipeline/pandas/) | Loading, selecting, and transforming data with pandas |

Task files use the names given in the project brief, such as
`0-from_numpy.py`. Files named `0-main.py`, `1-main.py`, and so on contain
the example tests for their corresponding tasks. More project folders will
be added as the programme continues.

## Environment

The course environment is Ubuntu 22.04 LTS with Python 3.10.
The projects here use NumPy, pandas, and Matplotlib, with `pycodestyle`
for checking code style.

## Code conventions

For completed task solutions, the course requires:

- `#!/usr/bin/env python3` on the first line.
- A docstring for each module, function, and class.
- Formatting that passes `pycodestyle`.
- Executable permissions and a newline at the end of the file.

## Running a task

Open the project folder and run its example test. For example:

```bash
cd pipeline/pandas
python3 0-main.py
```

You can check the solution's style separately:

```bash
pycodestyle 0-from_numpy.py
```

Some exercises need dataset files before their examples can run.
The project README lists those files and any other setup needed.
