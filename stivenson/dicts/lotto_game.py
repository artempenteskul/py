from random import shuffle


attempts = []


def create_all_lotto_cards(lotto_card: str):
    lotto_cards = []
    word = 'BINGO'

    i = 1
    j = 16

    for letter in word:
        for num in range(i, j):
            lotto_cards.append(letter + str(num))
        i += 15
        j += 15

    shuffle(lotto_cards)

    if lotto_card not in lotto_cards:
        print('Lotto card is not in suitable format')
        exit()

    counter = 0

    for card in lotto_cards:
        counter += 1
        if lotto_card == card:
            attempts.append(counter)
            break


if __name__ == '__main__':
    users_lotto_card = input('Enter your lotto card: ')
    for i in range(1000):
        create_all_lotto_cards(lotto_card=users_lotto_card)
    print(len(attempts))
    print(f'Minimal attempts quantity: {min(attempts)}')
    print(f'Maximum attempts quantity: {max(attempts)}')
    print(f'Average attempts quantity: {sum(attempts) / len(attempts):.2f}')
