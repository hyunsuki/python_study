#!/usr/bin/python3
# -*- coding: utf-8 -*-

from enum import Enum


class Topics:
    INSTALLINFOS = 0
    FILEDOWNLOADINFOS = 1
    BUYINFOS = 2
    CONTENTACTINFOS = 3
    RESOURCECHANGEINFOS = 4
    VMONEYCHANGEINFOS = 5
    ITEMCHANGEINFOS = 6
    CONNECTINFOS = 7
    ADPERFORMINFOS = 8
    FRIENDSHIPINFOS = 9


class Sdk:
    def __init__(self):
        self.case = {
              Topics.INSTALLINFOS: self.install
            , Topics.FILEDOWNLOADINFOS: self.filedownload
            , Topics.BUYINFOS: self.buy
            , Topics.CONTENTACTINFOS: self.contentact
            , Topics.RESOURCECHANGEINFOS: self.resourcechange
            , Topics.VMONEYCHANGEINFOS: self.vmoneychange
            , Topics.ITEMCHANGEINFOS: self.itemchange
            , Topics.CONTENTINFOS: self.content
            , Topics.ADPERFORMINFOS: self.adperform
            , Topics.FRIENDSHIPINFOS: self.friendship
        }

    def sendToApi(self, topic_obj, **kwargs):
         topic = self.case[topic_obj]
         topic

    def install(self):

    def filedownload(self):

    def buy(self):

    def contentact(self):

    def resourceChang(self):

    def vmoneychange(self):

    def itemchange(self):

    def connect(self):

    def adperform(self):

    def friendship(self):

class Api:
    def __init__(self): pass


def main(): pass


if __name__ == '__main__':
    main()
