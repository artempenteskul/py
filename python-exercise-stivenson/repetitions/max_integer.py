from random import randrange

max_number = randrange(1, 101)
print(f'{max_number} - start max number')

numbers_list = []

for i in range(100):
    numbers_list.append(randrange(1, 101))

for i in numbers_list:
    if i > max_number:
        max_number = i
        print(f'{i} - new max number')
    else:
        print(i)
