number = input('Enter the sum in order to know the sum of the digits:\n')

sum_of_digits = 0
for num in number:
    sum_of_digits += int(num)

print(f'Sum of digits is {sum_of_digits}')
