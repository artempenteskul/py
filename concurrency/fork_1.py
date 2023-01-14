import os


def child():
    print('Hello from child!', os.getgid())
    os._exit(0)


def parent():
    while True:
        new_pid = os.fork()
        if new_pid == 0:
            child()
        else:
            print('Hello from parent', os.getgid(), new_pid)
        if input() == 'q':
            break


parent()
