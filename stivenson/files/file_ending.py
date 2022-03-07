import sys

NUM_LINES = 10

if len(sys.argv) != 2:
    print('You should give name of the file as an second argument')
    exit()

lines = []

try:
    file = open(sys.argv[1], 'r')
    for line in file:
        lines.append(line.rstrip())
        if len(lines) > NUM_LINES:
            lines.pop(0)
    file.close()
except IOError:
    print('Error while file reading')
    exit()

for line in lines:
    print(line)
