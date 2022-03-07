num = int(input('Enter the positive integer: '))

nums_list = [num]

if num <= 0:
    print('You entered not a positive integer')
else:
    while nums_list[-1] != 1:
        if nums_list[-1] % 2 == 0:
            nums_list.append(nums_list[-1] // 2)
        else:
            nums_list.append(nums_list[-1] * 3 + 1)

print(nums_list)
