import datetime

from Stock import Stock
from asset_value import prompt_asset_value


def main_menu(stocks):
    command = input('Digite\n [0] Sair\n [1] Cadastrar compra/venda de ação\n [2] Ver o preço da ação\n:')
    match command:
        case '0':
            exit()
        case '1':
            print('TODO cadastro ação')
        case '2':
            prompt_asset_value()


def continue_running():
    can_exit = input('\nDeseja continuar? [y/n]')
    if can_exit != 'y':
        exit()
    print('\n----')


def input_type(d_type, message, err='Valor inválido'):
    try:
        raw_value = input(message)
        return d_type(raw_value)
    except Exception:
        raise ValueError(err)


def input_date():
    try:
        user_input = input('Digite uma Data [dd-mm-yyyy]')
        return datetime.datetime.strptime(user_input, '%d-%m-%Y').date()
    except Exception:
        raise ValueError('Data inválida')


if __name__ == '__main__':
    # petra4 = Stock('PETR4', 23)
    # stocks = [petra4]
    # petra4 = Stock('PETR4', 20)
    # t = petra4 in stocks
    # print(t)

    stocks = []
    while True:
        try:
            main_menu(stocks)
        except Exception as error:
            print(error)

        continue_running()
