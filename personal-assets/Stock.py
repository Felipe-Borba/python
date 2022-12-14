import datetime


class Stock:
    def __init__(self, ticket: str):
        self.ticket = ticket.upper().strip()
        self.operations = []

    def add_operation(self, price: float, operation_type: str, quantity: int, date: datetime.date):
        self._is_valid_operation(operation_type)

        self.operations.append((date, price, quantity, operation_type))

    @staticmethod
    def _is_valid_operation(operation):
        if operation != 'compra' and operation != 'venda':
            raise ValueError('Operação inválida')

    def get_resume(self):
        resume = [('jan', 0, 0), ('fev', 0, 0), ('mar', 0, 0), ('abr', 0, 0), ('mai', 0, 0), ('jun', 0, 0),
                  ('jul', 0, 0), ('ago', 0, 0), ('set', 0, 0), ('out', 0, 0), ('nov', 0, 0), ('dez', 0, 0)]

        total_stock_value = 0
        for operation in self.operations:
            (date, price, qtd, operation_type) = operation
            index_by_month = date.month - 1
            r = resume[index_by_month]

            if operation_type == 'compra':
                total_stock_value += r[1] + price * qtd
                resume[index_by_month] = (r[0], total_stock_value, r[2])
            elif operation_type == 'venda':
                total_earning = price * qtd - total_stock_value
                if total_earning > total_stock_value:
                    total_stock_value = 0
                else:
                    total_stock_value = total_earning
                resume[index_by_month] = (r[0], r[1], r[2] + total_earning)

        return resume

    def __eq__(self, other):
        return self.ticket == other.ticket
