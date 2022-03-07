from math import pi

cylinder_radius = float(input('Enter the radius of the cylinder:\n'))
cylinder_height = float(input('Enter the height of the cylinder:\n'))

circle_area = pi * pow(cylinder_radius, 2)
cylinder_volume = circle_area * cylinder_height

print(f'Cylinder volume is: {cylinder_volume:.1f}')
