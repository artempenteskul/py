from random import choice

values = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')
suits = ('d', 's', 'c', 'h')

cards_deck = []


def create_deck():
    for suit in suits:
        for value in values:
            card = value + suit
            cards_deck.append(card)
    return cards_deck


shuffled_cards_deck = []


def shuffle_deck(cards_deck: list):
    card = choice(cards_deck)
    while len(shuffled_cards_deck) != len(cards_deck):
        if card not in shuffled_cards_deck:
            shuffled_cards_deck.append(card)
        card = choice(cards_deck)
    return shuffled_cards_deck


if __name__ == '__main__':
    print(f'Cards deck - {create_deck()}')
    print(f'Shuffled cards deck -  {shuffle_deck(cards_deck=cards_deck)}')
