possible_palindrome = input('Enter the possible palindrome: ')

possible_palindrome = possible_palindrome.lower()
reversed_possible_palindrome = possible_palindrome[::-1]

if possible_palindrome == reversed_possible_palindrome and len(possible_palindrome) % 2 == 0:
    print(f'{possible_palindrome} is a palindrome!')
else:
    print(f'{possible_palindrome} is not a palindrome')
