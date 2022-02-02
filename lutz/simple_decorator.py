def wrapper(func):
    def inner():
        print('it\'s decorator start')
        func()
        print('it\'s decorator end')
    return inner


@wrapper
def print_hello():
    print('hello world')


if __name__ == '__main__':
    print_hello()
