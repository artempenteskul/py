height = int(input('Enter your height in sm:\n'))
weight = int(input('Enter your weight in kg:\n'))

height_in_metres = height / 100

body_mass_index = weight / pow(height_in_metres, 2)

print(f'Your body index is: {body_mass_index:.2f}')
