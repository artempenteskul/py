from random_password import random_password
from password_strength import check_password_strength

times = 1

password_to_check = random_password()

while not check_password_strength(password_to_check):
    times += 1
    password_to_check = random_password()


print(f'{password_to_check} is strong enough to use\n'
      f'It was created from {times} attempts')
