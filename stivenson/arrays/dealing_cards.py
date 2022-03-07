from random import choice

from cards_desk import create_deck, shuffle_deck

cards_deck = create_deck()
shuffled_deck = shuffle_deck(cards_deck)


def deal_cards(players: int, cards_quantity: int, shuffled_cards_deck: list):
    players_cards = [[] for x in range(players)]

    quantity = 0

    while quantity != cards_quantity:
        for player in players_cards:
            card = choice(shuffled_cards_deck)
            shuffled_deck.remove(card)
            player.append(card)
        quantity += 1

    return players_cards, shuffled_cards_deck


if __name__ == '__main__':
    players_decks, rest_shuffled_deck = deal_cards(players=4, cards_quantity=5, shuffled_cards_deck=shuffled_deck)
    print('-' * 20)
    for each_player_deck in players_decks:
        print(each_player_deck)
    print('-' * 20)
    print(f'Rest cards deck: {rest_shuffled_deck}')
