phone_calls_minutes = int(input('Enter the overall quantity of phone calls minutes in this month: '))
phone_sms_quantity = int(input('Enter the overall quantity of phone sms in this month: '))

extra_phone_calls_minutes = phone_calls_minutes % 50
extra_phone_sms_quantity = phone_sms_quantity % 50

if phone_calls_minutes < 50:
    extra_phone_calls_minutes = 0

if phone_sms_quantity < 50:
    extra_phone_sms_quantity = 0

sum_for_extra_calls_and_sms = extra_phone_calls_minutes * 0.25 + extra_phone_sms_quantity * 0.15
overall_sum = 15 + sum_for_extra_calls_and_sms + 0.44
tax_amount = overall_sum * 0.05

print(f'Tariff plan: 15$\n'
      f'Sum for extra phone minutes and sms: {sum_for_extra_calls_and_sms:.2f}$\n'
      f'Amount for the 911: 0.44$\n'
      f'Tax amount: {tax_amount:.2f}$\n'
      f'Overall sum: {overall_sum:.2f}$')
