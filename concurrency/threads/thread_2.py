import time
import _thread


def counter(th_id, count):
    for j in range(count):
        time.sleep(1)
        print(f'{th_id} => {j}')


for i in range(5):
    _thread.start_new_thread(counter, (i, 5))


# if program ends faster - the thread won't finish their work
time.sleep(6)

print('Main thread exiting')
