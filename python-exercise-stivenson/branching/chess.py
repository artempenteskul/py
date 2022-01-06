chess_cell = input('Enter the cell whose color you want to know: ')

starts_with_white = ['b', 'd', 'f', 'h']
starts_with_black = ['a', 'c', 'e', 'g']

chess_cell_char = chess_cell[0].lower()
chess_cell_number = int(chess_cell[1])

if chess_cell_char in starts_with_white and chess_cell_number % 2 == 0:
    print(f'{chess_cell.upper()} is black!')
elif chess_cell_char in starts_with_white and chess_cell_number % 2 != 0:
    print(f'{chess_cell.upper()} is white!')
elif chess_cell_char in starts_with_black and chess_cell_number % 2 == 0:
    print(f'{chess_cell.upper()} is white!')
elif chess_cell_char in starts_with_black and chess_cell_number % 2 != 0:
    print(f'{chess_cell.upper()} is black!')
else:
    print('There is no such chess cell. Try again!')
