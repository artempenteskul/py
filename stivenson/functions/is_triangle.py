first_side = float(input('Enter the length of the first side: '))
second_side = float(input('Enter the length of the second side: '))
third_side = float(input('Enter the length of the third side: '))


def is_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b > c and b + c > a and c + a > b:
        return True
    else:
        return False


res = is_triangle(a=first_side, b=second_side, c=third_side)

if res:
    print(f'From sides: {first_side} sm, {second_side} sm, {third_side} sm is possible to build triangle')
else:
    print(f'It\'s impossible to build triangle from {first_side} sm, {second_side} sm, {third_side} sm')
