import time
import multiprocessing


class Process:

    def __init__(self, range_num):
        self.range_num = range_num
        self.run_time = None

    def count(self, num_list):
        for name in num_list:
            for i in range(1, self.range_num):
                print(name, " : ", i)

    def process(self, num_list):
        start_time = time.time()
        self.count(num_list)

        end_time = time.time()
        self.run_time = end_time - start_time

    def getRunTime(self):
        return f'Run time :: {self.run_time}'


class Normal(Process):

    def __init__(self, range_num):
        super(Normal, self).__init__(range_num)

    def run(self, num_list):
        self.process(num_list)

class Multi(Process):

    def __init__(self,  range_num):
        super(Multi, self).__init__(range_num)

    def run(self, num_list):
        pool = multiprocessing.Pool(processes=2)
        pool.map(self.process, [num_list])
        pool.close()
        pool.join()
        self.process(num_list)


def main():
    range_num = 50001
    num_list = ['p1', 'p2', 'p3', 'p4']
    np = Normal(range_num)
    mp = Multi(range_num)
    np.run(num_list)
    mp.run(num_list)
    print(f'NORMAL {np.getRunTime()}')
    print(f'MULTI {mp.getRunTime()}')


if __name__ == '__main__':
    main()
