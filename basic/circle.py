import fractions
from math import pi

radius = float(input('Enter the radius in sm:\n'))

area = pi * pow(radius, 2)
volume = fractions.Fraction(4, 3) * pi * pow(radius, 3)

print(f'Radius is: {radius} sm\n'
      f'Area is: {area:.2f}\n'
      f'Volume is {volume:.2f}')
