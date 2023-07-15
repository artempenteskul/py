# synchronous code

import time


def print1():
    print(1)


def print2():
    time.sleep(10)
    print(2)


def print3():
    print(3)


def main():
    start_time = time.time()
    print1()
    print2()
    print3()
    print(f'{time.time() - start_time:.2f} seconds')


if __name__ == '__main__':
    main()
