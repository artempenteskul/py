vowel = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

punctuation_marks = ['.', ',', '!', '?']


def pig_latin_next(text: str):
    words = text.split()
    pig_latin_words = []
    for word in words:
        if word[0] in vowel:
            if word[-1] in punctuation_marks:
                pig_latin_words.append(word[:-1] + 'way' + word[-1])
            else:
                pig_latin_words.append(word + 'way')
        if word[0] not in vowel:
            s_index = 0
            for symbol in word:
                if symbol in vowel:
                    s_index = word.index(symbol)
                    break
            if word[-1] in punctuation_marks:
                pig_latin_words.append(word[s_index:-1] + word[:s_index] + 'ay' + word[-1])
            else:
                pig_latin_words.append(word[s_index:] + word[:s_index] + 'ay')
    return pig_latin_words


if __name__ == '__main__':
    test_text = 'computer! Anything Think,'
    print(f'Test pig latin: {pig_latin_next(text=test_text)}')

    user_text = input('Enter text to test pig latin next algorithm: ')
    print(f'Your pig latin next text: {pig_latin_next(text=user_text)}')
