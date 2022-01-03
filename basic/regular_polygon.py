from math import pi, tan


side_length = float(input('Enter the side length in sm:\n'))
side_quantity = int(input('Enter side quantity:\n'))

area = side_quantity * pow(side_length, 2) / 4 * tan(pi / side_quantity)

print(f'The regular polygon area is {area:.2f} square sm')
