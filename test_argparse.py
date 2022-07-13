#!/usr/bin/python3
# -*- coding: utf-8 -*-


from argparse import ArgumentParser


class ArgParse:

    def __init__(self):
        self.parser = ArgumentParser(description='Process some game.')


def main():
    ap = ArgParse()


if __name__ == '__main__':
    main()
