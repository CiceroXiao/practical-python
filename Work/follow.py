# follow.py
import os
import time


def follow(filepath):
    """以生成器的方式不断返回某个文件的内容，直至该文件没有新内容"""
    f = open(filepath)
    f.seek(0, os.SEEK_END)
    while True:
        line = f.readline()
        if line == "":
            time.sleep(0.1)
            continue
        yield line


# f = open("Data/stocklog.csv")
# f.seek(0, os.SEEK_END)  # Move file porinter 0 bytes from end of file

# while True:
#     line = f.readline()
#     if line == "":
#         time.sleep(0.1)  # Sleep briefly and retry
#         continue
#     fields = line.split(",")
#     name = fields[0].strip('"')
#     price = float(fields[1])
#     change = float(fields[4])
#     if change < 0:
#         print(f"{name:>10s} {price:>10.2f} {change:>10.2f}")

if __name__ == "__main__":
    import report

    portfolio = report.read_portfolio("Data/portfolio.csv")

    for line in follow("Data/stocklog.csv"):
        fields = line.split(",")
        name = fields[0].strip(",")
        price = float(fields[1])
        change = float(fields[4])
        if name in portfolio:
            print(f"{name:>10s} {price:>10.2f} {change:>10.2f}")
