sides_quantity = int(input('Enter the number os sides: '))


if sides_quantity == 1:
    print('Your figure is line!')
elif sides_quantity == 2:
    print('Your figures can be two lines or angle')
elif sides_quantity == 3:
    print('Your figure is triangle')
elif sides_quantity == 4:
    print('Your figures can be square or rectangle')
elif sides_quantity == 5:
    print('Your figure is pentagon')
elif sides_quantity <= 0:
    print('An error occurred. I do\'nt know the figure with 0 or less sides')
else:
    print('Your figure has 6 or more sides')
