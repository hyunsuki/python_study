from collections import abc


class Foo:
    def __len__(self):
        return 0


class Struggle:
    def __len__(self): return 1


def main():
    f = Foo()
    print(len(f))
    print(isinstance(Struggle(), abc.Sized))


if __name__ == '__main__':
    main()
