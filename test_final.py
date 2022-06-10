from typing import Final

import constant


class Constant1:
    PI = 3.14
    GRAVITY = 9.8


def main():
    num = 32
    print('='*num + 'case1' + '='*num)
    c1 = Constant1()
    print(f'PI :: {c1.PI}')
    c1.PI = 1
    print(f'After realocation PI :: {c1.PI}')

    print('='*num + 'case2' + '='*num)
    constant_data: Final = 3.14
    print(f'constant_data :: {constant_data}')
    constant_data = 1
    print(f'After realocation constant_data :: {constant_data}')

    print('='*num + 'case3' + '='*num)
    constant.PI = 3.14
    print(f'constant.PI :: {constant.PI}')
    print('Try realocate')
    constant.PI = 1
    print(f'constant.PI :: {constant.PI}')


if __name__ == '__main__':
    main()


