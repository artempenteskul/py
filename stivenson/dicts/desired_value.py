def reverse_lookup(d: dict, value):
    res = [x for x in d if d[x] == value]
    return res


if __name__ == '__main__':
    key = input('Enter the first key of the dict or press ENTER to exit: ')
    dictionary = {}

    while key != '':
        if key.isdigit():
            key = int(key)
        val = input('Enter value for the key: ')
        if val.isdigit():
            val = int(val)
        dictionary[key] = val

        key = input('Enter next key of the dict or press ENTER to exit: ')

    desired_value = input('Enter your desired value: ')
    if desired_value.isdigit():
        desired_value = int(desired_value)

    print(reverse_lookup(d=dictionary, value=desired_value))
