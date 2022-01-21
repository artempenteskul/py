first = float(input('Enter first number: '))
second = float(input('Enter second number: '))
third = float(input('Enter third number: '))


def three_values_median(a, b, c):
    three_values_list = [a, b, c]
    three_values_list.sort()
    median = three_values_list[1]
    return median


print(f'The median between ({first}, {second}, {third}) - {three_values_median(first, second, third)}')
