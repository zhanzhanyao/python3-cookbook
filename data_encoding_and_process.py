"""Use Python to process data encoded in a variety of ways"""
# read csv
import csv

with open("stocks.csv") as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    # print(headers)
    for row in f_csv:
        pass

# named tuple
from collections import namedtuple

with open("stocks.csv") as f:
    f_csv = csv.reader(f)
    headings = next(f_csv)
    Row = namedtuple("Row", headings)
    for r in f_csv:
        row = Row(*r)
        # print(row.Price)

# read csv to dict
import csv

with open("stocks.csv") as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        print(row)

# write to csv
headers = ["Symbol", "Price", "Date", "Time", "Change", "Volume"]
rows = [
    ("AA", 39.48, "6/11/2007", "9:36am", -0.18, 181800),
    ("AIG", 71.38, "6/11/2007", "9:36am", -0.15, 195500),
    ("AXP", 62.58, "6/11/2007", "9:36am", -0.46, 935000),
]

with open("stock.csv", "w") as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)

# write dict to csv
headers = ["Symbol", "Price", "Date", "Time", "Change", "Volume"]
rows = [
    {
        "Symbol": "AA",
        "Price": 39.48,
        "Date": "6/11/2007",
        "Time": "9:36am",
        "Change": -0.18,
        "Volume": 181800,
    },
    {
        "Symbol": "AIG",
        "Price": 71.38,
        "Date": "6/11/2007",
        "Time": "9:36am",
        "Change": -0.15,
        "Volume": 195500,
    },
    {
        "Symbol": "AXP",
        "Price": 62.58,
        "Date": "6/11/2007",
        "Time": "9:36am",
        "Change": -0.46,
        "Volume": 935000,
    },
]

with open("stocks.csv", "w") as f:
    f_csv = csv.DictWriter(f)
    f_csv.writeheader()
    f_csv.writerows(rows)
