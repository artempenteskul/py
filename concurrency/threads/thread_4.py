# this script ends only when all threads will be finished

import _thread

stdout_mutex = _thread.allocate_lock()
exit_mutes = []


def counter(th_id, count):
    for i in range(count):
        stdout_mutex.acquire()
        print(f'{th_id} => {i}')
        stdout_mutex.release()
    exit_mutes[th_id] = True


for j in range(10):
    exit_mutes.append(False)
    _thread.start_new_thread(counter, (j, 6))


while False in exit_mutes:
    pass

print('Main thread exiting.')
