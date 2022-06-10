class TestClass1:

    def __init__(self):
        self.a = [1, 2, 3]

    def __len__(self):
        return len(self.a)


class TestClass2:

    def __init__(self):
        self.a = [1, 2, 3]

    def getLenOfA(self):
        return len(self.a)

def main():
    tc1 = TestClass1()
    tc2 = TestClass2()
    print(len(tc1))
    print(tc1.__len__())
    print(tc2.getLenOfA())

    print(dir(tc1))
    print(dir(tc2))



if __name__ == '__main__':
    main()
