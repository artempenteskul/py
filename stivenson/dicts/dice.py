from random import randint


def two_dice():
    num1 = randint(1, 6)
    num2 = randint(1, 6)
    return num1 + num2


if __name__ == '__main__':

    expected = {
        2: 2.78, 3: 5.56, 4: 8.33,
        5: 11.11, 6: 13.89, 7: 16.67,
        8: 13.89, 9: 11.11, 10: 8.33,
        11: 5.56, 12: 2.78
    }

    results = {
        2: 0, 3: 0, 4: 0,
        5: 0, 6: 0, 7: 0,
        8: 0, 9: 0, 10: 0,
        11: 0, 12: 0
    }

    for i in range(1000):
        res = two_dice()
        results[res] += 1

    for i in sorted(results.keys()):
        print(f'{i} - {results[i] / 1000 * 100:.2f} - {expected[i]}')
