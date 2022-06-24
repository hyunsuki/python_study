import sys
import weakref
import numpy as np


class Foo:
    def __init__(self): pass


def first_case():
    l = []
    l.append(l)

    del l

def second_case():
    a = Foo() #  140527886807224 
    b = Foo() #  140527758869000

    a.x = b 
    b.x = a

    del a
    del b

def test_weakref(data):
    a = np.array([1,2,3])
    print(sys.getrefcount(a))
    b = weakref.ref(a)
    print(sys.getrefcount(a))

    print(f'b() :: {b()}')
    data = None
    print(f'after a = None. b ::  {b}')


def main():
    test_weakref(np.array([1,2,3]))


if __name__ == '__main__':
    main()
