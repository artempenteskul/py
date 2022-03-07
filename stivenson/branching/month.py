month = input('Enter the month: ')

months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
          'september', 'october', 'november', 'december']

months_31_days = ['january', 'march', 'may', 'july', 'august', 'october', 'december']
months_30_days = ['april', 'june', 'september', 'november']

if month.lower() in months_31_days:
    print('This month has 31 days!')
elif month.lower() == 'february':
    print('This month has 28 or 29 days')
elif month.lower() in months_30_days:
    print('This month has 30 days!')
else:
    print('This is not a name of month. Try again!')
