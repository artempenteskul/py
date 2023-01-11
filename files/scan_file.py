import sys


def scanner(filename, function):
    file = open(filename, 'r')
    while True:
        line = file.readline()
        if not line:
            break
        print(function(line))
    file.close()


if __name__ == '__main__':
    scanner(sys.argv[1], str.upper)
