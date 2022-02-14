import threading
import time

start_time = time.perf_counter()


def do_something(seconds):
    print('Start sleeping')
    time.sleep(seconds)
    print('Done sleeping')


threads = []

for _ in range(10):
    t = threading.Thread(target=do_something, args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

print('Threads are closed')

end_time = time.perf_counter()

print(f'Time spent: {end_time - start_time:.2f} seconds')
