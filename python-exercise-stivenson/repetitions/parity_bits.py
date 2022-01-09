bits = input('Enter 8 bits of information or "" to exit: ')

while bits != '':
    if bits.count('0') + bits.count('1') != 8 or len(bits) != 8:
        print('Something went wrong. Try again')
    else:
        ones = bits.count('1')
        if ones % 2 == 0:
            print('Parity bit should have value 0')
        else:
            print('Parity bit should have value 1')

    bits = input('Enter 8 bits of information or "" to exit: ')
