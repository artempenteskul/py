button_to_symbol = {
    1: ['.', '?', '!', ':'],
    2: ['A', 'B', 'C'],
    3: ['D', 'E', 'F'],
    4: ['G', 'H', 'I'],
    5: ['J', 'K', 'L'],
    6: ['M', 'N', 'O'],
    7: ['P', 'Q', 'R', 'S'],
    8: ['T', 'U', 'V'],
    9: ['W', 'X', 'Y', 'Z'],
    0: [' ']
}


def old_phone_keyboard(text: str):
    res = ''
    for symbol in text:
        for button in button_to_symbol:
            if symbol.upper() in button_to_symbol[button]:
                symbol_index = button_to_symbol[button].index(symbol.upper()) + 1
                res += str(button) * symbol_index
    return res


if __name__ == '__main__':
    users_text = input('Enter your text to get old phone keyboard sequence of this text: ')
    print(old_phone_keyboard(text=users_text))
