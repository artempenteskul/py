teaspoons_per_tablespoon = 3
tablespoons_per_cup = 16


def cooking_measures(quantity, measurement):
    measurement = measurement.lower()

    teaspoons = 0

    if measurement == 'teaspoon' or measurement == 'teaspoons':
        teaspoons = quantity
    elif measurement == 'tablespoon' or measurement == 'tablespoons':
        teaspoons = quantity * teaspoons_per_tablespoon
    elif measurement == 'cup' or measurement == 'cups':
        teaspoons = quantity * teaspoons_per_tablespoon * tablespoons_per_cup

    cups = teaspoons // (teaspoons_per_tablespoon * tablespoons_per_cup)
    teaspoons %= teaspoons_per_tablespoon * tablespoons_per_cup

    tablespoons = teaspoons // teaspoons_per_tablespoon
    teaspoons %= teaspoons_per_tablespoon

    res = 'Result: '

    if cups > 0:
        res += f'{cups} cup'
        if cups > 1:
            res += 's'

    if tablespoons > 0:
        res += ', ' if res != '' else res
        res += f'{tablespoons} tablespoon'
        if tablespoons > 1:
            res += 's'

    if teaspoons > 0:
        res += ', ' if res != '' else res
        res += f'{teaspoons} teaspoon'
        if teaspoons > 1:
            res += 's'

    return res


if __name__ == '__main__':
    q = int(input('Enter the quantity of the ingredient: '))
    m = input('Enter the measurement (cups, tablespoons, teaspoons): ')

    print(cooking_measures(quantity=q, measurement=m))
