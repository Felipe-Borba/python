import datetime
import unittest

from Stock import Stock


class TestStock(unittest.TestCase):

    def test_get_empy_resume(self):
        stock = Stock('WEGE3')
        expect = [('jan', 0, 0), ('fev', 0, 0), ('mar', 0, 0), ('abr', 0, 0), ('mai', 0, 0), ('jun', 0, 0),
                  ('jul', 0, 0), ('ago', 0, 0), ('set', 0, 0), ('out', 0, 0), ('nov', 0, 0), ('dez', 0, 0)]

        response = stock.get_resume()

        self.assertEqual(response, expect)

    def test_get_resume_with_buy_and_sale(self):
        stock = Stock('WEGE3')
        stock.add_operation(15.0, 'compra', 100, datetime.date(2022, 1, 14))
        stock.add_operation(16.5, 'venda', 100, datetime.date(2022, 2, 15))
        expect = [('jan', 1500.00, 0), ('fev', 0, 150), ('mar', 0, 0), ('abr', 0, 0), ('mai', 0, 0), ('jun', 0, 0),
                  ('jul', 0, 0), ('ago', 0, 0), ('set', 0, 0), ('out', 0, 0), ('nov', 0, 0), ('dez', 0, 0)]

        response = stock.get_resume()

        self.assertEqual(response, expect)

    def test_get_resume_with_buy(self):
        stock = Stock('WEGE3')
        stock.add_operation(15.0, 'compra', 100, datetime.date(2022, 1, 14))
        expect = [('jan', 1500.00, 0), ('fev', 0, 0), ('mar', 0, 0), ('abr', 0, 0), ('mai', 0, 0), ('jun', 0, 0),
                  ('jul', 0, 0), ('ago', 0, 0), ('set', 0, 0), ('out', 0, 0), ('nov', 0, 0), ('dez', 0, 0)]

        response = stock.get_resume()

        self.assertEqual(response, expect)


if __name__ == '__main__':
    unittest.main()
