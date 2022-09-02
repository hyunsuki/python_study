#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
from datetime import timedelta
from sys import getsizeof


class WithoutSlots:

    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier

    def getName(self): return self.name

    def getIdentifier(self): return self.identifier


class WithSlots:
    __slots__ = ["name", "identifier"]

    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier

    def getName(self): return self.name

    def getIdentifier(self): return self.identifier


def main():

    import traceback
    without_slots = WithoutSlots(1, 1)
    print(f"without_slot.__dict__ :: {without_slots.__dict__}\n")
    with_slots = WithSlots(1, 1)
    try: print(f"with_slot.__dict__ :: {with_slots.__dict__}\n")
    except: traceback.print_exc()

    start1 = time.process_time()
    with_slots.getName()
    end1 = time.process_time()
    print(f"with_slots's getName run time :: {timedelta(seconds=end1-start1)}")

    start2 = time.process_time()
    without_slots.getName()
    end2 = time.process_time()
    print(f"without_slots's getName run time :: {timedelta(seconds=end2-start2)}")

    start3 = time.process_time()
    with_slots.getIdentifier()
    end3 = time.process_time()
    print(f"with_slots's getIdentifier run time :: {timedelta(seconds=end3-start3)}")

    start4 = time.process_time()
    without_slots.getIdentifier()
    end4 = time.process_time()
    print(f"without_slots's getIdentifier run time :: {timedelta(seconds=end4-start4)}")

    print(f"size of with_slots class :: {getsizeof(with_slots)}")
    print(f"size of without_slots class :: {getsizeof(without_slots)}")


if __name__ == '__main__':
    main()
