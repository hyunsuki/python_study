from enum import Enum

class TestEnum(Enum):
    A = 0
    B = 1
    C = 2


class Test:
    def getName(self, e):
        if isinstance(e, int):
            return self.getNameByIndex(e)
            #print(f'e :: {e}, type :: int')

        elif isinstance(e, Enum):
            return e.name
            #print(f'e :: {e}, type :: enum')

        else:
            raise Exception('Not supported')

    def getNameByIndex(self, index):
        return TestEnum(index).name


def main():
    t = Test()
    print(t.getName(0))
    print(t.getName(TestEnum.A))
    print(t.getName([0, 1]))
     

if __name__ == '__main__':
    main()
