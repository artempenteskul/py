def euclid_nsd(a, b):
    if b == 0:
        return a
    c = a % b
    return euclid_nsd(b, c)


if __name__ == '__main__':
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))

    print(f'Euclid algorithm result for {num1} and {num2} is {euclid_nsd(a=num1, b=num2)}')
