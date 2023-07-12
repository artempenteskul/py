
def sum_tree(tree: list) -> int:
    total = 0
    
    for item in tree:
        if not isinstance(item, list):
            total += item
        else:
            total += sum_tree(item)
    
    return total


if __name__ == '__main__':
    print(sum_tree([1, [2, [3, 4], 5], 6, [7, 8]]))
