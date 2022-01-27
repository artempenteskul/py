from only_words import only_words


def is_palindrome(text: str):
    words = only_words(text)
    words = [x.lower() for x in words]
    reversed_words = list(reversed(list(words)))
    if ''.join(words) == ''.join(reversed_words):
        return True
    return False


if __name__ == '__main__':
    possible_palindrome = input('Enter the text to check if it palindrome is: ')
    print(f'Is your text palindrome: {is_palindrome(text=possible_palindrome)}')
