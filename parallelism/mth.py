# multithreading example in python

import time
import random
import threading as th


def func() -> None:
    print(f'RESULT - {random.randint(0, 10)}')
    time.sleep(2)  # here should be something like http call


if __name__ == '__main__':
    """
    this work in sync mode without threads
    """

    start = time.time()

    for i in range(3):
        func()

    end = time.time()

    print(end - start)


if __name__ == '__main__':
    """
    this works by spamming three threads
    """

    start = time.time()

    th1 = th.Thread(target=func)
    th2 = th.Thread(target=func)
    th3 = th.Thread(target=func)

    # start three threads (on time.sleep() gil is not blocked and return the control to other threads)
    for t in (th1, th2, th3):
        t.start()

    # waiting for threads to end the work
    for t in (th1, th2, th3):
        t.join()

    end = time.time()

    print(end - start)
