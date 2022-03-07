a = float(input('Enter the length of the first side of the triangle: '))
b = float(input('Enter the length of the second side of the triangle: '))
c = float(input('Enter the length of the third side of the triangle: '))


if a == b and b == c:
    print('This is equilateral triangle')
elif a == b or b == c or a == c:
    print('This is isosceles triangle')
else:
    print('This is versatile triangle')
