# Pandas

DataFrame exercises using Python and pandas.

- `0-from_numpy.py`: creates a DataFrame from a NumPy array, with columns
  named A, B, C, and so on.
- `0-main.py`: example test for task 0.
- `1-from_dictionary.py`: creates a DataFrame from a dictionary, with
  columns First and Second and rows A through D.
- `1-main.py`: example test for task 1.
- `2-from_file.py`: loads a DataFrame from a file using a given separator.
- `2-main.py`: example test using the Coinbase and Bitstamp CSV files.
- `3-rename.py`: converts Timestamp to Datetime and keeps Datetime and Close.
- `3-main.py`: example test using the Coinbase CSV file.
- `4-array.py`: returns the last ten High and Close rows as a NumPy array.
- `4-main.py`: example test using the Coinbase CSV file.

Run the tests from this directory with NumPy and pandas installed:

```bash
./0-main.py
./1-main.py
```

To run `./2-main.py`, place these datasets in this directory first:

- `coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv`
- `bitstampUSD_1-min_data_2012-01-01_to_2020-04-22.csv`

The datasets are not included in this repository.
Once the Coinbase file is available, run `./3-main.py` and `./4-main.py`
for tasks 3 and 4.
