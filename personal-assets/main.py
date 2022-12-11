from asset_value import prompt_asset_value


def main_menu():
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


if __name__ == '__main__':
    while True:
        try:
            main_menu()
        except Exception as error:
            print(error)

        continue_running()
