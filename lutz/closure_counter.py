from typing import Callable


def counter(start: int = 0) -> Callable:
    def step():
        nonlocal start
        start += 1
        return start

    return step


if __name__ == '__main__':
    c1 = counter(10)
    c2 = counter()

    print(c1(), c2())
    print(c1(), c2())
    print(c1(), c2())
