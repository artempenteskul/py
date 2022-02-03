postal_codes = {
    'Newfoundland': ['A'], 'Nova Scotia': ['B'], 'Prince Edward Island': ['C'],
    'New Brunswick': ['E'], 'Quebec': ['G', 'H', 'J'], 'Ontario': ['K', 'L', 'M', 'N', 'P'],
    'Manitoba': ['R'], 'Saskatchewan': ['S'], 'Alberta': ['T'], 'British Columbia': ['V'],
    'Nunavut': ['X'], 'Northwest Territories': ['X'], 'Yukon': 'Y',
}


def canadian_place_by_post_code(code: str):

    if len(code) != 6:
        return 'You entered incorrect postal code for the Canada'

    if not code[0].isalpha():
        return 'You entered incorrect postal code for the Canada, first char should be alpha'
    elif not code[1].isdigit():
        return 'You entered incorrect postal code for the Canada, second char should be digit'

    place = ''

    for place in postal_codes:
        if code[0].upper() in postal_codes[place] and code[0].upper() == 'X':
            place = 'Nunavut or Northwest Territories'
            break
        elif code[0].upper() in postal_codes[place]:
            place = place
            break

    location = ''

    if int(code[1]) == 0:
        location = 'countryside'
    elif int(code[1]) > 0:
        location = 'city'

    return place, location


if __name__ == '__main__':
    users_postal_code = input('Enter your postal code: ')
    users_place, users_location = canadian_place_by_post_code(code=users_postal_code)
    print(f'Your postal code: {users_postal_code}\n'
          f'Place in Canada: {users_place}\n'
          f'Location: {users_location}')
