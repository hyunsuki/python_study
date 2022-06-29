#!/usr/bin/python3
# -*- coding: utf-8 -*-


class CallbackTest:
    def __init__(self):
        pass

    def func_callback(self, c):
        print("string Length : ", c)

    def string_len(self, string, callback):
        string_len = len(string)
        callback(string_len)


def main():
    ct = CallbackTest()
    string1 = 'test string'
    string2 = 'test string test string'
    string3 = 'test string test string test string'
    string_list = [string1, string2, string3]

    for string in string_list:
        ct.string_len(string, ct.func_callback)
    

if __name__ == '__main__':
    main()
