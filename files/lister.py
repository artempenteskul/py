import os
import sys


def lister(current_dir):
    print(f' --- {current_dir} --- ')
    for file in os.listdir(current_dir):
        path = os.path.join(current_dir, file)
        if not os.path.isdir(path):
            print(path)
        else:
            lister(path)


if __name__ == '__main__':
    lister(sys.argv[1])
