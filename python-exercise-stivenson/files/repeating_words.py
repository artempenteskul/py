import sys

if len(sys.argv) != 2:
    print('You should enter file name as second argument')
    exit()

repeating_words = []

try:
    file = open(sys.argv[1], 'r')
    lines = file.read()
    lines = lines.split('.')
    lines = [line.replace('\n', ' ') for line in lines]
    file.close()
    for sentence in lines:
        splitted_sentence = sentence.split()
        for word in splitted_sentence:
            if splitted_sentence.count(word) > 1:
                repeating_words.append(word)
    file.close()
except IOError:
    print('Error while file reading')
    exit()


print(f'Repeating words: {set(repeating_words)}')
