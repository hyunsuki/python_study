from icecream import ic


class DebugTest:

    def __init__(self):
        pass

    def testDebug(self):
        data = [1, 2, 3]
        if __debug__:
            ic(data)


def main():
    dt = DebugTest()
    dt.testDebug()


if __name__ == '__main__':
    main()


