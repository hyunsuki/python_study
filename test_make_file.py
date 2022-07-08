#!/usr/bin/python3
# -*- coding: utf-8 -*-


def makeFile(file_):
    with open(file_, mode='w') as f:
        pass


def main():
    makeFile('test_file.txt')


if __name__ == '__main__':
    main()
