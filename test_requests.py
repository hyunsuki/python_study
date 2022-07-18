#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests


class TestRequest:

    def __init__(self):
        pass

    def get(self, url):
        return requests.get(url)


def main():
    url = "https://naver.com"
    tr = TestRequest()
    resp = tr.get(url)
    print(resp.text)


if __name__ == '__main__':
    main()
