import sys

if len(sys.argv) < 2:
    print('You should enter one or more argument to run following program')
    exit()

file_names = sys.argv[1:len(sys.argv)]

for file_name in file_names:
    try:
        file = open(file_name, 'r')
        for line in file:
            print(line.rstrip())
        file.close()
    except IOError:
        print(f'Error while file reading ({file_name})')
        exit()
