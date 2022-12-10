import builtins

import pytest

from expenses import Expenses
from main import handle_user_input, prompt_user_expense


class TestMain:
    expense = Expenses()
    menu = (
        '\n-------------------------\n',
        '[X] Digite uma opção abaixo',
        '[0] Sair',
        '[1] Cadastrar ganho',
        '[2] Cadastrar gasto',
        '[3] Ver saldo por mês',
        '[4] Ver extrato',
        '[5] Var valor total em conta',
        '[6] Ver gastos por tipo',
    )

    def test_handle_user_input_when_user_try_to_exit_then_program_should_exit(self, monkeypatch):
        input_values = ['0']
        print_values = []
        monkeypatch.setattr(builtins, 'input', lambda: input_values.pop(0))
        monkeypatch.setattr(builtins, 'print', lambda s: print_values.append(s))

        handle_user_input(self.expense)

        expected_output = [i for i in self.menu]
        expected_output.append('bye')
        assert print_values == expected_output

    def test_handle_user_input_when_user_sees_extrato_then_should_return_empty_extrato(self, monkeypatch):
        input_values = ['4', '0']
        print_values = []
        monkeypatch.setattr(builtins, 'input', lambda: input_values.pop(0))
        monkeypatch.setattr(builtins, 'print', lambda s: print_values.append(s.__str__()))

        handle_user_input(self.expense)

        expected_output = [i for i in self.menu]
        expected_output.append('nenhum dado cadastrado')
        expected_output += self.menu
        expected_output.append('bye')
        assert print_values == expected_output

    def test_handle_user_input_when_add_new_expense_then_add_in_expense_obj(self, monkeypatch):
        input_values = ['1', '100', 'kind', 'note', '25-12-2022', '4', '0']
        print_values = []
        monkeypatch.setattr(builtins, 'input', lambda s='': input_values.pop(0))
        monkeypatch.setattr(builtins, 'print', lambda s: print_values.append(s.__str__()))

        handle_user_input(self.expense)

        expected_output = [i for i in self.menu]
        expected_output += self.menu
        expected_output.append('2022-12-25 - Ganho - 100.0 - kind - note\n')
        expected_output += self.menu
        expected_output.append('bye')
        assert print_values == expected_output

    def test_prompt_user_expense_when_add_valid_values_then_return_expense_params(self, monkeypatch):
        input_values = ['100', 'kind', 'note']
        monkeypatch.setattr(builtins, 'input', lambda s: input_values.pop(0))

        response = prompt_user_expense()

        assert response == (100.0, 'kind', 'note')

    def test_prompt_user_expense_when_add_invalid_value_then_throw_error(self, monkeypatch):
        with pytest.raises(ValueError, match=r"Valor inválido"):
            input_values = ['invalid', 'kind', 'note']
            monkeypatch.setattr(builtins, 'input', lambda s: input_values.pop(0))

            prompt_user_expense()
