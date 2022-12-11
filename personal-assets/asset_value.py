import yfinance as yf


def prompt_asset_value():
    print('Deseja verificar o preço de qual ação?')
    ticket = input('Digite o ticket da ação')

    value = get_asset_value(ticket)

    print("Preço atual: R$ {:.2f}".format(value))


def get_asset_value(value: str):
    if not value:
        return 0

    msft = yf.Ticker(value.upper() + '.SA')
    history = msft.history(period="1d")
    open = history.Open.values[0]
    close = history.Close.values[0]
    return close
