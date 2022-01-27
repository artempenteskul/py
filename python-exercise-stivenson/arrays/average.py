num = input('Enter the first number or press ENTER to exit: ')

nums = []

while num != '':
    num = float(num)
    nums.append(num)
    num = input('Enter next number or press ENTER to exit: ')

avg_num = sum(nums) / len(nums)

more_than_avg_nums = []
less_than_avg_nums = []
equal_to_avg_nums = []

for num in nums:
    if num > avg_num:
        more_than_avg_nums.append(num)
    elif num < avg_num:
        less_than_avg_nums.append(num)
    elif num == avg_num:
        equal_to_avg_nums.append(num)


print('-' * 20)
print(f'AVG NUM: {avg_num}')
print('-' * 20)
print(f'MORE THAN AVG NUM LIST: {more_than_avg_nums}')
print('-' * 20)
print(f'LESS THAN AVG NUM LIST: {less_than_avg_nums}')
print('-' * 20)
print(f'EQUAL TO AVG NUM LIST: {equal_to_avg_nums}')
print('-' * 20)
