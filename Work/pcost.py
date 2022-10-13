# # pcost.py
# #
# # Exercise 1.27
import report


def portfolio_cost(file_path: str) -> float:
    """计算该文件中的股票总费用"""
    try:
        records = report.read_portfolio(file_path=file_path)
        return records.total_cost
    except FileNotFoundError as exc:
        raise FileNotFoundError("请您提供有效的文件路径") from exc
    except IndexError as exc:
        raise IndexError("您提供的文件内容有误，请检查您的文件内容") from exc


def main(args):
    """执行脚本"""
    if len(args) != 2:
        raise SystemExit(f"Usage: {args[0]} " "portfile pricefile")
    total_cost = portfolio_cost(args[1])
    print(f"Total cost {total_cost:0.2f}")


if __name__ == "__main__":
    import sys

    main(sys.argv)
