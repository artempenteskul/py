from math import acos, sin, cos, radians

a_width = radians(float(input('Enter the width of the A:\n')))
a_length = radians(float(input('Enter the length of the A:\n')))

b_width = radians(float(input('Enter the width of the B:\n')))
b_length = radians(float(input('Enter the length of the B:\n')))


distance = 6371.01 * acos(sin(a_width) * sin(b_width) + cos(a_width) * cos(b_width) * cos(a_length - b_length))
print(f'The distance between A and B is: {distance:.4f} kilometres')
