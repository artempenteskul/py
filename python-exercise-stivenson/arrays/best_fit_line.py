xs = []
ys = []

x = input('Enter x coordinate of the first dot or press ENTER to exit:  ')

while x != '':
    x = float(x)

    xs.append(x)

    y = input('Enter y coordinate of the next dot: ')
    y = float(y)
    ys.append(y)

    x = input('Enter x coordinate of the next dot or press ENTER to exit: ')


def best_line(x_list: list, y_list: list):
    if len(x_list) != len(y_list):
        raise Exception('Length of the lists should be equal')

    avg_x = sum(x_list) / len(x_list)
    avg_y = sum(y_list) / len(y_list)
    n = len(x)

    numer = sum([xi * yi for xi, yi in zip(x_list, y_list)]) - n * avg_x * avg_y
    denum = sum([xi ** 2 for xi in x_list]) - n * avg_x ** 2

    b = numer / denum
    a = avg_y - b * avg_x

    print(f'Best fit line formula:\n'
          f'y = {a:.2f} + {b:.2f}x')

    return a, b


if __name__ == '__main__':
    best_line(x_list=xs, y_list=ys)
