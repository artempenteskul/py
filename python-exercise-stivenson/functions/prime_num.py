def is_prime_num(num: int):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
        else:
            return True


if __name__ == '__main__':
    possible_simple_num = int(input('Enter possible simple number: '))
    print(is_prime_num(num=possible_simple_num))
