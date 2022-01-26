num = float(input('Enter num for the list or enter 0 to exit: '))

nums = []

while num != 0:
    nums.append(num)
    num = float(input('Enter next num for the list or 0 to exit: '))

nums.sort()

print(f'Sorted list: {nums}')
