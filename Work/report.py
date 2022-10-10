# report.py
#
# Exercise 2.4
import csv


def read_portfolio(file_path):
    """读取某个文件中的投资组合
    :param file_path: 存储购买信息的文件路径"""
    try:
        with open(file_path, mode="rt", encoding="utf-8") as f:
            rows = csv.reader(f)
            try:
                stocks_header = next(rows)
                portfolio = [
                    {
                        stocks_header[0]: row[0],
                        stocks_header[1]: int(row[1]),
                        stocks_header[2]: float(row[2]),
                    }
                    for row in rows
                ]
            except ValueError as exc:
                raise ValueError("文件内容有误，请您检查所提交文件的内容") from exc

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
            try:
                for row in rows:
                    prices[row[0]] = float(row[1])
            except ValueError as exc:
                raise ValueError("文件内容有误，请您检查所提交文件的内容") from exc
            except IndexError:
                pass

            return prices
    except FileNotFoundError as exc:
        raise FileNotFoundError("文件不存在，请您检查提交的文件路径") from exc


PORTFOLIO_PATH = (
    r"/home/cicero/Documents/Projects/practical-python/Work/Data/portfolio.csv"
)
portfolio_detail = read_portfolio(file_path=PORTFOLIO_PATH)
portfolio_cost = sum(stock["shares"] * stock["price"] for stock in portfolio_detail)
print(f"Total cost: {portfolio_cost:0.2f}")

PRICES_PATH = r"/home/cicero/Documents/Projects/practical-python/Work/Data/prices.csv"
prices_detail = read_prices(file_path=PRICES_PATH)
current_value = sum(
    stock["shares"] * prices_detail[stock["name"]] for stock in portfolio_detail
)
print(f"Current value: {current_value:0.2f}")
print(f"Total gain: {current_value - portfolio_cost:0.2f}")
