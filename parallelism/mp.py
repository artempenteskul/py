# multiprocessing example in python

import time
import math
import multiprocessing as mp


results_a = []
results_b = []
results_c = []


def make_calculation_one(numbers: list) -> None:
    for num in numbers:
        results_a.append(math.sqrt(num ** 5))
        pow(num, 1000)

    print(len(results_a))


def make_calculation_two(numbers: list) -> None:
    for num in numbers:
        results_b.append(math.sqrt(num ** 6))
        pow(num, 1000)

    print(len(results_b))


def make_calculation_three(numbers: list) -> None:
    for num in numbers:
        results_c.append(math.sqrt(num ** 7))
        pow(num, 1000)

    print(len(results_c))


if __name__ == '__main__':
    """
    this __main__ works without spamming processes
    """

    numbers_list = list(range(1_000_000))

    start = time.time()

    make_calculation_one(numbers_list)
    make_calculation_two(numbers_list)
    make_calculation_three(numbers_list)

    end = time.time()

    print(end - start)


if __name__ == '__main__':
    """
    this __main__ works with spamming three additional processes and counting in parallel
    """

    numbers_list = list(range(1_000_000))

    p1 = mp.Process(target=make_calculation_one, args=(numbers_list, ))
    p2 = mp.Process(target=make_calculation_two, args=(numbers_list,))
    p3 = mp.Process(target=make_calculation_three, args=(numbers_list, ))

    start = time.time()

    for p in (p1, p2, p3):
        p.start()

    for p in (p1, p2, p3):
        p.join()

    end = time.time()

    print(end - start)
