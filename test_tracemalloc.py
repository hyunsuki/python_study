#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tracemalloc
import waste_memory


class Test:
    def __init__(self):
        tracemalloc.start(10)
        self.time1 = tracemalloc.take_snapshot()
        import waste_memory
        x = waste_memory.run()
        self.time2 = tracemalloc.take_snapshot()

    def getStats(self):
        stats = self.time2.compare_to(self.time1, 'lineno')
        for stat in stats[:3]:
            print(stat)


def main():
    t = Test()
    t.getStats()


if __name__ == "__main__":
    main()
