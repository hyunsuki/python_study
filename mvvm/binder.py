#!/usr/bin/python3
# -*- condig: utf-8 -*-

#from view import View
#from view_model import ViewModel


class Binder:
    def __init__(self):
        self.client_input = None

    def receiveCall(self, client_input):
        self.client_input = client_input

    def getClientInput(self):
        return self.client_input


class BinderItem:
    def __init__(self, current_page):
        self.current_page = current_page


def main():
    b = Binder()
    print(b.page_stack)


if __name__ == '__main__':
    main()
