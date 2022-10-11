# stock.py


class Stock:
    """股票对象"""

    def __init__(self, name, shares: int, price: float):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"

    @property
    def cost(self) -> float:
        """返回当前股票的花费额"""
        return self.shares * self.price

    def sell(self, sold_shares: int):
        """出售指定数额的股票
        :param sold_shares: 已出售的股票数量"""
        self.shares -= sold_shares

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError("Expected int")
        self._shares = value
