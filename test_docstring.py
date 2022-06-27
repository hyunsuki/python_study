class Docsting:

    @classmethod
    def printDocsting(cls, mode='doc'):
        if mode == 'doc':
            print(cls.__doc__)
            return

        elif mode == 'help':
            help(cls)
            return

        else: print('Not supported mode')
        


class TestCase1(Docsting):
    '''This class is test class1.(Python official documentation standards)
    :param1: ~~~
    '''


class TestCase2(Docsting):
    '''This class is test class2.(Google Docstring)
    Param1:
      ~~~
    '''


class TestCase3(Docsting):
    '''
    This class is test class3
    '''


def main():
    print('\nPrint Case 1-1')
    TestCase1.printDocsting()
    print('\nPrint Case 1-2')
    TestCase1.printDocsting(mode='help')

    print('\nPrint Case 1-1')
    TestCase2.printDocsting()
    print('\nPrint Case 1-2')
    TestCase2.printDocsting(mode='help')

    print('\nPrint Case 1-1')
    TestCase3.printDocsting()
    print('\nPrint Case 1-2')
    TestCase3.printDocsting(mode='help')


if __name__ == '__main__':
    main()
