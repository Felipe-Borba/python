from datetime import date
from enum import Enum
from dateutil.relativedelta import relativedelta


class Operation(Enum):
    IN = 'Ganho'
    OUT = 'Gasto'


class Statement:
    def __init__(self, operation: Operation, operation_date: date, value: float, kind: str, note: str):
        self.operation = operation
        self.operation_date = operation_date
        self.value = value
        self.kind = kind.lower().strip()
        self.note = note.strip()

    def __str__(self):
        return f"{self.operation_date.isoformat()} - {self.operation.value} - {self.value} - {self.kind} - {self.note}"


class Expenses:
    def __init__(self):
        self.statements = []

    def _push_statement(self, operation_date: date, value: float, kind: str, note: str, operation: Operation,
                        instalments: int):
        if instalments < 1:
            return

        value = abs(value)
        statement = Statement(operation, operation_date, value, kind, note)
        self.statements.append(statement)
        next_month = operation_date + relativedelta(months=1)
        self._push_statement(next_month, value, kind, note, operation, instalments - 1)

    def add_spending(self, operation_date: date, value: float, kind='', note='', instalments=1):
        self._push_statement(operation_date, value, kind, note, Operation.OUT, instalments)

    def add_income(self, operation_date: date, value: float, kind='', note='', instalments=1):
        self._push_statement(operation_date, value, kind, note, Operation.IN, instalments)

    def get_balance(self):
        total = 0
        for statement in self.statements:
            if statement.operation == Operation.IN:
                total += statement.value
            else:
                total -= statement.value
        return total

    def get_expenses_by_kind(self):
        expenses = {}
        for statement in self.statements:
            if statement.operation == Operation.OUT:
                if statement.kind in expenses.keys():
                    expenses[statement.kind] += statement.value
                else:
                    expenses[statement.kind] = statement.value
        return expenses

    def get_balance_by_month(self):
        balance = {}

        for statement in self.statements:
            month = statement.operation_date.month
            if month not in balance.keys():
                balance[month] = statement.value
            elif statement.operation == Operation.IN:
                balance[month] += statement.value
            else:
                balance[month] -= statement.value

        return balance

    def __str__(self):
        if len(self.statements) == 0:
            return 'nenhum dado cadastrado'

        temp = ''
        for statement in self.statements:
            temp += statement.__str__()
            temp += '\n'
        return temp
