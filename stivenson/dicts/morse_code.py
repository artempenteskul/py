morse_symbols = {
    'A': '.–', 'B': '–...', 'C': '–.–.', 'D': '–..', 'E': '.', 'F': '..–.', 'G': '––.',
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.–..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '––.–', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '--..--', 'Y': '–.––', 'Z': '––..', '0': '–––––',
    '1': '.––––', '2': '..–––', '3': '...––', '4': '....–', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.'
}


def word_into_morse_code(text: str):
    res = ''
    for symbol in text:
        if symbol.upper() in morse_symbols:
            res += morse_symbols[symbol.upper()] + ' '
    return res


if __name__ == '__main__':
    users_text = input('Enter text you want to transform into morse code: ')
    print(word_into_morse_code(text=users_text))
