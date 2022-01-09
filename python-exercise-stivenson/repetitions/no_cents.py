amount_of_money = input('Enter the amount of money or '' to exit: ')

total = 0

while amount_of_money != '':
    total += float(amount_of_money)
    amount_of_money = input('Enter the amount of money or '' to exit: ')

print(f'Total sum: {total:.2f}')

total_cash = round(0.05 * round(total / 0.05), 2)

print(f'Total sum in cash: {total_cash:.2f}')
