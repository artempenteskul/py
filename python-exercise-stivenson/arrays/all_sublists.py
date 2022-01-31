def possible_sub_lists(original_list: list):
    all_sub_lists = [[]]
    for length in range(1, len(original_list) + 1):
        for i in range(0, len(original_list) - length + 1):
            all_sub_lists.append(original_list[i:i+length])
    return all_sub_lists


if __name__ == '__main__':

    num = input('Enter the first num of the sequence or press ENTER to exit: ')
    nums = []

    while num != '':
        num = int(num)
        nums.append(num)
        num = input('Enter next num of the sequence or press ENTER to exit: ')

    print(f'All possible sub lists of your list: {possible_sub_lists(original_list=nums)}')
