import time
from typing import Callable


def timer(func: Callable):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return result
    return wrapper


@timer
def one(n: int) -> list:
    l = []
    for i in range(n):
        if i % 2 == 0:
            l.append(i)
    return l


@timer
def two(n: int) -> list:
    l = [x for x in range(n) if x % 2 == 0]
    return l


if __name__ == '__main__':
    one(100_000)
    two(100_000)
