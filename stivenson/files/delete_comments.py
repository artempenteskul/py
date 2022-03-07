from_file_name = input('Enter name of the file from where comments should be deleted: ')
to_file_name = input('Enter name of the file to where new data should be stored: ')

try:
    from_file = open(from_file_name, 'r')
    to_file = open(to_file_name, 'w')
    for line in from_file:
        if not line.startswith('#'):
            to_file.write(line)
    from_file.close()
    to_file.close()
except IOError:
    print('Error while reading or writing into file')
    exit()

print('File was successful rewritten without comments')
