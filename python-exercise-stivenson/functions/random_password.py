import random

MIN_PASSWORD_LENGTH = 7
MAX_PASSWORD_LENGTH = 10

MIN_ASCII = 33
MAX_ASCII = 126


def random_password():
    length = random.randint(MIN_PASSWORD_LENGTH, MAX_PASSWORD_LENGTH)
    password = ''
    for i in range(length):
        password += chr(random.randint(MIN_ASCII, MAX_ASCII))
    return password


if __name__ == '__main__':
    for i in range(5):
        print(random_password())
