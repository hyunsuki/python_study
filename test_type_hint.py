class SomeClass:

    def some_work(self, name: str) -> str:
        full_name: str = ''.join(['Kim', name])
        return full_name


def main():
    sc = SomeClass()
    #sc.some_work('hunsuki')
    sc.some_work(1)


if __name__ == '__main__':
    main()
