# report.py
#
# Exercise 2.4
import csv
from pprint import pprint

def read_portfolio(file_name):
    """
    Opens portfolio file, reads it and returns a list.
    """
    portfolio = []
    with open(file_name, 'rt') as f:
        f = csv.reader(f)
        next(f)
        for line in f:
            name, shares, price = line
            portfolio.append(
                {
                    'name': name,
                    'shares': int(shares),
                    'price': float(price),
                }
            )
    return portfolio

def read_prices(file_name):
    """
    Reads prices from a csv file and returns a dictionary
    """
    prices = {}
    with open(file_name, 'rt') as f:
        f = csv.reader(f)
        for line in f:
            if line:
                prices[line[0]] = float(line[1])
    return prices

portfolio = read_portfolio(r'Work\Data\portfolio.csv')
current_prices = read_prices(r'Work\Data\prices.csv')

portfolio_price = 0.0
current_price = 0.0

for i in portfolio:
    portfolio_price += i['shares'] * i['price']
    current_price += i['shares'] * current_prices[i['name']]

print(f'Original Value : {portfolio_price:0.2f}')
print(f'Current Value : {current_price:0.2f}')
print(f'Gain/Loss : {(current_price - portfolio_price)*100/portfolio_price:0.2f}%')