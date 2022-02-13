file_name = input('Enter the name of the file: ')

letters_freq = {}

counter_of_symbols = 0

try:
    file = open(file_name, 'r')
    for line in file:
        for symbol in line:
            if 'A' <= symbol.upper() <= 'Z' and symbol.upper() not in letters_freq.keys():
                letters_freq[symbol.upper()] = 1
                counter_of_symbols += 1
            elif 'A' <= symbol.upper() <= 'Z' and symbol.upper() in letters_freq.keys():
                letters_freq[symbol.upper()] += 1
                counter_of_symbols += 1
    file.close()
except IOError:
    print('Error while file reading')
    exit()


print('*' * 20)
print(f'Quantity of the symbols in the file: {counter_of_symbols}')
print('*' * 20)
for key in letters_freq:
    print(f'Letter {key} frequency: {letters_freq[key] / counter_of_symbols * 100:.2f}%')
