possible_integer = input('Enter the number you want to check: ')


def is_integer(str_number: str):
    if str_number[0] == '+' or str_number[0] == '-':
        str_number = str_number[1:]

    for i in str_number:
        if i in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            str_number += i
        else:
            return False

    return True


if __name__ == '__main__':
    print(is_integer(possible_integer))
