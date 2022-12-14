import datetime


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
