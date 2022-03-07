def days_quantity(month, year):
    is_leap_year = False
    if year % 4 == 0 or year % 100 == 0 or year % 400 == 0:
        is_leap_year = True

    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month in (4, 6, 9, 11):
        return 30
    elif month == 2 and is_leap_year:
        return 29
    elif month == 2 and not is_leap_year:
        return 28
    return 'Something was typed incorrect'


if __name__ == '__main__':
    m = int(input('Enter month number form 1 to 12: '))
    y = int(input('Enter year in four digit format: '))

    print(f'Quantity of days: {days_quantity(month=m, year=y)}')
