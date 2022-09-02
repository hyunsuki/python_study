#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os


def main():
#    print(f"os.name :: {os.name}")
#
#    # os.fsencode(file name) => using UTF-8, add python version 3.2
#    print(f"os.fsencode('tree.txt') :: {os.fsencode('tree.txt')}")
#
#    # os.fsdencode(file name) => using UTF-8
#    print(f"os.fsdecode('tree.txt') :: {os.fsdecode('tree.txt')}")
#
#    # os.ctermid() => 프로세스 제어 터미널에 해당하는 파일명을 반환. unix에서만 사용 가능
#    print(f"os.ctermid() :: {os.ctermid()}")
#
#    # os.environ => C에서의 getenv("HOME")
#    #print(f"os.environ :: {os.environ}")
#    print(f"os.environ :: {os.environ['HOME']}")
#
#    # os.environb => environ bytes
#    #print(f"os.environb :: {os.environb}")
#    print(f"os.environb :: {os.environb[b'HOME']}")
#
#    # os.chdir =>
#    print(f"os.chdir('../python_study') :: {os.chdir('../python_study')}")
#
#    # os.fchdir =>?
#    #print(f"os.fchdir('../python_study') :: {os.fchdir('../python_study')}")
#
#    # os.getcwd =>
#    print(f"os.getcwd() :: {os.getcwd()}")

    # os.fspath(path) => add python version 3.6. 경로의 파일 시스템표현을반환
    print(f"os.fspath('tree.txt') :: {os.fspath('tree.txt')}")

    # os.PathLike => add python version 3.6
    print(f"os.PathLike :: {os.PathLike}")


if __name__ == "__main__":
    main()
