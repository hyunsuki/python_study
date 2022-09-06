#!/usr/bin/python3
# -*- coding: utf-8 -*-

from time import process_time
from datetime import timedelta
from functools import wraps
from configparser import ConfigParser


class Test:
    def __init__(self):
        self.conf = ConfigParser()
        self.conf.read('test2.conf')
        self.test_conf = None

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
    def try_except_defendency(self):
        try: self.test_conf = self.conf['TEST']['test']
        except: self.test_conf = 'test.conf'

    @timer_decorator
    def ternary_operator_defendency(self):
        self.test_conf=self.conf['TEST']['test'] if self.conf.has_option('TEST', 'test') else 'test.conf'


def main():
    t = Test()
    t.try_except_defendency()
    t.ternary_operator_defendency()


if __name__ == "__main__":
    main()
