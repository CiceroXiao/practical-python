from follow import follow
import report
from ticker import filter_symbols, parse_stock_data

portfolio = report.read_portfolio("Data/portfolio.csv")
rows = parse_stock_data(follow("Data/stocklog.csv"))
rows = filter_symbols(rows=rows, names=portfolio)

for row in rows:
    print(row)
