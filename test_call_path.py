from test_module import TestModule


class Test(TestModule):

    def __init__(self):
        super(Test, self).__init__(Test)


def main():
    t = Test()


if __name__ == '__main__':
    main()
