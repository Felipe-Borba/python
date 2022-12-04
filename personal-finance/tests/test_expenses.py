import datetime

from expenses import Expenses


class TestExpenses:
    today = datetime.date.today()

    def test_given_expenses_with_incomes_when_get_total_value_then_returns_value_sum(self):
        expenses = Expenses()
        expenses.add_income(operation_date=self.today, value=500.99, kind='salary', note='na')
        expenses.add_income(operation_date=self.today, value=50.02, kind='salary', note='na')

        total = expenses.get_valor_total()

        assert total == 551.01
