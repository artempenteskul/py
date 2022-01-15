num_1 = int(input('Enter first positive integer number: '))
num_2 = int(input('Enter second positive integer number: '))

d = min(num_1, num_2)

while num_1 % d != 0 or num_2 % d != 0:
    d -= 1

print(f'NSD for {num_1} and {num_2} is: {d}')
