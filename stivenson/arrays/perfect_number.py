def own_divisors(num: int):
    divisors = []
    if num > 0:
        divisors = [x for x in range(1, num) if num % x == 0]
    elif num == 0:
        exit()
        return Exception('Your number is 0, so it\'s inappropriate for the program')
    elif num < 0:
        exit()
        return Exception('Your number is negative, so it\'s inappropriate for the program')
    return divisors


def is_perfect_num(num: int, divisors: list):
    sum_of_divisors = sum(divisors)
    return True if num == sum_of_divisors else False


if __name__ == '__main__':
    n = int(input('Enter num in order to know its perfectness: '))
    print(f'{n} is perfect number: {is_perfect_num(num=n, divisors=own_divisors(num=n))}')
