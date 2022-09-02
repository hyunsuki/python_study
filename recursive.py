#!/usr/bin/python3
# -*- coding: utf-8 -*-


def main(data):
    if data < 0:
        print("ended")
        return
    else:
        print(data)
        main(data-1)
        print("-"*10)
        print(f"returned {data}")


if __name__ == "__main__":
    main(4)
