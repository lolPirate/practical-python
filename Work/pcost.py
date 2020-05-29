# pcost.py
#
# Exercise 1.27
import sys

def portfolio_cost(file_name):
    """
    Returns the total cost to buy all shares.
    """
    total_cost = 0.0
    with open(file_name, 'rt') as f:
        next(f)
        for line in f:
            _, shares, price = line.strip().split(',')
            total_cost = total_cost + int(shares) * float(price)
    return total_cost


if len(sys.argv) == 2:
    file = sys.argv[1]
else:
    file = r'Work\Data\portfolio.csv'

total_cost = portfolio_cost(file)
print(f'Total cost {total_cost:0.2f}')

