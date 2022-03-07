def only_words(line: str):
    symbols_to_exclude = ['.', ',', ':', '!', '?']
    line_without_symbols = ''
    for symbol in line:
        if symbol not in symbols_to_exclude:
            line_without_symbols += symbol
    words = line_without_symbols.split()
    return words


if __name__ == '__main__':
    text = input('Enter text in order to get list only of words from this text: ')
    print(f'Your list of words: {only_words(line=text)}')
