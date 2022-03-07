def format_list(items: list):
    if len(items) == 0:
        return 'Empty list'
    elif len(items) == 1:
        return str(items[0])
    elif len(items) > 1:
        res = ''
        for i in range(len(items) - 2):
            res += f'{items[i]}, '
        res += f'{items[-2]} and '
        res += f'{items[-1]}.'
        return res


if __name__ == '__main__':
    element = input('Enter first element of the list or press ENTER to exit: ')
    elements = []

    while element != '':
        elements.append(element)
        element = input('Enter next element of the list or press ENTER to exit: ')

    print(format_list(items=elements))
