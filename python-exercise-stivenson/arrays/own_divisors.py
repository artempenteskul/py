def own_divisors(num: int):
    divisors = []
    if num > 0:
        for x in range(-num, num):
            if x == 0:
                continue
            elif num % x == 0:
                divisors.append(x)
    elif num < 0:
        for x in range(num + 1, -num + 1):
            if x == 0:
                continue
            elif num % x == 0:
                divisors.append(x)
    elif num == 0:
        return Exception('Your num is zero!')
    return divisors


if __name__ == '__main__':
    number = int(input('Enter number in order to know all its divisors: '))
    print(f'Divisors of {number} are: {own_divisors(num=number)}')
