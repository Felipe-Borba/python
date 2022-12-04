import datetime

from expenses import Expenses


class TestExpenses:
    today = datetime.date.today()

    def test_given_expenses_when_add_income_then_push_in_statement_array(self):
        expenses = Expenses()

        expenses.add_income(self.today, 555, 'some kind', 'some note')

        assert len(expenses.statements) == 1
        statement = expenses.statements[0]
        assert statement.value == 555
        assert statement.operation_date == self.today
        assert statement.kind == 'some kind'
        assert statement.note == 'some note'

    def test_given_expenses_when_add_spending_then_push_in_statement_array(self):
        expenses = Expenses()

        expenses.add_expense(self.today, 555, 'some kind', 'some note')

        assert len(expenses.statements) == 1
        statement = expenses.statements[0]
        assert statement.value == 555
        assert statement.operation_date == self.today
        assert statement.kind == 'some kind'
        assert statement.note == 'some note'

    def test_given_expenses_with_incomes_when_get_balance_then_returns_value_sum(self):
        expenses = Expenses()
        expenses.add_income(operation_date=self.today, value=500.99, kind='salary', note='na')
        expenses.add_income(operation_date=self.today, value=50.02, kind='salary', note='na')

        total = expenses.get_balance()

        assert total == 551.01

    def test_given_expenses_with_incomes_and_spending_when_get_balance_then_returns_correct_value_sum(self):
        expenses = Expenses()
        expenses.add_income(operation_date=self.today, value=500.99, kind='salary', note='na')
        expenses.add_expense(operation_date=self.today, value=50.99, kind='milk', note='cat milk')

        total = expenses.get_balance()

        assert total == 450.00

    def test_given_expenses_with_incomes_and_spending_when_get_expenses_by_type_then_returns_expenses_grouped_by_kind(
            self):
        expenses = Expenses()
        expenses.add_income(operation_date=self.today, value=500.99, kind='salary', note='na')
        expenses.add_expense(operation_date=self.today, value=50, kind='milk', note='cat')
        expenses.add_expense(operation_date=self.today, value=50, kind='milk', note='wolf')
        expenses.add_expense(operation_date=self.today, value=40, kind='ball', note='wolf')
        expenses.add_expense(operation_date=self.today, value=40, kind='ball', note='cat')

        result = expenses.get_expenses_by_kind()

        assert result == {'milk': 100, 'ball': 80}
