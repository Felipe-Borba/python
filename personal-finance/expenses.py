from datetime import date
from enum import Enum


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

    def _push_statement(self, operation_date: date, value: float, kind: str, note: str, operation: Operation):
        value = abs(value)
        statement = Statement(operation, operation_date, value, kind, note)
        self.statements.append(statement)

    def add_spending(self, operation_date: date, value: float, kind='', note=''):
        self._push_statement(operation_date, value, kind, note, Operation.OUT)

    def add_income(self, operation_date: date, value: float, kind='', note=''):
        self._push_statement(operation_date, value, kind, note, Operation.IN)

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

    def __str__(self):
        if len(self.statements) == 0:
            return 'nenhum dado cadastrado'

        temp = ''
        for statement in self.statements:
            temp += statement.__str__()
            temp += '\n'
        return temp
