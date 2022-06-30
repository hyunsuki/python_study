#!/usr/bin/python3
# -*- conding: utf-8 -*-


import sys
from select import select
from io import StringIO


class KeyBoard:

    def __init__(self):
        self.time_out = 5

    def getInput(self):
        input_value = sys.stdin
        io = StringIO()
        i, o, e = select([input_value], [], [], self.time_out)
        if (i):
            print(input_value.readline().strip(), file=io, end="")
            return io.getvalue()

        else:
            print("INPUT INDEX NOTHING... TIME OUT")


def main():
    keyboard = KeyBoard()
    input_index = keyboard.getInput()
    print(input_index)


if __name__ == '__main__':
    main()
