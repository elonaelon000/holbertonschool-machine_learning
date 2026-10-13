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
- `5-slice.py`: selects High, Low, Close, and Volume_(BTC) every 60 rows.
- `5-main.py`: example test using the Coinbase CSV file.
- `6-flip_switch.py`: sorts the index in descending order and transposes.
- `6-main.py`: example test using the Coinbase CSV file.
- `7-high.py`: sorts rows by High price in descending order.
- `7-main.py`: example test using the Coinbase CSV file.
- `8-prune.py`: removes rows with missing Close prices.
- `8-main.py`: example test using the Coinbase CSV file.
- `9-fill.py`: removes Weighted_Price and fills missing prices and volumes.
- `9-main.py`: example test using the Coinbase CSV file.
- `10-index.py`: sets Timestamp as the DataFrame index.
- `10-main.py`: example test using the Coinbase CSV file.
- `11-concat.py`: prepends Bitstamp rows through timestamp 1417411920 to
  Coinbase data, using source labels and a Timestamp index.
- `11-main.py`: example test using the Coinbase and Bitstamp CSV files.
- `12-hierarchy.py`: combines both exchanges from timestamp 1417411980
  through 1417417980, with Timestamp first in the index and rows in time order.
- `12-main.py`: example test using the Coinbase and Bitstamp CSV files.
- `13-analyze.py`: computes descriptive statistics, excluding Timestamp.
- `13-main.py`: example test using the Coinbase CSV file.
- `14-visualize.py`: cleans Coinbase data, prints daily statistics from 2017
  onward, and plots the six price and volume columns.

Run the tests from this directory with NumPy and pandas installed:

```bash
./0-main.py
./1-main.py
```

To run `./2-main.py`, place these datasets in this directory first:

- `coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv`
- `bitstampUSD_1-min_data_2012-01-01_to_2020-04-22.csv`

The datasets are not included in this repository.
Once the Coinbase file is available, the example scripts for tasks 3 through 10
and task 13 can also be run from this directory, for example `./13-main.py`.
Tasks 11 and 12 use both datasets. Run `./11-main.py` or `./12-main.py`.

Task 14 also requires Matplotlib. With the Coinbase CSV available, run
`./14-visualize.py` to print the daily DataFrame and open the plot window.
