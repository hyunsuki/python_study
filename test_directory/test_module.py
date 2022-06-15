from test_condition import ConditionTest


class TestClass(ConditionTest):
    """
    This is test string.
    """
    def __init__(self):
        super(TestClass, self).__init__()

    @elapsed
    def printDoc(self):
        print(self.__doc__)


def main():
    print(TestClass().__doc__)


if __name__ == '__main__':
    main()
