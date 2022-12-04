import datetime
from datetime import date

from expenses import Expenses


def main():
    expense = Expenses()
    while True:
        print('\n---\nDeseja cadastrar um ganho ou gasto?\nver extrato?\ndigite 0 para sair')
        command = input()

        try:
            match command:
                case '0':
                    print('bye')
                    return
                case 'ganho':
                    day, montante, month, obs, tipo, year = get_input_value()

                    validate_date(year, month, day)
                    input_date = date(year=int(year), month=int(month), day=int(day))

                    expense.add_income(input_date, montante, tipo, obs)
                case 'gasto':
                    day, montante, month, obs, tipo, year = get_input_value()

                    validate_date(year, month, day)
                    input_date = date(year=int(year), month=int(month), day=int(day))

                    expense.add_expense(input_date, montante, tipo, obs)
                case 'extrato':
                    print(expense)
                case _:
                    print('Entrada invalida')
                    pass

            print('Valor total em conta:', expense.get_valor_total())
            print('Total de gastos por Tipo:')
            print_gastos_por_tipo(expense)

        except:
            pass


def get_input_value():
    try:
        values = input('[ano, mes, dia, valor, tipo, obs]\n')
        [ano, mes, dia, valor, tipo, obs] = values.split(',')
        year = str(ano).strip()
        month = str(mes).strip()
        day = str(dia).strip()
        montante = float(valor)
        return day, montante, month, obs, tipo, year
    except:
        print('formato da entrada errada\n')
        raise


def validate_date(year, month, day):
    try:
        date_str = year + '-' + month + '-' + day
        datetime.strptime(date_str, '%Y-%m-%d')
    except:
        print("Data invalida")
        raise


def print_gastos_por_tipo(gastos):
    gastos = gastos.get_gastos_por_tipo()
    for gasto in gastos:
        print(f"{gasto}={gastos[gasto]}")


if __name__ == '__main__':
    main()
