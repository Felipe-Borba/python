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

        expenses.add_spending(self.today, 555, 'some kind', 'some note')

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
        expenses.add_spending(operation_date=self.today, value=50.99, kind='milk', note='cat milk')

        total = expenses.get_balance()

        assert total == 450.00

    def test_given_expenses_with_incomes_and_spending_when_get_expenses_by_type_then_returns_expenses_grouped_by_kind(
            self):
        expenses = Expenses()
        expenses.add_income(operation_date=self.today, value=500.99, kind='salary', note='na')
        expenses.add_spending(operation_date=self.today, value=50, kind='milk', note='cat')
        expenses.add_spending(operation_date=self.today, value=50, kind='milk', note='wolf')
        expenses.add_spending(operation_date=self.today, value=40, kind='ball', note='wolf')
        expenses.add_spending(operation_date=self.today, value=40, kind='ball', note='cat')

        result = expenses.get_expenses_by_kind()

        assert result == {'milk': 100, 'ball': 80}

    def test_given_expenses_when_add_income_with_negative_value_then_add_statement_with_abs_value(self):
        expenses = Expenses()

        expenses.add_income(operation_date=self.today, value=-100, kind='salary', note='senegal')

        statement = expenses.statements[0]
        assert statement.value == 100

    def test_given_expenses_when_add_spending_with_negative_value_then_add_statement_with_abs_value(self):
        expenses = Expenses()

        expenses.add_spending(operation_date=self.today, value=-300, kind='salary', note='senegal')

        statement = expenses.statements[0]
        assert statement.value == 300

    def test_given_expenses_when_add_spending_with_installment_then_add_statements_with_correct_date(
            self):
        expenses = Expenses()
        date = [datetime.date(2022, 1, 20), datetime.date(2022, 2, 20), datetime.date(2022, 3, 20)]

        expenses.add_spending(operation_date=date[0], value=100, kind='salary', note='England', instalments=3)

        assert len(expenses.statements) == 3
        for i in range(0, 3):
            statement = expenses.statements[i]
            assert statement.value == 100
            assert statement.operation_date == date[i]

    def test_given_expenses_when_add_income_with_installment_then_add_statements_with_correct_date(
            self):
        expenses = Expenses()
        date = [datetime.date(2022, 5, 20), datetime.date(2022, 6, 20), datetime.date(2022, 7, 20)]

        expenses.add_income(operation_date=date[0], value=300, kind='salary', note='England', instalments=3)

        assert len(expenses.statements) == 3
        for i in range(0, 3):
            statement = expenses.statements[i]
            assert statement.value == 300
            assert statement.operation_date == date[i]

    def test_given_expenses_when_get_balance_by_month_then_return_total_balance_by_month(self):
        expenses = Expenses()
        expenses.add_income(operation_date=datetime.date(2022, 1, 1), value=100, instalments=12)
        expenses.add_spending(operation_date=datetime.date(2022, 2, 1), value=150, instalments=5)

        result = expenses.get_balance_by_month()

        assert result == {
            1: 100,
            2: -50,
            3: -50,
            4: -50,
            5: -50,
            6: -50,
            7: 100,
            8: 100,
            9: 100,
            10: 100,
            11: 100,
            12: 100,
        }

    def test_given_expenses_empty_when_get_balance_by_month_then_return_empty_dict(self):
        expenses = Expenses()

        result = expenses.get_balance_by_month()

        assert result == {}
