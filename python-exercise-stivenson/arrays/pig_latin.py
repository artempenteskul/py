from only_words import only_words

vowel = ('a', 'e', 'i', 'o', 'u')


def pig_latin(text: str):
    words = only_words(line=text)
    pig_latin_words = []
    for word in words:
        if word[0] in vowel:
            pig_latin_words.append(word + 'way')
        if word[0] not in vowel:
            s_index = 0
            for symbol in word:
                if symbol in vowel:
                    s_index = word.index(symbol)
                    break
            pig_latin_words.append(word[s_index:] + word[:s_index] + 'ay')
    return pig_latin_words


if __name__ == '__main__':
    test_text = 'think office computer algorithm'
    print(f'Test pig latin: {pig_latin(text=test_text)}')

    user_text = input('Enter text to test pig latin: ')
    print(f'Your words with pig latin: {pig_latin(text=user_text)}')
