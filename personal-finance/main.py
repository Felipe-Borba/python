import datetime

from expenses import Expenses


def handle_user_input(expenses: Expenses):
    while True:
        try:
            print('\n-------------------------\n')
            print('[X] Digite uma opção abaixo')
            print('[0] Sair')
            print('[1] Cadastrar ganho')
            print('[2] Cadastrar gasto')
            print('[3] Ver saldo por mês')
            print('[4] Ver extrato')
            print('[5] Var valor total em conta')
            print('[6] Ver gastos por tipo')

            match input():
                case '0':
                    print('bye')
                    return
                case '1':
                    [value, kind, note] = prompt_user_expense()
                    user_date = prompt_date()

                    expenses.add_income(user_date, value, kind, note)
                case '2':
                    [value, kind, note] = prompt_user_expense()
                    user_date = prompt_date()

                    expenses.add_spending(user_date, value, kind, note)
                case '3':
                    balance = expenses.get_balance_by_month()
                    print(balance)
                case '4':
                    print(expenses)
                case '5':
                    print('Valor total em conta:\n', expenses.get_balance())
                case '6':
                    print('Total de gastos por Tipo:\n', expenses.get_expenses_by_kind())
                case _:
                    print('Opção Inválida')
        except Exception as error:
            print(error)


def prompt_date():
    try:
        user_input = input('Digite uma Data [dd-mm-yyyy]')
        return datetime.datetime.strptime(user_input, '%d-%m-%Y').date()
    except Exception:
        raise ValueError('Data inválida')


def prompt_user_expense():
    try:
        raw_value = input('Digite um valor')
        value = float(raw_value)
    except Exception:
        raise ValueError('Valor inválido')

    try:
        raw_kind = input('Digite um tipo')
        kind = raw_kind.strip()
    except Exception:
        raise ValueError('Tipo inválido')

    try:
        raw_note = input('Digite uma nota')
        note = raw_note.strip()
    except Exception:
        raise ValueError('Nota inválida')

    return value, kind, note


def print_gastos_por_tipo(gastos):
    gastos = gastos.get_expenses_by_kind()
    for gasto in gastos:
        print(f"{gasto}={gastos[gasto]}")


if __name__ == '__main__':
    expense = Expenses()
    handle_user_input(expense)
