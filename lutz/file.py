FILENAME = 'test.txt'


if __name__ == '__main__':
    file = open(FILENAME, 'w')
    file.write('hello world!\n')
    file.close()
