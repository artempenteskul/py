import datetime


d = int(input('Enter the day: '))
m = int(input('Enter the month: '))
y = int(input('Enter the year: '))

first_date_of_year = datetime.date(day=1, month=1, year=y)
first_date_of_year = first_date_of_year.toordinal()


def to_ordinal(day, month, year):
    users_date = datetime.date(day=day, month=month, year=year)
    users_ordinal_date = users_date.toordinal()
    return users_ordinal_date


needed_ordinal_date = to_ordinal(day=d, month=m, year=y)

current_day_number = needed_ordinal_date - first_date_of_year
print(f'Your date is {current_day_number} in the the {y} year')
