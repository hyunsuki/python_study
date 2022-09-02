#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tracemalloc


class Test:
    def __init__(self, num):
        self.result = []
        self.num = num

        for i in range(self.num):
            self.result.append(i)

    def getResult(self): return self.result

def main():
    tracemalloc.start()
 
    t = Test(1000)

    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')

    print('[ TOP 10 ]')
    for stat in top_stats[:10]: print(stat)

if __name__ == "__main__":
    main()
