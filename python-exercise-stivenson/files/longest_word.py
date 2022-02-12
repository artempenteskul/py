file_name = input('Enter name of the file in order to get longest words of the file: ')

longest_word = ''
longest_words = []

try:
    file = open(file_name, 'r')
    for line in file:
        for word in line.split():
            if len(word) > len(longest_word):
                longest_word = word
                longest_words = [word]
            elif len(word) == len(longest_word):
                longest_words.append(word)
    file.close()
except IOError:
    print('Error while file reading')
    exit()

print(f'Length of the longest word of the file: {len(longest_word)}')
print(f'Longest words list: {longest_words}')
