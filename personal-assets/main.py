def main_menu():
    command = input('Digite\n [0] Sair\n [1] Cadastrar compra/venda de ação\n [2] Ver o preço da ação\n:')
    match command:
        case '0':
            exit()
        case '1':
            print('TODO cadastro ação')
        case '2':
            assets_value()


def assets_value():
    print('Deseja verificar o preço de qual ação?')
    ticket = input('Digite o ticket da ação')
    print(ticket)


if __name__ == '__main__':
    while True:
        try:
            main_menu()
        except Exception as error:
            print(error)
