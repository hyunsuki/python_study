#!/usr/bin/python3
# -*- coding: utf-8 -*-


def removeUseDel(data, key):
    del(data[key])
    return data

def removeUsePop(data, key):
    data.pop(key)
    return data

def main():
    test_dict = {1: 'one', 2: 'two', 3: 'three'}
    print(f'test_dict :: {test_dict}')
    print(f'remove using del {removeUseDel(test_dict, 1)}')

    test_dict = {1: 'one', 2: 'two', 3: 'three'}
    print(f'remove using pop {removeUsePop(test_dict, 1)}')

    test_dict = {2: 'two', 5: 'five', 10: 'ten'}
    print(f'test_dict :: {test_dict}')
    test_dict[3]="three"
    print('add param :: 3: "three"')
    print(f'test_dict :: {test_dict}')


if __name__ == '__main__':
    main()
