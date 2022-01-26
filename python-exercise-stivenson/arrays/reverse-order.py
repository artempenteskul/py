num = float(input('Enter num for the list or 0 to exit: '))

nums = []

while num != 0:
    nums.append(num)
    num = float(input('Enter next num or 0 to exit: '))

nums.sort(reverse=True)

print(f'Reversed list: {nums}')
