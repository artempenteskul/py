def interact():
    print('hello stream world')  # sys.stdout
    while True:
        try:
            reply = input('enter a num: ')  # sys.stdin
        except EOFError:
            break
        else:
            num = int(reply)
            print(f'{num} squared is {num ** 2}')
    print('bye')

# sys.stderr for errors


if __name__ == '__main__':
    interact()
