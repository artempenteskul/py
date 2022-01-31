def is_sublist(larger: list, smaller: list):
    if all(x in larger for x in smaller):
        is_true_sub = False
        smaller_len = len(smaller)
        for i in range(len(larger)):
            if larger[i:i+smaller_len] == smaller:
                is_true_sub = True
                break
        return is_true_sub
    else:
        return False


print(is_sublist(larger=[1, 2, 3, 4], smaller=[1, 3]))

if __name__ == '__main__':

    original = input('Enter the first num of the original list or press ENTER to exit: ')
    original_list = []

    while original != '':
        original = float(original)
        original_list.append(original)
        original = input('Enter next num of the original list or press ENTER to exit: ')

    possible_sub = input('Enter the first num of the possible sub list or press ENTER to exit: ')
    possible_sub_list = []

    while possible_sub != '':
        possible_sub = float(possible_sub)
        possible_sub_list.append(possible_sub)
        possible_sub = input('Enter next num of the possible sub list or press ENTER to exit: ')

    print(f'{possible_sub_list} is sub list of {original_list}: {is_sublist(larger=original_list, smaller=possible_sub_list)}')
