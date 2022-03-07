official_word = input('Enter the first official word or press Enter to exit: ')

official_words = []

while official_word != '':
    official_words.append(official_word)
    official_word = input('Enter next official word or press Enter to exit: ')

file_name = input('Enter file name where official words should be replaced with asterisks: ')
new_file_name = input('Enter file name where official text should be stored: ')

try:
    file = open(file_name, 'r')
    new_file = open(new_file_name, 'w')
    line = file.readline()
    while line != '':
        for word in official_words:
            line = line.replace(word, '*' * len(word))
        new_file.write(line)
        line = file.readline()
    file.close()
    new_file.close()
except IOError:
    print('Error while file reading or writing')
    exit()


print(f'Success. Check out your file {new_file_name}')
