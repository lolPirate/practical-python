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
        headers = next(f)
        for line in f:
            record = dict(zip(headers, line))
            portfolio.append(
                {
                    'name': record['name'],
                    'shares': int(record['shares']),
                    'price': float(record['price']),
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


def make_report(portfolio, current_prices):
    """
    Makes a report from the supplied portfolio and current_prices
    """
    report = []
    for i in portfolio:
        name, shares, price = i.values()
        current_price = current_prices[name]
        change = current_price - price
        report.append((name, shares, current_price, change))
    return report


def retire(portfolio, current_prices):
    portfolio_price = 0.0
    current_price = 0.0

    for i in portfolio:
        portfolio_price += i['shares'] * i['price']
        current_price += i['shares'] * current_prices[i['name']]

    print(f'Original Value : {portfolio_price:0.2f}')
    print(f'Current Value : {current_price:0.2f}')
    print(
        f'Gain/Loss : {(current_price - portfolio_price)*100/portfolio_price:0.2f}%')


def print_report():
    portfolio = read_portfolio(r'Work\Data\portfolio.csv')
    current_prices = read_prices(r'Work\Data\prices.csv')

    report = make_report(portfolio, current_prices)

    headers = ('Name', 'Shares', 'Price', 'Change')
    print(
        f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')

    seperators = '-'*10
    print(f'{seperators} {seperators} {seperators} {seperators}')

    for name, shares, current_price, change in report:
        current_price = round(current_price, 2)
        current_price = '$'+str(current_price)
        print(f'{name:>10s} {shares:>10n} {current_price:>10s} {change:>10.2f}')


print_report()
