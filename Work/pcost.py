# pcost.py
# author linghch
# Exercise 1.27

total_cost = 0.0

with open('Data/portfolio.csv') as f:
    next(f) # skip the header
    for line in f:
        stock = line.strip().split(',') 
        shares = int(stock[1])
        price = float(stock[2])
        total_cost += shares * price # Accumulate cost of each company's shares

print(f'Total cost {round(total_cost, ndigits=2)}')