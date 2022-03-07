users_operator = input('Enter the operator: ')


def precedence(operator: str):
    if operator in ('+', '-'):
        return 1
    elif operator in ('/', '*'):
        return 2
    elif operator == '^':
        return 3
    else:
        return -1


if __name__ == '__main__':
    print(f'The priority of the operator is {precedence(operator=users_operator)}')
