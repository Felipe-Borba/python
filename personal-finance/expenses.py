from datetime import date
from enum import Enum


class Operation(Enum):
    IN = 'Ganho'
    OUT = 'Gasto'


class Statement:
    def __init__(self, operacao: Operation, data: date, valor: float, tipo='', obs=''):
        self.operacao = operacao
        self.data = data
        self.valor = valor
        self.tipo = tipo
        self.obs = obs

    def __str__(self):
        return f"{self.data.isoformat()} - {self.operacao.value} - {self.valor} - {self.tipo} - {self.obs}"


class Expenses:
    def __init__(self):
        self.statements = []

    def _push_statement(self, ano, mes, dia, valor, tipo, obs, operacao: Operation):
        statement = Statement(operacao=operacao, data=date(year=int(ano), month=int(mes), day=int(dia)),
                              valor=float(valor),
                              tipo=str(tipo).lower().strip(), obs=str(obs).strip())
        self.statements.append(statement)

    def add_expense(self, ano, mes, dia, valor, tipo, obs):
        self._push_statement(ano, mes, dia, valor, tipo, obs, Operation.OUT)

    def add_income(self, ano, mes, dia, valor, tipo, obs):
        self._push_statement(ano, mes, dia, valor, tipo, obs, Operation.IN)

    # TODO change method to __str__ and return string
    def print_extrato(self):
        if len(self.statements) == 0:
            print('nenhum dado cadastrado')
            return

        temp = ''
        for statement in self.statements:
            temp += statement.__str__()
            temp += '\n'
        print(temp)

    def get_valor_total(self):
        total = 0
        for statement in self.statements:
            if statement.operacao == Operation.IN:
                total += statement.valor
            else:
                total -= statement.valor
        return total

    def get_gastos_por_tipo(self):
        expenses = {}
        for statement in self.statements:
            if statement.operacao == Operation.OUT:
                if statement.tipo in expenses.keys():
                    expenses[statement.tipo] += statement.valor
                else:
                    expenses[statement.tipo] = statement.valor
        return expenses

    def print_gastos_por_tipo(self):
        gastos = self.get_gastos_por_tipo()
        for gasto in gastos:
            print(f"{gasto}={gastos[gasto]}")
