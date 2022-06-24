from threading import Thread
from threading import Lock


class Counter:

    def __init__(self):
        self.count = 0
        self.lock = Lock()#

    def increment(self, offset):
        with self.lock:#
            self.count += offset


def worker(index, how_many, counter):
    for _ in range(how_many):
        counter.increment(1)


how_many = 100000
counter = Counter()

threads = []
for i in range(5):
    thread = Thread(target=worker, args=(i, how_many, counter))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

expected = 5*how_many
result = counter.count

print(f"Expected {expected}, Result {result}")
