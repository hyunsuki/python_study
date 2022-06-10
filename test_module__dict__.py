class TestDict:

    def __init__(self):
        self.a = None
        self.b = None
        self.c = None
#        self.result = None

    def add(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        d = 4
        self.add_result = self.a+self.b+self.c+d
#        return self.a+self.b+self.c+d
        return self.result

    def getMember(self):
        return self.__dict__


def main():
    td = TestDict()
    print(td.getMember())
    print(td.add(1, 2, 3))
    print(td.getMember())


if __name__ == '__main__':
    main()
