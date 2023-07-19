numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 10:
        print('else block will not be executed')
        break
else:
    print('invocation of else block in for loop')


print()
print('=====')
print()


for num in numbers:
    if num == 5:
        print('else block will not be executed')
        break
else:
    print('invocation of else block in for loop')
