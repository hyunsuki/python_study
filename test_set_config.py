#!/usr/bin/python3
# -*- coding: utf-8 -*-

from varname import nameof
from configparser import ConfigParser


class Test:
    def __init__(self):
        print('Test class init start')
        conf = ConfigParser()
        conf.read('test2.conf')
        self.test_1 = None
        self.test_2 = None
        self.test_3 = None

        self.setConfig(conf, self.test_1, 'TEST', 'test_1', 'test.conf')
        self.setConfig(conf, self.test_2, 'TEST', 'test_2', 1)
        self.setConfig(conf, self.test_3, 'TEST', 'test_3', 2)
        print('Test class init success')

    def setConfig(self, conf, var, section, option, default):
        var = default if not conf.has_option(section, option) else int(conf[section][option]) if option == 'test_2' or option == 'test_3' else conf[section][option]
        
        print(f"var name :: {nameof(var)}")
        print(f"var :: {var}")
        print(f"var's type :: {type(var)}")


def main():
    t = Test()
    print(f"t.test_1 :: {t.test_1}") # Why None...?
    print(f"t.test_2 :: {t.test_2}") # Why None...?
    print(f"t.test_3 :: {t.test_3}") # Why None...?

    # 값들이 self.test_가 아닌 var에 할당되고 있음

if __name__ == "__main__":
    main()
