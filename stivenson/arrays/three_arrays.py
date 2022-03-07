num = input('Enter first number or press ENTER to exit: ')

positive_nums = []
negative_nums = []
zero_nums = []

while num != '':
    num = int(num)

    if num < 0:
        negative_nums.append(num)
    elif num > 0:
        positive_nums.append(num)
    elif num == 0:
        zero_nums.append(num)

    num = input('Enter next number or press ENTER to exit: ')

print('--- FINAL ORDER ---\n')

for i in negative_nums:
    print(i)

for i in zero_nums:
    print(i)

for i in positive_nums:
    print(i)
