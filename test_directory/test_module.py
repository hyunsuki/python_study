class TestClass:
    """
    This is test string.
    """
    def __init__(self):
        super(TestClass, self).__init__()
        print(f"__name__ :: {__name__}")

    def printDoc(self):
        print(self.__doc__)


def main():
    print(TestClass().__doc__)


if __name__ == '__main__':
    main()
