from prime_num import is_prime_num


def next_prime(prev_prime: int):
    res = is_prime_num(num=prev_prime)
    next_possible_prime = prev_prime + 1
    if res:
        while not is_prime_num(next_possible_prime):
            next_possible_prime += 1
            return next_possible_prime
    else:
        return None


if __name__ == '__main__':
    number = int(input('Enter prime number in order to get the next one: '))
    print(f'Next prime number is {next_prime(prev_prime=number)}')
