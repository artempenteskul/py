s = input('Enter the string you want to code or decode by Cesar Code: ')
step = int(input('Enter the step for the code or for the decode: '))

s_coded = ''

for symbol in s:
    if 'a' <= symbol <= 'z':
        pos = ord(symbol) - ord('a')
        pos = (pos + step) % 26
        coded_symbol = chr(pos + ord('a'))
        s_coded += coded_symbol
    elif 'A' <= symbol <= 'Z':
        pos = ord(symbol) - ord('A')
        pos = (pos + step) % 26
        coded_symbol = chr(pos + ord('A'))
        s_coded += coded_symbol
    else:
        s_coded += symbol

print(s_coded)
