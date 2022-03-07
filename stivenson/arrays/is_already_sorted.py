num = input('Enter first num of the sequence or press ENTER to exit: ')

nums = []

while num != '':
    num = float(num)
    nums.append(num)
    num = input('Enter next num of the sequence or press ENTER to exit: ')


def is_reversed(arr: list):
    sorted_arr = list(sorted(arr))
    reversed_sorted_arr = list(sorted(arr, reverse=True))

    if arr == sorted_arr:
        return True
    elif arr == reversed_sorted_arr:
        return True
    return False


if __name__ == '__main__':
    print(f'Was it sorted: {is_reversed(arr=nums)}')
