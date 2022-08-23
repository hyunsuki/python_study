#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
import random
import secrets
from datetime import datetime


class Utils:

    def __init__(self, data_list):
        self.time_format = "%Y-%m-%d %M:%M:%S.%f"
        self.data_list = data_list
        self.weights = self.getRandomWeights()

    def getRandom(self):
        return self.data_list[self.getRandomIndex()]

    def getRandomIndex(self):
        indexs = [index for index in range(len(self.data_list))]
        random_p = self.weights
        a = np.random.choice(indexs, len(self.data_list), p=random_p)
        return random.choice(a)

    def getRandomWeights(self):
        weights = []
        p = 1.0
        # list의 요소 개수만큼 random weight 생성
        for i in range(len(self.data_list)):
            if i == len(self.data_list)-1: rand_p = p
            else: rand_p = random.uniform(0, p)
            weights.append(rand_p)
            p = p-rand_p
        print(weights)
        print("")
        return weights       


def main():
    test_data = [1, 2, 3, 4, 5]
    num = 10000

    u = Utils(test_data)

    result = []
    for i in range(0, num):
        result.append(u.getRandom())

    for param in test_data:
        print(f"{param} 확률 :: {result.count(param)/num}")


if __name__ == "__main__":
    main()
