import datetime


class Stock:
    operations = []

    def __init__(self, ticket: str, price: float, operation: str, quantity: int, date: datetime.date):
        self._is_valid_operation(operation)

        self.ticket = ticket.upper()
        self.operation = [(date, price, quantity, operation)]

    def add_operation(self, price: float, operation: str, quantity: int, date: datetime.date):
        self._is_valid_operation(operation)
        self.operation.append((date, price, quantity, operation))

    @staticmethod
    def _is_valid_operation(operation):
        if operation != 'compra' and operation != 'venda':
            raise ValueError('Operação inválida')

    def get_summary(self):
        pass

    def __eq__(self, other):
        return self.ticket == other.ticket
