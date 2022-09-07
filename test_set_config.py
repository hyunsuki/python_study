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

        self.setTest1(conf, 'TEST', 'test_1')
        self.setTest2(conf, 'TEST', 'test_2')
        self.setTest3(conf, 'TEST', 'test_3')
        print('Test class init success')

    def setConfig(self, conf, var, section, option, default):
        var = default if not conf.has_option(section, option) else int(conf[section][option]) if option == 'test_2' or option == 'test_3' else conf[section][option]
        
    def setTest1(self, conf):
        self.test_1 = conf['TEST']['test_1'] if conf.has_option('TEST', 'test_1') else 'test.conf'

    def setTest2(self, conf, section, option):
        self.test_2 = int(conf[section][option]) if conf.has_option(section, option) else 1

    def setTest3(self, conf, section, option):
        self.test_3 = int(conf[section][option]) if conf.has_option(section, option) else 2


def main():
    t = Test()
    print(f"t.test_1 :: {t.test_1}") # Why None...?
    print(f"t.test_2 :: {t.test_2}") # Why None...?
    print(f"t.test_3 :: {t.test_3}") # Why None...?

    # 값들이 self.test_가 아닌 var에 할당되고 있음

if __name__ == "__main__":
    main()
