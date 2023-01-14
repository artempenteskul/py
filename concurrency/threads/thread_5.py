import threading


class ProgramThread(threading.Thread):
    def __init__(self, th_id, count, mutex):
        self.th_id = th_id
        self.count = count
        self.mutex = mutex
        threading.Thread.__init__(self)

    def run(self) -> None:
        for i in range(self.count):
            with self.mutex:
                print(f'{self.th_id} => {i}')


stdout_mutex = threading.Lock()
threads = []

for j in range(10):
    thread = ProgramThread(j, 100, stdout_mutex)
    thread.start()
    threads.append(thread)


for th in threads:
    th.join()


print('Main thread exiting.')
