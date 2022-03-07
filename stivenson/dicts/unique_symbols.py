unique_symbols_dict = {}


def count_unique(text: str):
    for symbol in text:
        unique_symbols_dict[symbol] = text.count(symbol)
    return len(unique_symbols_dict)


if __name__ == '__main__':
    users_text = input('Enter your text to count unique symbols: ')
    print(f'Unique symbols quantity: {count_unique(text=users_text)}')
    print(unique_symbols_dict)
