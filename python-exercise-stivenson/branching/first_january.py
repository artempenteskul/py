from math import floor

year = int(input('Enter the year: '))

day_of_the_week = (year + floor((year - 1) / 4) - floor((year - 1) / 100) + floor((year - 1) / 400)) % 7

name_of_the_day_of_week = ''

if day_of_the_week == 0:
    name_of_the_day_of_week = 'sunday'
elif day_of_the_week == 1:
    name_of_the_day_of_week = 'monday'
elif day_of_the_week == 2:
    name_of_the_day_of_week = 'tuesday'
elif day_of_the_week == 3:
    name_of_the_day_of_week = 'wednesday'
elif day_of_the_week == 4:
    name_of_the_day_of_week = 'thursday'
elif day_of_the_week == 5:
    name_of_the_day_of_week = 'friday'
elif day_of_the_week == 6:
    name_of_the_day_of_week = 'saturday'
else:
    name_of_the_day_of_week = ''


if name_of_the_day_of_week:
    print(f'The first January in {year} is on {name_of_the_day_of_week.upper()}!')
else:
    print('Something went wrong. Try again!')
