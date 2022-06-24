import sys
import weakref


class WeakList(list):
    def append(self, item):
        list.append(self, weakref.ref(item, self.remove))


def main():
    a = [1, 2, 3]
    print(f"a's reference counting :: {sys.getrefcount(a)}")
    b = WeakList(a)
    print(f"a's reference counting :: {sys.getrefcount(a)}")

    a = None
    print(f'b :: {b}')


if __name__ == '__main__':
    main()
