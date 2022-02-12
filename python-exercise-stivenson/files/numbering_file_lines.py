from_file_name = input('From which file should program take data: ')
to_file_name = input('To which file should program write data: ')


try:
    from_file = open(from_file_name, 'r')
    to_file = open(to_file_name, 'w')
    num = 1
    line = from_file.readline()
    while line != '':
        to_file.write(f'{num}: {line}')
        num += 1
        line = from_file.readline()
    from_file.close()
    to_file.close()
except IOError:
    print('Error while operation with files')
    exit()

print('Program was successfully finished. Check out your files')
