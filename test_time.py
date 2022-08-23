#!/usr/bin/python3
# -*- coding: utf-8 -*- 

import datetime


class Time:
    @classmethod
    def getCurrTime(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[-6:]


def main():
    date_list = [1, 2, 3]
    print(f"Time.getCurrTime() :: {Time.getCurrTime()}")
    index = [idx for idx in range(len(date_list))]
    print(f"index :: {index}")


if __name__ == "__main__":
    main()
