number = int(input('Enter positive integer > 2: '))
entered_number = number

factor = 2

prime_factors = []

if number < 2:
    print('You entered less than 2')
else:
    while factor <= number:
        if number % factor == 0:
            prime_factors.append(factor)
            number //= factor
        else:
            factor += 1

if len(prime_factors) == 0:
    pass
else:
    print(f'Prime factors of the {entered_number}:')
    for prime_factor in prime_factors:
        print(prime_factor)
