#!/usr/bin/python3
# -*- coding: utf-8 -*-

from view import View
from model import Model
from binder import Binder
from view_model import ViewModel
from event import KeyBoardCommand

def main():
    client_input = KeyBoardCommand.excute()
    print(client_input)


if __name__ == '__main__':
    main()
