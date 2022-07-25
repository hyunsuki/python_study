#!/usr/bin/python3
#-*- coding: utf-8 -*-


class SingletonUseNew:
   def __new__(cls):
       if not hasattr(cls, "_instance"):
           print("__new__ is called\n")
           cls._instance = super().__new__(cls)
       return cls._instance

   def __init__(self):
       cls = type(self)
       print(cls._instance)
       if not hasattr(cls, "_init"):
           print("__init__ is called\n")
           cls._init = True


class SingletionWithoutNew:
    __instance = None

    @classmethod
    def __getInstance(cls):
        return cls.__instance

    @classmethod
    def instance(cls, *args, **kwargs):
        print(super().__new__(cls))
        if cls.__instance is None:
            cls.__instance = cls(*args, **kwargs)
        return cls.__instance


def main():
    print("Singleton with __new__")
    sun1 = SingletonUseNew()
    sun2 = SingletonUseNew()
    print(f"sun1's :: {id(sun1)}")
    print(f"sun2's :: {id(sun2)}\n")
    print("Singleton without __new__")
    swn1 = SingletionWithoutNew.instance()
    swn2 = SingletionWithoutNew.instance()
    print(f"\nswn1's :: {id(swn1)}")
    print(f"swn2's :: {id(swn2)}")


if __name__ == '__main__':
    main()
