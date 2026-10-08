# report.py
# author linghch
# Exercise 2.4

import csv

def read_portfolio(filename):
    '''
    Read a stock holdings file (initial purchase price) and return a list of dicts

    Each dict has keys: 'name' (str), 'shares' (int), 'price' (float)
    '''
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows) # skip the header row
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                portfolio.append({
                    'name': record['name'],
                    'shares': int(record['shares']),
                    'price': float(record['price']),
                })
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
    return portfolio


def read_prices(filename):
    '''
    Read a file of current share prices and return a price dict
    mapping 'name' (str), 'price' (float)
    '''
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if len(row) < 2:
                continue
            prices[row[0]] = float(row[1])
    return prices


def make_report(portfolio, prices):
    '''
    Take a list of stocks and dictionary prices as input,
    and return a list of tuples containing name, shares, price, and change.
    Change is the price variation of the share
    '''
    report = [] # for return tuples
    change = 0.0
    for holding in portfolio:
        if holding['name'] in prices:
            change = prices[holding['name']] - holding['price']
        report.append((holding['name'], holding['shares'], prices[holding['name']], round(change,ndigits=2)))
    return report


# Compute current value of portfolio gain
gain = 0.0

# Get initial stock holdings
portfolio = read_portfolio('Data/portfoliodate.csv')

# Get current share prices
prices = read_prices('Data/prices.csv')

# Make a report about the portfolio
report = make_report(portfolio, prices)

# Format header
headers = ('Name', 'Shares', 'Price', 'Change')
print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
print(("-" * 10 + " ") * len(headers))


# Format print report
for name, shares, price, change in report:
    price = '$' + str(price)
    print(f'{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}')


# Accumulate gain or loss of each stock holding
for holding in portfolio:
    if holding['name'] not in prices:
        continue
    gain += holding['shares'] * (prices[holding['name']]- holding['price'])

# Tell user if he/she can retire on current gain
if gain > 0.0:
    print(f'Your gain is {gain:.2f}')
else:
    print(f'Your loss is {-gain:.2f}')
