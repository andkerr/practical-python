# pcost.py
#
# Exercise 1.27

import csv
import sys

def row_cost(columns):
    shares, price = columns[1:3]
    try:
        return int(shares) * float(price)
    except ValueError:
        print(f"warning: row with invalid shares or price column {columns}")
        return 0.00

def portfolio_cost(filename):
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        return sum(row_cost(row) for row in rows)

filename = sys.argv[1] if len(sys.argv) == 2 else "Data/portfolio.csv"
tcost = portfolio_cost(filename)
print(f"Total cost {tcost:.2f}")
