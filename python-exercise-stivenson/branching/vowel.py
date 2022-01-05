char = input('Enter the char: ')

if len(char) > 1:
    print('Too many symbols, try again')
elif char.lower() in ('a', 'e', 'i', 'o', 'u'):
    print('You typed vowel char!')
elif char.lower() == 'y':
    print('You typed y symbol!')
else:
    print('You typed not vowel symbol or number')
