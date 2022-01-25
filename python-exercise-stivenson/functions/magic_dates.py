from days_quantity import days_quantity


def is_magic_date(d, m, y):
    if d * m == y % 100:
        return True
    return False


if __name__ == '__main__':
    for year in range(1900, 2000):
        for month in range(1, 13):
            for day in range(1, days_quantity(month=month, year=year) + 1):
                if is_magic_date(d=day, m=month, y=year):
                    print(f'{day}/{month}/{year} is a magic date')

