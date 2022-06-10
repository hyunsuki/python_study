class YieldTest:

    def __init__(self):
        self.test_list = ['1 ', '2 ', '3 ', '4 ', '5 ']

    def load(self):
        for line in self.test_list:
            value = line.strip()
            yield value


def main():
    yt = YieldTest()
    y = yt.load()
    print(next(y))
    print(next(y))
    print(next(y))
    print(next(y))
    print(next(y))
    print(next(y))
    

if __name__ == '__main__':
    main()
