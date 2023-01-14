import time
import threading


count = 0


def adder(lock):
    global count
    with lock:
        count += 1
    time.sleep(0.5)
    with lock:
        count += 1


add_lock = threading.Lock()
threads = []

for i in range(100):
    thread = threading.Thread(target=adder, args=(add_lock, ))
    thread.start()
    threads.append(thread)

for th in threads:
    th.join()

print(f'GLOBAL COUNT: {count}')
