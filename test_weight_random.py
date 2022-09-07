#!/usr/bin/python3
# -*- coding: utf=8 -*-

import random
from enum import Enum
from enum import EnumMeta


class Vo(Enum):
    A = 0
    B = 1
    C = 2
    D = 3


class WeightRandom:
    def __init__(self):
        # Random 기준점 세팅
        self
        self.pivot = random.uniform(0, 1)

    def getRandomWeights(self, target):
        if 


def main():
    wr = WeightRandom()
    print(f"wr.pivot :: {wr.pivot}")


if __name__ == "__main__":
    main()
