from random import randint

OLD_FORMAT = 1
NEW_FORMAT = 2

A_LETTER_ASCII = 65
Z_LETTER_ASCII = 90

ZERO_NUM_ASCII = 48
NINE_NUM_ASCII = 57


def random_car_sign():
    car_sign = ''
    sign_format = randint(1, 2)
    if sign_format == OLD_FORMAT:
        for i in range(3):
            car_sign += chr(randint(A_LETTER_ASCII, Z_LETTER_ASCII))
        for i in range(3):
            car_sign += chr(randint(ZERO_NUM_ASCII, NINE_NUM_ASCII))
        return car_sign
    elif sign_format == NEW_FORMAT:
        for i in range(4):
            car_sign += chr(randint(ZERO_NUM_ASCII, NINE_NUM_ASCII))
        for i in range(3):
            car_sign += chr(randint(A_LETTER_ASCII, Z_LETTER_ASCII))
        return car_sign
    return 'Something went wrong'


if __name__ == '__main__':
    for j in range(10):
        print(random_car_sign())
