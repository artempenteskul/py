deposit_sum = float(input('Enter the sum of the deposit: '))
percent = 0.04

deposit_sum_after_year = deposit_sum * percent + deposit_sum
deposit_sum_after_two_years = deposit_sum_after_year * percent + deposit_sum_after_year
deposit_sum_after_three_years = deposit_sum_after_two_years * percent + deposit_sum_after_two_years

print(f'Deposit sum: {deposit_sum:.2f}$\n'
      f'Deposit sum after 1 year: {deposit_sum_after_year:.2f}$\n'
      f'Deposit sum after 2 years: {deposit_sum_after_two_years:.2f}$\n'
      f'Deposit sum after 3 years: {deposit_sum_after_three_years:.2f}$')
