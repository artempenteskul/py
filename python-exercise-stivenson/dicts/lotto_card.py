from random import randint


def create_lotto_card():
    lotto_card = {}
    word = 'BINGO'
    i = 1
    j = 15
    for symbol in word:
        lotto_card[symbol] = randint(i, j)
        i += 15
        j += 15
    return lotto_card


if __name__ == '__main__':
    card = create_lotto_card()

    for key in card:
        print(key, end='   ')

    print()

    for value in card.values():
        print(value, end='  ')

    print()
