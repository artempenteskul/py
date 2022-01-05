change_in_cents = int(input('Please enter the amount of change in cents:\n'))


toonies_quantity = change_in_cents // 200
rest_change = change_in_cents % 200

loonies_quantity = rest_change // 100
rest_change %= 100

cents_25_quantity = rest_change // 25
rest_change %= 25

cents_10_quantity = rest_change // 10
rest_change %= 10

cents_5_quantity = rest_change // 5
rest_change %= 5

cent_1_quantity = rest_change // 1


print(f'Change in cents: {change_in_cents}\n'
      f'Toonies: {toonies_quantity}\n'
      f'Loonies: {loonies_quantity}\n'
      f'25 Cent Coins: {cents_25_quantity}\n'
      f'10 Cent Coins: {cents_10_quantity}\n'
      f'5 Cent Coins: {cents_5_quantity}\n'
      f'1 Cent Coins: {cent_1_quantity}')
