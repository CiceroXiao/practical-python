import report
from tableformat import create_formatter, print_table

portfolio = report.read_portfolio('Data/portfolio.csv')
formatter = create_formatter('txts')

print_table(portfolio, ['name', 'shares', 'price'], formatter)
