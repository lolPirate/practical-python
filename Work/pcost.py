# pcost.py
#
# Exercise 1.27
import sys
import csv

def portfolio_cost(file_name):
    """
    Returns the total cost to buy all shares.
    """
    total_cost = 0.0
    with open(file_name, 'rt') as f:
        f = csv.reader(f)
        headers = next(f)
        for indx, line in enumerate(f, start=1):
            record = dict(zip(headers, line))
            try:
                shares = int(record['shares'])
                price = float(record['price'])
                total_cost = total_cost + shares * price
            except ValueError:
                print(f'Row {indx}: Bad Row: {line}')
    return total_cost


if len(sys.argv) == 2:
    file = sys.argv[1]
else:
    file = r'Work\Data\portfolio.csv'

total_cost = portfolio_cost(file)
print(f'Total cost {total_cost:0.2f}')
