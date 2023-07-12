def squares(n: int):
    for i in range(n):
        yield i


if __name__ == '__main__':
    gen = squares(5)

    for num in gen:
        print(num)

    print(gen)
