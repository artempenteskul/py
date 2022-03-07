possible_palindrome = input('Enter the possible palindrome: ')

possible_palindrome_list = list(possible_palindrome)
possible_palindrome_list.reverse()
reversed_possible_palindrome = ''.join(possible_palindrome_list)
reversed_possible_palindrome = reversed_possible_palindrome.replace(' ', '').lower()

possible_palindrome_without_spaces = possible_palindrome.replace(' ', '').lower()

if possible_palindrome_without_spaces == reversed_possible_palindrome:
    print(f'{possible_palindrome} is a palindrome')
else:
    print(f'{possible_palindrome} isn\'t palindrome')
