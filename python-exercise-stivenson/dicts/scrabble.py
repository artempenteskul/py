scrabble_points = {
    1: ['A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'],
    2: ['D', 'G'],
    3: ['B', 'C', 'M', 'P'],
    4: ['F', 'H', 'V', 'W', 'Y'],
    5: ['K'],
    8: ['J', 'X'],
    10: ['Q', 'Z']
}


def count_scrabble_points(word: str):
    res = 0
    for symbol in word:
        for point in scrabble_points:
            if symbol.upper() in scrabble_points[point]:
                res += point
                break
    return res


if __name__ == '__main__':
    users_word = input('Enter your word to count the quantity of points you get: ')
    print(f'{count_scrabble_points(word=users_word)} point for the {users_word}')
