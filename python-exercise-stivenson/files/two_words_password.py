from random import choice


file_name = input('Enter name of the file where words are stored: ')

words = []

try:
    file = open(file_name, 'r')
    for line in file:
        if 3 <= len(line) < 7:
            words.append(line.rstrip())
    file.close()
except IOError:
    print('Error while reading file with words')
    exit()

first_word = choice(words)
first_word = first_word.capitalize()

password = first_word

while len(password) < 8 or len(password) > 10:
    second_word = choice(words)
    second_word = second_word.capitalize()
    password = first_word + second_word

print(f'Your random password from two words from the file: {password}')
