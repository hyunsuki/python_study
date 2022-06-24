#!/usr/bin/python3

class TestClass:
    def __init__(self):
        print('instance create\n')


def main(test_class: TestClass) -> None:
    test_class1 = test_class or TestClass()
    return test_class1


if __name__ == '__main__':
    # test case1
    print('Test case 1 :: main(None)\n')
    main(None)

    # test case2
    print('test_class = TestClass()')
    test_class = TestClass()
    print('Test case 2 :: main(test_class)')
    main(test_class)

    print(id(main(None)) == id(main(test_class)))
    print(id(main(test_class)) == id(main(test_class)))
