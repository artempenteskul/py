from math import sqrt

height = float(input('Enter the height in metres:\n'))
start_speed = float(input('Enter start speed in km per hour:\n'))

acceleration_of_gravity = 9.8

end_speed = sqrt(pow(start_speed, 2) + 2 * acceleration_of_gravity * height)

print(f'End speed would be: {end_speed:.2f}')
