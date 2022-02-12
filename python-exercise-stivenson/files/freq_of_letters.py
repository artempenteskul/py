import sys

if len(sys.argv) != 2:
    print('You should enter file name as a second argument')
    exit()

letters_freq = {}

try:
    file = open(sys.argv[1], 'r')
    for line in file:
        for symbol in line:
            if 'A' <= symbol.upper() <= 'Z' and symbol.upper() not in letters_freq.keys():
                letters_freq[symbol.upper()] = 1
            elif 'A' <= symbol.upper() <= 'Z' and symbol.upper() in letters_freq.keys():
                letters_freq[symbol.upper()] += 1
    file.close()
except IOError:
    print('Error while file reading')
    exit()

for letter in letters_freq:
    print(f'{letter} - {letters_freq[letter]}')
