possible_palindrome = input('Enter the possible palindrome: ')

reversed_possible_palindrome = list(reversed(list(possible_palindrome)))
reversed_possible_palindrome = ''.join(reversed_possible_palindrome)

if possible_palindrome == reversed_possible_palindrome and len(possible_palindrome) % 2 == 0:
    print(f'{possible_palindrome} is a palindrome!')
else:
    print(f'{possible_palindrome} is not a palindrome!')
