def fib_numbers(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_numbers(n - 1) + fib_numbers(n - 2)


if __name__ == '__main__':
    num = int(input('Enter index of the desired Fibonacci number: '))
    print(f'Fibonacci number with index {num} is {fib_numbers(n=num)}')
