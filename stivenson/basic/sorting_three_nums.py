a = int(input('Enter first number:\n'))
b = int(input('Enter second number:\n'))
c = int(input('Enter third number:\n'))

sum_of_numbers = a + b + c

max_number = max(a, b, c)
min_number = min(a, b, c)
middle_number = sum_of_numbers - max_number - min_number

print(f'Min number: {min_number}\n'
      f'Middle number: {middle_number}\n'
      f'Max number: {max_number}')
