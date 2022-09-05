#!/usr/bin/python3
# -*- coding: utf-8 -*-
from configparser import ConfigParser


class Test:
   def __init__(self):
       config_file = "test.conf"
       self.conf = ConfigParser()
       self.conf.read(config_file)

   def test1(self):
       format_ = self.conf['LOG']['formatter']
#       try: self.conf['LOG']['format']
#       except: "[%(asctime)s] [%(process)d | %(threadName)s] [%(levelname)s] [%(module)s | %(funcName)s] - %(message)s"

   def test2(self):
       return self.conf['LOG']['formatter'] if self.conf.has_option('LOG', 'formatter') else "[%%(asctime)s] [%%(process)d | %%(threadName)s] [%%(levelname)s] [%%(module)s | %%(funcName)s] - %%(message)s"


def main():
    t = Test()
    t.test1()
    t.test2()


if __name__ == "__main__":
    main()
