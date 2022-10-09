# # pcost.py
# #
# # Exercise 1.27
import csv
import sys

if len(sys.argv) == 2:
    PORTFOLIO_PATH = sys.argv[1]
else:
    PORTFOLIO_PATH = (
        r"/home/cicero/Documents/Projects/practical-python/Work/Data/portfolio.csv"
    )


def portfolio_cost(file_path):
    """提供文件，计算该文件中的股票总费用（ shares * price ）"""
    try:
        with open(file_path, mode="rt", encoding="utf-8") as f:
            rows = csv.reader(f)
            _ = next(rows)

            cost = sum(int(_[1]) * float(_[2]) for _ in rows)
        return cost
    except FileNotFoundError as exc:
        raise FileNotFoundError("请您提供有效的文件路径") from exc
    except IndexError as exc:
        raise IndexError("您提供的文件内容有误，请检查您的文件内容") from exc
    except ValueError as exc:
        raise ValueError("您输入的数据有误，请您检查您的输入") from exc


total_cost = portfolio_cost(PORTFOLIO_PATH)

print(f"Total cost {total_cost:0.2f}")


# import gzip

# portfolio_zip_path = (
#     r"/home/cicero/Documents/Projects/practical-python/Work/Data/portfolio.csv.gz"
# )

# with gzip.open(portfolio_zip_path, mode="rt") as f:
#     for line in f:
#         print(line)
