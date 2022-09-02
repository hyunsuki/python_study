#!/usr/bin/python3
# -*- coding: utf-8 -*- 

import time
import datetime


class Time:
    @classmethod
    def getCurrTime(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[-6:]

    @classmethod
    def getMinYear(self): return datetime.MINYEAR

    @classmethod
    def getMaxYear(self): return datetime.MAXYEAR


def main():
    date_list = [1, 2, 3]
    print(f"Time.getCurrTime() :: {Time.getCurrTime()}")
    index = [idx for idx in range(len(date_list))]
    print(f"index :: {index}")

    # datetime - min year
    print(f"datetime.MINYEAR :: {Time.getMinYear}")

    # datetime - max year
    print(f"datetime.MAXYEAR :: {Time.getMaxYear}")


if __name__ == "__main__":
    main()
