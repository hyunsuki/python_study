#!/usr/bin/python3
# -*- coding: utf-8 -*-

from time import process_time
from datetime import timedelta
from functools import wraps


class Test:
    def __init__(self, datas):
        self.tesk1(datas)
        self.tesk2(datas)
        self.tesk3(datas)


    def timer_decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            start = process_time()
            result = function(*args, **kwargs)
            end = process_time()
            print(f"Sucess {timedelta(seconds=(end-start))} taken for {function.__name__}")

            return result
        return wrapper

    @timer_decorator
    def tesk1(self, datas):
        for i in range(100000):
            for data in datas:
                self.returnOnce(data)

    @timer_decorator
    def tesk2(self, datas):
        for i in range(100000):
            for data in datas:
                self.returnEarly1(data)

    @timer_decorator
    def tesk3(self, datas):
        for i in range(100000):
            for data in datas:
                self.returnEarly2(data)

    def returnOnce(self, data):
        if isinstance(data, str): result = int(data)
        else: result = data
        return result

    def returnEarly1(self, data):
        if isinstance(data, str): return int(data)
        else: return data

    def returnEarly2(self, data):
        if not isinstance(data, str): return data
        else: return int(data)

def main():
    data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, '15']
    t = Test(data_list)


if __name__ == '__main__':
    main()
