#!/usr/bin/python3
# -*- coding: utf-8 -*-


from enum import Enum


class Case(Enum): 
    CASE1 = {'test1': 'value1'}
    CASE2 = {'test2': 'value2'}


class Sdk:

    single_instance = None

    def __init__(self):
        if Sdk.single_instance is None:
            Sdk.single_instance = Api()

    def sendTo(self, **kwargs):
        Sdk.single_instance.vo.update(kwargs)
        

class Api:
    def __init__(self):
        self.vo = {
              'test1':''
            , 'test2':''
    }

def main():
    sdk = Sdk()
    sdk.sendTo(**Case.CASE1.value)
    sdk.sendTo(**Case.CASE2.value)
    print(sdk.single_instance.vo)


if __name__ == '__main__':
    main()
