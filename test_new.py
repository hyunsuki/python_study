#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Sample:

    def __new__(cls, *args, **kwargs):
        print('new', args, kwargs)
        this = super().__new__(cls)
        cls.args = args
        cls.kwargs = kwargs
        return this

    def __init__(self, *args, **kwargs):
        print('init', args, kwargs)

    def show(self):
        print('show', self.args, self.kwargs)


def main():
    sample = Sample(123, key='abc')
    sample.show()
    print(sample)


if __name__ == '__main__':
    main()
