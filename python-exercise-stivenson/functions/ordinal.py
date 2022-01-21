number = int(input('Enter the number from 1 to 12: '))


def number_to_ordinal(num):
    if num < 1 or num > 12:
        return 'You entered less than 1 or more than 12'
    elif num == 1:
        return 'first'
    elif num == 2:
        return 'second'
    elif num == 3:
        return 'third'
    elif num == 4:
        return 'fourth'
    elif num == 5:
        return 'fifth'
    elif num == 6:
        return 'sixth'
    elif num == 7:
        return 'seventh'
    elif num == 8:
        return 'eighth'
    elif num == 9:
        return 'ninth'
    elif num == 10:
        return 'tenth'
    elif num == 11:
        return 'eleventh'
    elif num == 12:
        return 'twelfth'


if __name__ == '__main__':
    print(f'{number_to_ordinal(number).capitalize()} is ordinal number of {number}\n')

    for n in range(1, 13):
        print(f'{number_to_ordinal(n).capitalize()} is ordinal number of {n}')

