year = int(input('Enter the year: '))

is_leap = False

if year % 400 == 0:
    is_leap = True
elif year % 100 == 0:
    is_leap = True
elif year % 4 == 0:
    is_leap = True
else:
    is_leap = False

if is_leap:
    print(f'{year} is leap!')
else:
    print(f'{year} isn\'t leap!')
