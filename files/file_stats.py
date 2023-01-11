import os
import sys

if __name__ == '__main__':
    print(f'File {sys.argv[1]} stats')
    print(os.stat(sys.argv[1]))
