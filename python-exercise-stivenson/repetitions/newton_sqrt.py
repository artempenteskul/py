x = int(input('Enter the number to get sqrt from this number by Newton method: '))
approximation = int(input('Enter the level of the approximation: '))
guess = x / 2


for i in range(approximation):
    print(guess)
    guess = (guess + x / guess) / 2
