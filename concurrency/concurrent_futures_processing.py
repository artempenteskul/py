import time
import concurrent.futures


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)')
    time.sleep(seconds)
    return f'Done sleeping {seconds}'


if __name__ == '__main__':

    start_time = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        results = [executor.submit(do_something, sec) for sec in secs]
        for p in concurrent.futures.as_completed(results):
            print(p.result())

    end_time = time.perf_counter()

    print(f'Time spent: {end_time - start_time:.2f} second(s)')
