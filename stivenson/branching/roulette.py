from random import randrange

value = randrange(0, 38)

red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black_numbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

if value == 37:
    print('Drawn number: 00')
else:
    print(f'Drawn number: {value}')

if value == 37:
    print('Winning bet: 00')
else:
    print(f'Winning bet: {value}')

if value in red_numbers:
    print('Winning bet: red')
elif value in black_numbers:
    print('Winning bet: black')
elif value == 0:
    print('Winning bet: green (0)')
elif value == 37:
    print('Winning bet: green (00)')

if value % 2 == 0 and value != 0:
    print('Winning bet: even')
elif value % 2 != 0 and value != 37:
    print('Winning bet: odd')
elif value == 0:
    print('It\'s not odd or even. It\'s 0')
elif value == 37:
    print('It\'s not odd or even. It\'s 00')

if 1 <= value <= 18:
    print('Winning bet: from 1 to 18')
elif 19 <= value <= 36:
    print('Winning bet: from 19 to 36')
elif value == 0:
    print('Winning bet: 0')
elif value == 37:
    print('Winning bet: 00')
