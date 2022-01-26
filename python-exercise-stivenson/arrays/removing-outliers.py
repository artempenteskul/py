num = input('Enter num for the list or press ENTER to exit: ')

nums = []

while num != '':
    nums.append(int(num))
    num = input('Enter next num for the list or press ENTER to exit: ')


def min_max_remove(values_list: list):
    if len(values_list) < 4:
        return Exception('List length is less than 4. You need enter more values')

    min_value = min(values_list)
    max_value = max(values_list)

    values_list_without_outliers = values_list[:]
    values_list_without_outliers.remove(min_value)
    values_list_without_outliers.remove(max_value)

    return values_list_without_outliers


if __name__ == '__main__':
    print(f'Values list with outliers: {nums}\n'
          f'Values list without outliers: {min_max_remove(values_list=nums)}')
