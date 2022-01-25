def check_password_strength(password: str):
    has_upper = False
    has_lower = False
    has_num = False

    for i in password:
        if 'A' <= i <= 'Z':
            has_upper = True
        elif 'a' <= i <= 'z':
            has_lower = True
        elif '0' <= i <= '9':
            has_num = True

    if len(password) >= 8 and has_upper and has_lower and has_num:
        return True
    return False


if __name__ == '__main__':
    password_to_check = input('Enter password in order to check its strength: ')
    print(f'Is your password strong enough: {check_password_strength(password_to_check)}')
