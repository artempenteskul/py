bill = float(input('Enter the sum from your bill: '))

tax_amount = bill * 0.2
tips_amount = (bill - tax_amount) * 0.18

overall_bill = bill + tips_amount

print(f'Bill: {bill:.2f}$\n'
      f'Tax amount: {tax_amount:.2f}\n'
      f'Tips amount {tips_amount:.2f}\n'
      f'Overall bill: {overall_bill:.2f}')
