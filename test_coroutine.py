class Test:

    def __init__(self):
        self.total = 0.0
        self.count = 0
        self.average = None

    def averager(self, input_num):
        self.total += input_num
        self.count += 1
        self.average = self.total/self.count
        return self.average

class TestCoroutine:

    def __init__(self): pass

    def averager(self):
        total = 0.0
        count = 0
        average = None

        while True:
            term = yield average
            total += term
            count += 1
            average = total/count


def main():
    t = Test()
    print(f't.averager(10) :: {t.averager(10)}')
    print(f't.averager(30) :: {t.averager(30)}')
    print(f't.averager(5) :: {t.averager(5)}')

    tc = TestCoroutine()
    coroutine_avg = tc.averager()
    next(coroutine_avg) # coroutine 기동

    print(f'coroutine_avg.send(10) :: {coroutine_avg.send(10)}')
    print(f'coroutine_avg.send(30) :: {coroutine_avg.send(30)}')
    print(f'coroutine_avg.send(5) :: {coroutine_avg.send(5)}')


if __name__ == '__main__':
    main()

