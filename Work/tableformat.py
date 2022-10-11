# tableformat.py


class TableFormatter:
    def headings(self, headers):
        """
        Emit the table headings.
        """

    def row(self, rowdata):
        """
        Emit a single row of table data.
        """


class TextTableFormatter(TableFormatter):
    """以表格形式来输出文件中的数据"""

    def headings(self, headers):
        """输出文件的表头

        Args:
            headers: 文件的表头数据
        """
        for header in headers:
            print(f"{header:>10s}", end=" ")
        print()
        print(("-" * 10 + " ") * len(headers))

    def row(self, rowdata):
        """输出文件的非表头数据

        Args:
            rowdata: 文件的非表头数据
        """
        import math
        for data in rowdata:
            try:
                print(f"{data:>10s}", end="")
            except ValueError:
                if math.floor(data) == data:
                    print(f"{data:>10d}", end="")
                else:
                    print(f"{data:>10.2f}", end="")
        print()


class CSVTableFormatter(TableFormatter):
    """以 csv 的原始数据格式来输出文件中的数据"""

    def headings(self, headers):
        """输出文件的表头

        Args:
            headers: 数据的表头
        """
        print(",".join(headers))

    def row(self, rowdata):
        """输出文件的非表头数据

        Args:
            rowdata: 文件的非表头数据
        """
        print(",".join(rowdata))


class HTMLTableFormatter(TableFormatter):
    """以 HTML 的格式来输出文件中的数据"""

    def headings(self, headers):
        """以 HTML 格式输出文件中的数据

        Args:
            headers: 文件的表头数据
        """
        print("<tr>", end="")
        for header in headers:
            print(f"<th>{header}</th>", end="")
        print("</tr>")

    def row(self, rowdata):
        """输出文件的非表头数据

        Args:
            rowdata: 文件的非表头数据
        """
        print(
            f"<tr><td>{rowdata[0]}</td><td>{rowdata[1]}"
            f"</td><td>{rowdata[2]}</td><td>{rowdata[2]}</td></tr>"
        )


class FormatError(Exception):
    pass


def create_formatter(fmt):
    """根据传入的文件类型使用不同的输出格式。

    Args:
        fmt (str): 传入的文件格式。
    """
    if fmt == "txt":
        return TextTableFormatter()
    elif fmt == "csv":
        return CSVTableFormatter()
    elif fmt == "html":
        return HTMLTableFormatter()
    else:
        raise FormatError(f"Unknown format {fmt}")


def print_table(data, select: list, formatter):
    """根据文件格式来输出指定字段的内容。

    Args:
        data (_type_): 文件数据。
        select (list): 用户选择输出的字段，默认为 None，即输出全部字段。
        formatter (_type_): 文件的格式。
    """
    headers = select
    formatter.headings(headers)

    for _ in data:
        rowdata = [getattr(_, colname) for colname in select]
        formatter.row(rowdata)
