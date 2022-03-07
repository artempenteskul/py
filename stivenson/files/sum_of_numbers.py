num = input('Enter the first num or press ENTER to exit: ')

res = 0

while num != '':
    try:
        num = float(num)
        res += num
        num = input('Enter the first num or press ENTER to exit: ')
    except ValueError:
        print('Error while last number adding')
        num = input('Enter the first num or press ENTER to exit: ')

print(f'Sum of all numbers: {res}')
