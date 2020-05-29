# pcost.py
#
# Exercise 1.27

file = r'Work\Data\portfolio.csv'

total_cost = 0.0

with open(file, 'rt') as f:
    next(f)
    for line in f:
        name, shares, price = line.strip().split(',')
        total_cost = total_cost + int(shares) * float(price)

print(f'Total cost {total_cost:0.2f}')
