fts = int(input('Enter how tall in fts you are:\n'))
inches = int(input('And enter inches:\n'))

height_in_inches = inches + fts * 12
height_in_sm = height_in_inches * 2.54

print(f'You height in sm is: {height_in_sm:.2f}')
