day = int(input('Enter the day of the holiday: '))
month = input('Enter the month of the holiday: ')

if day == 1 and month.lower() == 'january':
    print('It\'s the day of the New Year!')
elif day == 1 and month.lower() == 'july':
    print('It\'s the Canada Day!')
elif day == 25 and month.lower() == 'december':
    print('It\'s the day of the Christmas!')
else:
    print('There is not official holiday on this day in Canada')
