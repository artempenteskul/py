from typing import List, Dict, Iterable, Sequence, Union

# variable annotations
y: str = 'hello'


# function annotations
def add_numbers(a: int, b: int, c: int) -> int:
    return a + b + c


# type aliases
Vector = list[float]


def count_vector_sum(lst: Vector) -> float:
    return sum(lst)
