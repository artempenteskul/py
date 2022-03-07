import sys

if len(sys.argv) != 2:
    print('You should enter file name as a second argument')
    exit()

words_dictionary = {'yes', 'no'}

file_name = sys.argv[1]

counter_checked = 0
counter_not_checked = 0

try:
    file = open(file_name, 'r')
    for line in file:
        words_list = line.split()
        for word in words_list:
            if word not in words_dictionary:
                counter_not_checked += 1
            elif word in words_dictionary:
                counter_checked += 1
    file.close()
except IOError:
    print('Error while file reading')
    exit()

print(f'Quantity of checked words: {counter_checked}')
print(f'Quantity of not checked words: {counter_not_checked}')
