list_of_prices = [4.95, 9.95, 14.95, 19.95, 24.95]

table_of_prices = []

for price in list_of_prices:
    price_with_discount = price * 0.60
    price_difference = price - price_with_discount
    table_of_prices.append((price, price_difference, price_with_discount))


for price, price_difference, price_with_discount in table_of_prices:
    print(f'Old price: {price:.2f}\n'
          f'Price difference: {price_difference:.2f}\n'
          f'Price with discount: {price_with_discount:.2f}\n\n')
