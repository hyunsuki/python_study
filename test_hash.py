#!/usr/bin/python3
# -*- coding: utf-8 -*-

import hashlib


class TestHash:
   def __init__(self):
       self.md5_hash = hashlib.md5()

   def printAlgorithms(self):
       print(hashlib.algorithms_available)

   def update(self, data):
       self.md5_hash.update(bytes(data, 'utf-8'))

   def get(self):
       return self.md5_hash

   def printHash(self):
       print(self.md5_hash.digest())


def main():
    string = 'test'
    th = TestHash()
    th.printAlgorithms()

    th.update(string)
    print(f'Result :: {th.get()}')
    th.printHash()


if __name__ == '__main__':
    main()
