# report.py
#
# Exercise 2.4
import fileparse


def read_portfolio(file_path: str) -> list:
    """读取某个文件中的投资组合
    :param file_path: 存储投资组合信息的文件路径
    :return portfolio: list ，股票投资组合信息"""

    with open(file_path, mode="rt", encoding="utf-8") as lines:
        portfolio = fileparse.parse_csv(
            lines,
            select=["name", "shares", "price"],
            types=[str, int, float],
            has_headers=True,
        )
        return portfolio


def read_prices(file_path: str) -> dict:
    """从指定文件中获取股票名称及其对应的价格
    :param file_path: 股票文件的路径"""
    with open(file_path, mode="rt", encoding="utf-8") as lines:
        prices = dict(fileparse.parse_csv(lines=lines, types=[str, float]))
        return prices


def make_report(portfolio: list[dict], prices: dict) -> tuple:
    """获取投资组合的当前价格变动数据。
    :param portfolio: 投资组合数据，其字段包括 name、shares 和 price
    :param prices: 股票的当前价格，其字段包括 name 和 price"""
    portfolio = portfolio[:]
    for _ in portfolio:
        _["change"] = prices[_["name"]] - _["price"] if _["name"] in prices else 0
        _["now_price"] = prices[_["name"]] if _["name"] in prices else 0
    reports = ((_["name"], _["shares"], _["now_price"], _["change"]) for _ in portfolio)
    return reports


def print_report(report_data):
    """打印美观的表格数据，其字段包括 Name、Shares、Price 和 Change"""

    header = ["Name", "Shares", "Price", "Change"]
    print(f"{header[0]:>10s} {header[1]:>10s} {header[2]:>10s} {header[3]:>10s}")
    print(f"{'':->10s} " * len(header))
    for name, shares, price, change in report_data:
        print(
            f"{name:>10s} {shares:>10d} {'$'+str(round(price, 2)):>10s} {change:>10.2f}"
        )


def portfolio_filename(portfolio_file: str, prices_file: str):
    """反映已购的股票组合之价格波动
    :param portfolio_file: 包含已购买的股票组合之花费的文件
    :param prices_file: 包含当前股票价格的文件"""
    portfolio_detail = read_portfolio(file_path=portfolio_file)
    portfolio_cost = sum(stock["shares"] * stock["price"] for stock in portfolio_detail)
    print(f"Total cost: {portfolio_cost:0.2f}")

    prices_detail = read_prices(file_path=prices_file)
    current_value = sum(
        stock["shares"] * prices_detail[stock["name"]]
        for stock in portfolio_detail
        if stock["name"] in prices_detail
    )
    print(f"Current value: {current_value:0.2f}")
    print(f"Total gain: {current_value - portfolio_cost:0.2f}")

    report = make_report(portfolio=portfolio_detail, prices=prices_detail)
    print_report(report_data=report)


def main(args):
    """执行此脚本"""
    if len(args) != 3:
        raise SystemExit(f"Usage: {args[0]} " "portfile pricefile")
    portfolio_filename(portfolio_file=args[1], prices_file=args[2])


if __name__ == "__main__":
    import sys

    main(sys.argv)
