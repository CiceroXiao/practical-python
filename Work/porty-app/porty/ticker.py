# ticker.py

import csv

from porty.follow import follow
from porty.pcost import main


def select_columns(rows, indices):
    """根据下标来选择股票数据中的指定字段

    Args:
        rows (list): 股票数据
        indices (list): 想要的数据字段之下标

    Yields:
        list: 用户想要的数据
    """
    for row in rows:
        yield [row[index] for index in indices]


def convert_types(rows, types):
    """将股票数据中的指定字段之数据类型转换为指定指定数据类型

    Args:
        rows (list): 股票数据
        types (list): 包含指定数据类型的列表

    Yields:
        list: 转换数据类型后的数据
    """
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]


def make_dicts(rows, headers):
    """以字典格式返回股票数据

    Args:
        rows (list): 股票数据
        headers (list): 股票数据中各个数据段的字头

    Yields:
        dict: 以 {header: row} 的形式返回数据
    """
    return (dict(zip(headers, row)) for row in rows)


def filter_symbols(rows, names):
    """根据字段名字来选择股票数据中的指定字段

    Args:
        rows (list): 股票数据
        names (list): 包含字段名字的列表

    Yields:
        list: 以列表形式返回指定数据
    """
    for row in rows:
        if row["name"] in names:
            yield row


def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, indices=[0, 1, 4])
    rows = convert_types(rows=rows, types=[str, float, float])
    rows = make_dicts(rows=rows, headers=["name", "price", "change"])
    return rows


def ticker(portfile, logfile, fmt):
    """以特定格式展现已购买的股票组合的实时数据

    Args:
        portfile (str): 已购买的股票组合数据文件
        logfile (str): 股票实时数据文件
        fmt (str): 展现数据的格式
    """
    from porty import report, tableformat

    portfolio = report.read_portfolio(portfile)
    rows = parse_stock_data(follow(logfile))
    # rows = filter_symbols(rows=rows, names=portfolio)
    rows = (row for row in rows if row["name"] in portfolio)
    formatter = tableformat.create_formatter(fmt=fmt)
    formatter.headings(["name", "price", "change"])
    for row in rows:
        formatter.row(
            rowdata=[row["name"], f"{row['price']:>10.2f}", f"{row['change']:>10.2f}"]
        )


def main(args):
    if len(args) != 4:
        raise SystemExit(f"Usage: {args[0]} portfoliofile logfile fmt")
    ticker(portfile=args[1], logfile=args[2], fmt=args[3])


if __name__ == "__main__":
    import sys

    main(sys.argv)
