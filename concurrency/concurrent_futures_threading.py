import time
import concurrent.futures


start_time = time.perf_counter()


def do_something(seconds):
    print(f'Start {seconds} sleeping')
    time.sleep(seconds)
    return f'Done sleeping ... {seconds}'


with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = [executor.submit(do_something, sec) for sec in secs]
    for f in concurrent.futures.as_completed(results):
        print(f.result())

end_time = time.perf_counter()

print(f'Time spent: {end_time - start_time:.2f} seconds')
