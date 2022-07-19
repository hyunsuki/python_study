#!/usr/bin/python3
# -*- coding: utf-8 -*-

from enum import Enum


class Topics:
    INSTALLINFOS = 0
    FILEDOWNLOADINFOS = 1
    BUYINFOS = 2


class Sdk:
    def __init__(self):
        self.case = {
              Topics.INSTALLINFOS: self.install
            , Topics.FILEDOWNLOADINFOS: self.filedownload
            , Topics.BUYINFOS: self.buy
        }

    def sendToApi(self, topic_obj, **kwargs):
         topic = self.case[topic_obj]
         topic

    def install(self):
        print('install')

    def filedownload(self):
        print('filedownload')

    def buy(self):
        print('buy')


class Api:
    def __init__(self): pass


class Test:
    test = 1
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3


def main(): pass


if __name__ == '__main__':
    main()
