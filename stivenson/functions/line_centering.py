line = input('Enter the text you want to center: ')
w = int(input('Enter the width of the window: '))


def line_centering(s: str, width: int):
    if len(s) >= width:
        return s
    spaces = (width - len(s)) // 2
    result = ' ' * spaces + s
    return result


if __name__ == '__main__':
    print(line_centering(s=line, width=w))
