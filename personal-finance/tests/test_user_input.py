from expenses import Expenses
from main import handle_user_input
import builtins


class TestUserInput:
    expense = Expenses()
    menu = [
        '\n-------------------------\n',
        '[X] Digite uma opção abaixo',
        '[0] Sair',
        '[1] Cadastrar ganho',
        '[2] Cadastrar gasto',
        '[3] Ver saldo por mês',
        '[4] Ver extrato',
        '[5] Var valor total em conta',
        '[6] Ver gastos por tipo',
    ]

    def test_given_program_running_when_user_type_0_then_program_should_exit(self, monkeypatch):
        input_values = ['0']
        print_values = []
        monkeypatch.setattr(builtins, 'input', lambda: input_values.pop(0))
        monkeypatch.setattr(builtins, 'print', lambda s: print_values.append(s))

        handle_user_input(self.expense)

        expected_output = self.menu.copy()
        expected_output.append('bye')
        assert print_values == expected_output

    def test_given_expense_empty_when_user_sees_extrato_then_should_return_empty_extrato(self, monkeypatch):
        input_values = ['4', '0']
        print_values = []
        monkeypatch.setattr(builtins, 'input', lambda: input_values.pop(0))
        monkeypatch.setattr(builtins, 'print', lambda s: print_values.append(s.__str__()))

        handle_user_input(self.expense)

        expected_output = self.menu.copy()
        expected_output.append('nenhum dado cadastrado')
        expected_output += self.menu
        expected_output.append('bye')
        assert print_values == expected_output
