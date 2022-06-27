#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Singleton:
    __instance = None

    def __init__(self):
        print('Instance exist yet')

    @classmethod
    def getInstance(cls, *args, **kwargs):
        cls.__instance = cls.__instance or cls(*args, **kwargs)
        return cls.__instance
