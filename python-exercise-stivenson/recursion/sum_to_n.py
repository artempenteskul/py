num = int(input('Enter the number: '))


def sum_to(n):
    if n == 0:
        return 0
    return n + sum_to(n - 1)


print(f'Sum of the values to {num}: {sum_to(n=num)}')
