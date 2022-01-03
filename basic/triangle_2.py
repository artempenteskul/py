from math import sqrt

a = float(input('Enter in sm the length of the A:\n'))
b = float(input('Enter in sm the length of the B:\n'))
c = float(input('Enter in sm the length of the C:\n'))

half_perimeter = (a + b + c) / 2
triangle_area = sqrt(half_perimeter * (half_perimeter - a) * (half_perimeter - b) * (half_perimeter - c))

print(f'Triangle area is: {triangle_area:.2f} square sm')
