from Stock import Stock
from asset_value import prompt_asset_value
from utils import input_type, input_date


def main_menu(stock_list):
    command = input(
        'Digite\n [0] Sair\n [1] Cadastrar compra/venda de ação\n [2] Ver o preço da ação\n [3] Ver ação\n:')

    match command:
        case '0':
            exit()
        case '1':
            add_stock(stock_list)
        case '2':
            prompt_asset_value()
        case '3':
            print_stock_info_by_name(stock_list)


def print_stock_info_by_name(stock_list):
    ticket = input('Digite o nome da ação')
    stock_ticket = Stock(ticket)
    if stock_ticket in stock_list:
        stock_index = stock_list.index(stock_ticket)
        stock_item = stock_list[stock_index]
        print('(mês - Saldo Total de ações - Lucro/Prejuízo)')
        for item in stock_item.get_resume():
            print(item)
    else:
        print('ação não encontrada')


def add_stock(stock_list):
    ticket = input('Digite o nome da ação')
    new_stock = Stock(ticket)

    operation = input('Deseja cadastrar uma compra ou venda?')
    price = input_type(float, 'Digite o preço da ação')
    quantity = input_type(int, 'Digite a quantidade da ação', 'quantidade inválida')
    date = input_date()

    if new_stock in stock_list:
        stock_index = stock_list.index(new_stock)
        stock_item = stock_list[stock_index]
        stock_item.add_operation(price, operation, quantity, date)
    else:
        new_stock.add_operation(price, operation, quantity, date)
        stock_list.append(new_stock)


def continue_running():
    can_exit = input('\nDeseja continuar? [y/n]:')
    if can_exit != 'y':
        exit()
    print('\n----')


if __name__ == '__main__':
    stocks = []
    while True:
        try:
            main_menu(stocks)
        except Exception as error:
            print(error)

        continue_running()
