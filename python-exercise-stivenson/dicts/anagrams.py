def is_anagrams(word1: str, word2: str):
    word1_symbols = {}
    word2_symbols = {}

    for symbol in word1:
        word1_symbols[symbol] = word1.count(symbol)
    for symbol in word2:
        word2_symbols[symbol] = word2.count(symbol)

    return True if word1_symbols == word2_symbols else False


if __name__ == '__main__':
    users_word1 = input('Enter the first word: ')
    users_word2 = input('Enter second word: ')
    print(f'Is {users_word1} and {users_word2} anagrams: {is_anagrams(word1=users_word1, word2=users_word2)}')
