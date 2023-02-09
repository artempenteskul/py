import sys

from datetime import datetime


TIMESTAMP = 1675847985.745177

if __name__ == '__main__':
    timestamp = float(sys.argv[1]) if len(sys.argv) > 1 else TIMESTAMP
    print(datetime.fromtimestamp(timestamp))
