#!/usr/bin/python3
# -*- coding: utf-8 -*-


def main():
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    print(f"dict1 | dict2 :: {dict1 | dict2}")
    print(f"dict2 | dict1 :: {dict2 | dict1}")


if __name__ == "__main__":
    main()
