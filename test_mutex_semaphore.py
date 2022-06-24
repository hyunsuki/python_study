import threading
import time

class MutualExclution:
    resource = 0

    def __init__(self, excute_num):
        self.num = excute_num

    def testMutex(self):
        lock = threading.Lock()
# way1
        with lock:
            self.__caculation()
# way2
#        lock.acquire()
#        self.__caculation()
#        lock.release()

    def testSemaphore(self, limit_num=2):
        semaphore = threading.Semaphore(limit_num)
        print(f"semaphore counter_num before run :: {semaphore._value}")

        with semaphore:
            self.__caculation()
            print(f"semaphore counter_num after run :: {semaphore._value}")
        print(f"semaphore counter_num with outside :: {semaphore._value}")

    def __caculation(self):
        for i in range(self.num):
            MutualExclution.resource += 1


def main():
    me = MutualExclution(100)
    mutex_thread = threading.Thread(target=me.testMutex)
    mutex_thread.start()
    mutex_thread.join()
    print(f"Resource after mutex test ::  {MutualExclution.resource}")

    semaphore_therad = threading.Thread(target=me.testSemaphore)
    semaphore_therad.start()
    semaphore_therad.join()
    print(f"Resource after semaphore test ::  {MutualExclution.resource}")


if __name__ == '__main__':
    main()


