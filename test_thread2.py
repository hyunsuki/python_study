#!/usr/bin/python3
# -*- coding: utf-8 -*-

#import signal
#import time
#from queue import Queue
#from threading import Thread
#
#
#class Thread:
#    threads = []
#
#    def __init__(self): pass
#
#    def run(self):
#        for thread in threads:
#            print(thread)
#
#
#class KillSignal:
#    def __init__(self):
#        self.IS_SHUTDOWN = False
#        signal.signal(signal.SIGINT, self.handler)
#        signal.signal(signal.SIGTERM, self.handler)
#
#    def handler(self, *args):
#        self.setShutdown()
#        return self.IS_SHUTDOWN
#
#    def setShutdown(self):
#        return self.IS_SHUTDOWN
#
#
#class Engine:
#    def __init__(self):
#        self.kill_signal = KillSignal()
#        self.thread = Thread()
#
#    def run(self):
#        while not self.kill_signal.isShutdown():
#            if self.kill_signal.isShutdown(): break
#            try:
#                 input_value = input('input: ')
#                 print(f"Input value :: {input_value}")
#
#            except Exception('Problem Occurred'): pass
#
#
#class Keyboard:
#    def __init__(self):
#        self.input_buffer = queue.Queue()
#        self.thread = Thread()
#
#    def getInput(self, message):
#        time.sleep(1)
#        response = input(message)
#        self.input_buffer.put(response)
#
#    def getInputWithTimeout(self):


import time
import threading
import traceback

class TestTimer:
    def __init__(self):
        #self.thread_timer = threading.Timer(, self.function)
        self.is_stop = False
        self.input_list = []
        execute_num = 0


    def function(self):
        input_value = input('input: ')
        self.input_list.append(input_value)

    def realFunction(self):
        while not self.is_stop:
             thread = threading.Timer(1, self.function)
             time.sleep(3)
             thread.daemon = True
             thread.start()
#            self.thread_timer.start()
             try:
                 response = self.input_list.pop()
                 return response
             except: traceback.print_exc()
             return None 


def main():
    tt = TestTimer()
    tt.realFunction()


if __name__ == '__main__':
    main()
