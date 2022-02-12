import sys

NUM_LINES = 10

if len(sys.argv) != 2:
    print('You should give name of the file as an second argument')
    exit()

file_name = sys.argv[1]

file = None

try:
    file = open(file_name, 'r')
    line = file.readline()
    count = 0

    while count < NUM_LINES and line != '':
        line = line.strip()
        print(line)
        count += 1
        line = file.readline()

except IOError:
    print('Error while file reading')
    exit()
finally:
    file.close()
