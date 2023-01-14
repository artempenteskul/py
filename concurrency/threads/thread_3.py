# this script locks the access to the print func (only 1 thread could use print at the time)

import time
import _thread


mutex = _thread.allocate_lock()


def counter(th_id, count):
    for i in range(count):
        time.sleep(1)
        mutex.acquire()
        print(f'{th_id} => {i}')

        mutex.release()


for j in range(5):
    _thread.start_new_thread(counter, (j, 5))

time.sleep(6)
print('Main thread exiting')
