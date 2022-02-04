def is_sentence_anagrams(text1: str, text2: str):
    text1 = text1.lower().replace(' ', '')
    text2 = text2.lower().replace(' ', '')

    text1_symbols = {}
    text2_symbols = {}

    for symbol in text1:
        text1_symbols[symbol] = text1.count(symbol)

    for symbol in text2:
        text2_symbols[symbol] = text2.count(symbol)

    return True if text1_symbols == text2_symbols else False


if __name__ == '__main__':
    users_text1 = input('Enter your first sentence: ')
    users_text2 = input('Enter your second sentence: ')
    print(f'Is your sentences anagrams: {is_sentence_anagrams(text1=users_text1, text2=users_text2)}')
