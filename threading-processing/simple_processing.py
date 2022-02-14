import time
import multiprocessing


def do_something(seconds):
    print(f'Sleeping {seconds} seconds(s)')
    time.sleep(seconds)
    print('Done sleeping')


if __name__ == '__main__':

    start_time = time.perf_counter()

    processes = []

    for _ in range(10):
        p = multiprocessing.Process(target=do_something, args=(1.5,))
        p.start()
        processes.append(p)

    for process in processes:
        process.join()

    end_time = time.perf_counter()

    print(f'Time spent: {end_time - start_time:.2f} second(s)')
