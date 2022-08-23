#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import secrets


def main():
    print(f"dir(random.SystemRandom) :: {dir(random.SystemRandom)}")
    print(f"dir(secrets.SystemRandom) :: {dir(secrets.SystemRandom)}")


if __name__ == "__main__":
    main()
