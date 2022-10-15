# report.py
#
# Exercise 2.4
import copy

import fileparse
import stock
import tableformat
from portfolio import Portfolio


def read_portfolio(file_path: str, **opts) -> list:
    """读取某个文件中的投资组合数据，其字段包括 name、shares 和 price
    :param file_path: 存储投资组合信息的文件路径
    :return portfolio: list ，股票投资组合信息"""

    with open(file_path, mode="rt", encoding="utf-8") as lines:
        portfolio = fileparse.parse_csv(
            lines, select=["name", "shares", "price"], types=[str, int, float], **opts
        )
        portfolios = [stock.Stock(**d) for d in portfolio]
        return Portfolio(portfolios)


def read_prices(file_path: str, **opts) -> dict:
    """从指定文件中获取股票名称及其对应的价格
    :param file_path: 股票文件的路径"""
    with open(file_path, mode="rt", encoding="utf-8") as lines:
        prices = dict(
            fileparse.parse_csv(lines, types=[str, float], has_headers=False, **opts)
        )
    return prices


def make_report(portfolio: list[dict], prices: dict) -> list:
    """获取投资组合的当前价格变动数据。
    :param portfolio: 投资组合数据，其字段包括 name、shares 和 price
    :param prices: 股票的当前价格，其字段包括 name 和 price"""
    portfolio = copy.copy(portfolio)
    reports = []
    for _ in portfolio:
        change = prices[_.name] - _.price if _.name in prices else 0
        current_price = prices[_.name] if _.name in prices else 0

        reports.append([_.name, _.shares, current_price, change])
    return reports


def print_report(report_data, formatter):
    """打印美观的表格数据，其字段包括 Name、Shares、Price 和 Change
    :param report_data: 想要打印的数据
    :param formatter:"""

    formatter.headings(["Name", "Shares", "Price", "Change"])

    for name, shares, price, change in report_data:
        rowdata = [name, str(shares), f"{price:0.2f}", f"{change:0.2f}"]
        formatter.row(rowdata)


def portfolio_report(portfolio_file: str, prices_file: str, fmt="txt"):
    """反映已购的股票组合之价格波动
    :param portfolio_file: 包含已购买的股票组合之花费的文件
    :param prices_file: 包含当前股票价格的文件
    :param fmt: 传入的文件格式"""
    portfolio_detail = read_portfolio(file_path=portfolio_file)
    prices_detail = read_prices(file_path=prices_file)

    report = make_report(portfolio=portfolio_detail, prices=prices_detail)

    formatter = tableformat.create_formatter(fmt)
    print_report(report_data=report, formatter=formatter)


def main(args):
    """执行此脚本"""
    if len(args) != 4:
        raise SystemExit(f"Usage: {args[0]} " "portfile pricefile fmt")
    portfolio_report(portfolio_file=args[1], prices_file=args[2], fmt=args[3])


if __name__ == "__main__":
    import sys

    main(sys.argv)
