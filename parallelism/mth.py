# multithreading example in python

import time
import threading as th


def func(data: str) -> None:
    print(f'data - {data}')
    time.sleep(2)  # here should be something like http call


if __name__ == '__main__':
    start = time.time()

    th1 = th.Thread(target=func, args=('text', ))
    th2 = th.Thread(target=func, args=('text', ))
    th3 = th.Thread(target=func, args=('text', ))

    # start three threads (on time.sleep() gil is not blocked and return the control to main thread)
    for t in (th1, th2, th3):
        t.start()

    # waiting for threads to end the work
    for t in (th1, th2, th3):
        t.join()

    end = time.time()

    print(end - start)
