# report.py
#
# Exercise 2.4
import csv


def read_portfolio(file_path):
    """读取某个文件中的投资组合
    :param file_path: 存储投资组合信息的文件路径"""
    try:
        with open(file_path, mode="rt", encoding="utf-8") as f:
            rows = csv.reader(f)
            portfolio = []
            stocks_header = next(rows)
            for rowno, row in enumerate(rows):
                try:
                    _ = dict(zip(stocks_header, row))
                    _["shares"] = int(_["shares"])
                    _["price"] = float(_["price"])
                    portfolio.append(_)
                except ValueError:
                    print(f"Row {rowno}: 错误 row: {row}")
            print(portfolio)
            return portfolio
    except FileNotFoundError as exc:
        raise FileNotFoundError("文件不存在，请您检查提交的文件路径") from exc


def read_prices(file_path):
    """从指定文件中获取股票名称及其对应的价格
    :param file_path: 股票文件的路径"""
    try:
        prices = {}
        with open(file_path, mode="rt", encoding="utf-8") as f:
            rows = csv.reader(f)
            # 因为这个 csv 文件没有头部数据，因此 row 的下标从 1 开始
            for rowno, row in enumerate(rows, start=1):
                try:
                    prices[row[0]] = float(row[1])
                except (ValueError, IndexError):
                    print(f"Row {rowno+1}: Bad row: {row}")

            return prices
    except FileNotFoundError as exc:
        raise FileNotFoundError("文件不存在，请您检查提交的文件路径") from exc


def make_report(portfolio: list[dict], prices: dict) -> tuple:
    """反映投资组合的当前价格变动情况。
    :param portfolio: 投资组合数据，其字段包括 name、shares 和 price
    :param prices: 股票的当前价格，其字段包括 name 和 price"""
    portfolio = portfolio[:]
    for _ in portfolio:
        _["change"] = prices[_["name"]] - _["price"] if _["name"] in prices else 0
        _["now_price"] = prices[_["name"]] if _["name"] in prices else 0
    reports = ((_["name"], _["shares"], _["now_price"], _["change"]) for _ in portfolio)
    return reports


PORTFOLIO_PATH = (
    r"/home/cicero/Documents/Projects/practical-python/Work/Data/portfolio.csv"
)
portfolio_detail = read_portfolio(file_path=PORTFOLIO_PATH)
portfolio_cost = sum(stock["shares"] * stock["price"] for stock in portfolio_detail)
print(f"Total cost: {portfolio_cost:0.2f}")

PRICES_PATH = r"/home/cicero/Documents/Projects/practical-python/Work/Data/prices.csv"
prices_detail = read_prices(file_path=PRICES_PATH)
current_value = sum(
    stock["shares"] * prices_detail[stock["name"]]
    for stock in portfolio_detail
    if stock["name"] in prices_detail
)
print(f"Current value: {current_value:0.2f}")
print(f"Total gain: {current_value - portfolio_cost:0.2f}")

report = make_report(portfolio=portfolio_detail, prices=prices_detail)
header = ["Name", "Shares", "Price", "Change"]
print(f"{header[0]:>10s} {header[1]:>10s} {header[2]:>10s} {header[3]:>10s}")
print(f"{'':->10s} " * len(header))
for name, shares, price, change in report:
    print(f"{name:>10s} {shares:>10d} {'$'+str(round(price, 2)):>10s} {change:>10.2f}")
