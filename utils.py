#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
import random
import secrets
from datetime import datetime


class Vo:
    def __init__(self, a, b, c, d, e):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e

    def getLen(self): return len(self.__dict__)

    def getList(self): return list(self.__dict__.values())


class Utils:

    def __init__(self, data_vo):
        self.data_vo = data_vo
        self.weights = Weights()
        self.__setRandomWeights()
        print(f"probabilltys :: {self.weights.probabilltys}")

    def getRandom(self):
        return np.random.choice(self.data_vo.getList(), 1, p=self.weights.probabilltys)

    def __setRandomWeights(self):
        p = 1.0
        for i in range(self.data_vo.getLen()):
            # 마지막 실행
            if i == self.data_vo.getLen()-1: rand_p = p
            else: rand_p = random.uniform(0, p)
            self.weights.probabilltys.append(rand_p)
            p = p-rand_p


class Weights:

    def __init__(self):
        self.probabilltys = []


def main():
    test_data = Vo(1, 2, 3, 4, 5)

    num = 100000

    u = Utils(test_data)

    result = []
    for i in range(0, num):
        result.append(u.getRandom())

    for param in test_data.getList():
        print(f"{param} 확률 :: {result.count(param)/num}")


if __name__ == "__main__":
    main()
