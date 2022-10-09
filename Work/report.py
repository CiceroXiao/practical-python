# report.py
#
# Exercise 2.4
import csv
import sys

if len(sys.argv) == 2:
    PORTFOLIO_PATH = sys.argv[1]
else:
    PORTFOLIO_PATH = (
        r"/home/cicero/Documents/Projects/practical-python/Work/Data/portfolio.csv"
    )


def portfolio_cost(file_path) -> float | int:
    """计算购买各公司股票的花费总额（ price * shares ）
    :param file_path: 存储购买信息的文件路径"""
    try:
        with open(file_path, mode="rt", encoding="utf-8") as f:
            rows = csv.reader(f)
            stocks_header = next(rows)
            stocks_info = [
                {
                    stocks_header[0]: row[0],
                    stocks_header[1]: int(row[1]),
                    stocks_header[2]: float(row[2]),
                }
                for row in rows
            ]

            total_cost = sum(stock["price"] * stock["shares"] for stock in stocks_info)
            return total_cost
    except FileNotFoundError as exc:
        raise FileNotFoundError("您提交的文件路径有误，请检查您提交的文件路径") from exc
    except ValueError as exc:
        raise ValueError("您提供的文件内容有误，请检查您的文件内容") from exc


print(f"Total cost: {portfolio_cost(PORTFOLIO_PATH):0.2f}")
