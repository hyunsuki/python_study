import os


class TestModule:

    @classmethod
    def __init__(self, cls):
        self.mode = 'FILE'
        self.handle = TestFileModule if self.mode == 'FILE' else TestDBModule
        print(issubclass(cls, TestModule))
        if issubclass(cls, TestModule):
            print(type(cls))

    def create(self):
        self.handle().create()


class TestFileModule:

    def __init__(self): pass

    def create(self):
        print('create')


class TestDBModule:

    def __init__(self): pass

    def create(self):
        print('create')


def main():
    tm = TestMode()


if __name__ == '__main__':
    main()
