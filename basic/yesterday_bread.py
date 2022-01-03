bread_quantity = int(input('Enter bread quantity you have bought:\n'))

price = 3.49
sale_price = 3.49 * 0.6

print(f'Bread quantity: {bread_quantity}\n'
      f'Regular price: {bread_quantity * price:.2f} dollars\n'
      f'Sale price: {bread_quantity * sale_price:.2f} dollars\n'
      f'Saved: {bread_quantity * price - bread_quantity * sale_price:.2f} dollars')
