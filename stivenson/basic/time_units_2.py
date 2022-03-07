amount_of_seconds = int(input('Enter the amount of seconds:\n'))

days_quantity = amount_of_seconds // 86400
rest_amount_of_seconds = amount_of_seconds % 86400

hours_quantity = rest_amount_of_seconds // 3600
rest_amount_of_seconds %= 3600

minutes_quantity = rest_amount_of_seconds // 60
rest_amount_of_seconds %= 60

seconds_quantity = rest_amount_of_seconds

print(f'Duration: {days_quantity}:{hours_quantity:02d}:{minutes_quantity:02d}:{seconds_quantity:02d}')
