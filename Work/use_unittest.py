import unittest

import stock


class TestStock(unittest.TestCase):
    def test_create(self):
        s = stock.Stock("GOOG", 100, 490.1)
        self.assertEqual(s.name, "GOOG")
        self.assertEqual(s.shares, 90)
        self.assertEqual(s.price, 490.1)


if __name__ == "__mian__":
    unittest.main()
