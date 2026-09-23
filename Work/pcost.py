# pcost.py
# author linghch
# Exercise 1.27

import sys
import csv

def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows) # skip the header row
        for row in rows:
            try: # catch conversion error
                shares = int(row[1])
                price = float(row[2])
            except ValueError:
                print(f"Error: {row}")
            total_cost += shares * price # Add cost of the current holding
    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
