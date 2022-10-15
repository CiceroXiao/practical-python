# follow.py
import os
import time


def follow(filepath):
    """以生成器的方式不断返回某个文件的内容，直至该文件没有新内容"""
    f = open(filepath)
    f.seek(0, os.SEEK_END)
    while True:
        line = f.readline()
        if line != "":
            yield line
        else:
            time.sleep(0.1)


if __name__ == "__main__":
    import report

    portfolio = report.read_portfolio("Data/portfolio.csv")

    for line in follow("Data/stocklog.csv"):
        print(line)
        fields = line.split(",")
        name = fields[0].strip(",")
        price = float(fields[1])
        change = float(fields[4])
        if name in portfolio:
            print(f"{name:>10s} {price:>10.2f} {change:>10.2f}")
