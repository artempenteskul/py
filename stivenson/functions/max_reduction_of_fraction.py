def reduction_of_fraction(n, m):
    if n == 0 and m != 0:
        return 0
    elif m == 0:
        return Exception('Zero Division Error')

    d = min(n, m)

    while n % d != 0 or m % d != 0:
        d -= 1
    n //= d
    m //= d

    return n, m


if __name__ == '__main__':
    numerator = int(input('Enter numerator of the fraction: '))
    denominator = int(input('Enter denominator of the fraction: '))

    print(reduction_of_fraction(n=numerator, m=denominator))

