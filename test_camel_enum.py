#!/usr/bin/python3
# -*- coding: utf-8 -*-

from enum import Enum


class CEnum(Enum):

    def process(cls, string, index):
        return string[:index]+string[index+1].upper()+string[index+2:]

    def convertCamel(cls):
        camel_name = cls.name.lower()
        for i in range(cls.name.count('_')):
            index = camel_name.find('_')
            camel_name = cls.process(camel_name, index)
        return camel_name


class Test(Enum):
    installType = 0
    

class Test2(CEnum):
    INSTALL_TYPE = 0
    PROMOTE_CONTENT_NAME = 1


def main():
    print(f"Test.installType.name :: {Test(0).name}")
    print(f"Test.INSTALL_TYPE.name :: {Test2(0).convertCamel()}")
    print(f"Test.PROMOTE_CONTENT_NAME.name :: {Test2(1).convertCamel()}")


if __name__ == "__main__":
    main()
