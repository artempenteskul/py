word = input('Enter the first word or press ENTER to exit: ')

words = []

while word != '':
    if word not in words:
        words.append(word)
    word = input('Enter next word or press ENTER to exit: ')

for word in words:
    print(word)
