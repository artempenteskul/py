month = input('Enter the month: ').lower()
day = int(input('Enter the day: '))

season = ''

if month == 'january' or month == 'february':
    season = 'winter'
elif month == 'march' and 1 <= day < 20:
    season = 'winter'
elif month == 'march' and 20 <= day <= 31:
    season = 'spring'
elif month == 'april' or month == 'may':
    season = 'spring'
elif month == 'june' and 1 <= day < 21:
    season = 'spring'
elif month == 'june' and 21 <= day <= 30:
    season = 'summer'
elif month == 'july' or month == 'august':
    season = 'summer'
elif month == 'september' and 1 <= day < 22:
    season = 'summer'
elif month == 'september' and 22 <= day <= 30:
    season = 'autumn'
elif month == 'october' or month == 'november':
    season = 'autumn'
elif month == 'december' and 1 <= day < 21:
    season = 'autumn'
elif month == 'december' and 21 <= day <= 31:
    season = 'winter'

if season:
    print(f'Your day is in {season.upper()} season!')
else:
    print('You entered something incorrect')
