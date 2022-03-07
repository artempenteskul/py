def count_range(arr: list, min_value: [int, float], max_value: [int, float]):

    if min_value > max_value:
        raise Exception('Min value should be lower than max value')

    suitable_elements = []
    for num in arr:
        if min_value <= num <= max_value:
            suitable_elements.append(num)
    quantity = len(suitable_elements)
    return quantity


if __name__ == '__main__':
    num = input('Enter the first num of the sequence or press ENTER to exit: ')
    nums = []
    while num != '':
        num = float(num)
        nums.append(num)

        num = input('Enter next num of the sequence or press ENTER to exit: ')

    min_value = float(input('Enter min value of the range: '))
    max_value = float(input('Enter max value of the range: '))

    print(f'Quantity of the suitable elements: {count_range(arr=nums, min_value=min_value, max_value=max_value)}')
