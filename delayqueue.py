import time
import threading
from queue import Queue

class DelayQueue:
    def __init__(self):
        self.queue = Queue()

    def put(self, item, delay):
        end_time = time.time() + delay
        self.queue.put((item, end_time))

    def run(self):
        while True:
            item, end_time = self.queue.get()
            while time.time() < end_time:
                time.sleep(0.1)
            self.process_item(item)
            self.queue.task_done()

    def process_item(self, item):
        print(f"handled: {item}")

dq = DelayQueue()
consume_thread = threading.Thread(target=dq.run)
consume_thread.daemon = True
consume_thread.start()

dq.put('task1', 5)
dq.put('task2', 10)
dq.queue.join()
print('all tasks finished')