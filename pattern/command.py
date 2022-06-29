#!/usr/bin/python3
# -*- conding: utf-8 -*-


class button:

    def __init__(self):
        self.__command = None

    def pressed(self):
        self.__command()

    def setCommand(self, command):
        self.__command = command


class Command:

    def execute(self): pass


class Power:

    @classmethod
    def turnOn(cls): print('TURN ON!')

    @classmethod
    def turnOff(cls): print('TURN OFF!')


class Channel:

    @classmethod
    def up(cls): print('CHANNEL UP')

    @classmethod
    def down(cls): print('CHANNEL DOWN')


class PowerOncommand(Command):

    @classmethod
    def excute(cls): 
