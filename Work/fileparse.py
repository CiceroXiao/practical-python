# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(
    lines,
    select=None,
    types=None,
    has_headers=True,
    delimiter=",",
    silence_errors=True,
) -> list[dict] | list[tuple]:
    """解析 csv 文件的数据
    :param lines: csv 文件路径
    :param select: list ，要读取的字段内容，默认为 None ，即读取文件中的所有字段
    :paran types: list ，字段对应的数据类型，默认为 None ，即不转换文件中的字段数据类型
    :param has_headers: 文件是否有表头，默认为 True ，即文件有表头
    :param delimiter: csv 文件的分隔符，默认为 “,”
    :return records: 如果文件有表头，则以 list[dict] 格式返回文件的数据；
                     否则，以 list[tuple] 格式返回文件的数据"""
    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")

    rows = csv.reader(lines, delimiter=delimiter)

    header = next(rows) if has_headers else []
    if select:
        try:
            field_indices = [header.index(colname) for colname in select]
        except ValueError as value_error:
            raise ValueError("字段错误，请您检查所提交的字段名") from value_error
        header = select
    else:
        field_indices = []

    records = []
    start = 0 if has_headers else 1
    for rowno, row in enumerate(rows, start=start):
        if not row:
            continue
        if field_indices:
            row = [row[index] for index in field_indices]

        try:
            row = [func(val) for func, val in zip(types, row)]
        except ValueError as exc:
            if silence_errors:
                continue
            print(f"Row {rowno}: Couldn't convert [{row}]")
            print(f"Row {rowno}: {exc}")

        record = dict(zip(header, row)) if has_headers else tuple(row)
        records.append(record)

    return records


if __name__ == "__main__":
    try:
        with open(r"Data/missing.csv", mode="rt", encoding="utf-8") as f:
            portfolio = parse_csv(
                lines=f,
                types=[str, int, float],
                # has_headers=True,
                # delimiter=" ",
            )
    except FileNotFoundError as file_error:
        raise FileNotFoundError("文件路径错误，请您检查所提交的文件路径") from file_error
    print(portfolio)
