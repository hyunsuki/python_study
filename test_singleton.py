#!/usr/bin/python3
# -*- conding: utf-8 -*-


class Singleton(object):
    __instance = None

    def __init__(self):

        if not Singleton.__instance:
            print('Instance exist yet')

        else:
            print('Instance already exist', self.get_instance())

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


def main():
    print('Get Instance...  s1 = Singleton.get_instance()')
    s1 = Singleton.get_instance()
    print('Get Instance...  s2 = Singleton.get_instance()')
    s2 = Singleton.get_instance()
    print(f'Is id(s1) == id(s2)?? {id(s1) == id(s2)}')


if __name__ == '__main__':
    main()
