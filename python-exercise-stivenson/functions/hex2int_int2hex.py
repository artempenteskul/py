import random

hex_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
int_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']


def hex_to_int(symbol):
    if '0' <= symbol <= '9':
        return symbol
    elif symbol == 'A':
        return '10'
    elif symbol == 'B':
        return '11'
    elif symbol == 'C':
        return '12'
    elif symbol == 'D':
        return '13'
    elif symbol == 'E':
        return '14'
    elif symbol == 'F':
        return '15'
    return 'You typed something wrong'


def int_to_hex(symbol):
    if '0' <= symbol <= '9':
        return symbol
    elif symbol == '10':
        return 'A'
    elif symbol == '11':
        return 'B'
    elif symbol == '12':
        return 'C'
    elif symbol == '13':
        return 'D'
    elif symbol == '14':
        return 'E'
    elif symbol == '15':
        return 'F'
    return 'You typed something wromg'


if __name__ == '__main__':
    hex_symbol = random.choice(hex_list)
    int_symbol = random.choice(int_list)
    print(f'Hex symbol {hex_symbol} is {hex_to_int(hex_symbol)} in decimal')
    print(f'Decimal symbol {int_symbol} is {int_to_hex(int_symbol)} in hex')
