#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Calculator:
    @classmethod
    def div(self, a, b):
        return a%b


def main():
    a = 1118
    b = 3
    print(f"Calculator.div({a}, {b}) :: {Calculator.div(a, b)}")


if __name__  == "__main__":
    main()
