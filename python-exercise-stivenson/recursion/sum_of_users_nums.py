def users_total_sum():
    num = input('Enter your number or press ENTER to get the sum: ')

    if num == '':
        return 0

    return float(num) + users_total_sum()


print(f'Sum of your numbers: {users_total_sum()}')
