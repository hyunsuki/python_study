#!/usr/bin/python3
# -*- coding: utf-8 -*-


class WithoutSlots:
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier


class WithSlots:
    __slots__ = ["name", "identifier"]
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier


def main():
    import traceback
    without_slot = WithoutSlots(1, 1)
    print(f"without_slot.__dict__ :: {without_slot.__dict__}\n")
    with_slot = WithSlots(1, 1)
    try: print(f"with_slot.__dict__ :: {with_slot.__dict__}\n")
    except: traceback.print_exc()


if __name__ == '__main__':
    main()
