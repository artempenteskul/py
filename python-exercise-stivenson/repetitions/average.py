number = int(input('Enter the number to know the average, enter 0 to exit: '))

number_list = []

while number != 0:
    number_list.append(number)
    average = sum(number_list) / len(number_list)
    print(f'The average is {average:.2f}')

    number = int(input('Enter the number to know the average, enter 0 to exit: '))

if len(number_list) == 0:
    raise Exception('Exception message')
