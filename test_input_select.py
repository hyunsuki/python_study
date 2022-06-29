#!/usr/bin/python3
# -*- conding: utf-8 -*-


import sys
from select import select


class KeyBoard:

    def __init__(self):
        self.time_out = 5

    def getInput(self):
        i, o, e = select([sys.stdin], [], [], self.time_out)
        if (i): print("INPUT INDEX : ", sys.stdin.readline().strip())

        else: print("INPUT INDEX NOTHING... TIME OUT")

        return i[0]


def main():
    keyboard = KeyBoard()
    input_index = keyboard.getInput()
    print(input_index)


if __name__ == '__main__':
    main()
