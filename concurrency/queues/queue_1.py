import time
import queue
import _thread


NUM_CONSUMERS = 2
NUM_PRODUCERS = 4
NUM_MESSAGES = 4

safe_print = _thread.allocate_lock()
data_queue = queue.Queue()


def producer(id_num):
    for msg_num in range(NUM_MESSAGES):
        time.sleep(id_num)
        data_queue.put(f'[Producer - {id_num} - {msg_num}]')


def consumer(id_num):
    while True:
        time.sleep(0.1)
        try:
            data = data_queue.get(block=False)
        except queue.Empty:
            pass
        else:
            with safe_print:
                print(f'Consumer {id_num} got {data}')


if __name__ == '__main__':
    for i in range(NUM_CONSUMERS):
        _thread.start_new_thread(consumer, (i, ))
    for i in range(NUM_PRODUCERS):
        _thread.start_new_thread(producer, (i, ))
    time.sleep(((NUM_PRODUCERS - 1) * NUM_MESSAGES) + 1)
    print('Main thread exited')
