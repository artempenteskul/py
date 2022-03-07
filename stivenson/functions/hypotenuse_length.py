from math import sqrt

first_side = float(input('Enter first side of the triangle: '))
second_side = float(input('Enter second side of the triangle: '))


def hypotenuse(a, b):
    return sqrt(pow(a, 2) + pow(b, 2))


print(f'Hypotenuse length is: {hypotenuse(a=first_side, b=second_side)} sm')
