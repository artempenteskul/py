from random import randint

lottery_numbers = []

while len(lottery_numbers) != 6:
    num = randint(1, 49)
    if num not in lottery_numbers:
        lottery_numbers.append(num)

lottery_numbers.sort()

print(f'Your lottery numbers: {lottery_numbers}')
