#!/usr/bin/python3
# -*- coding: utf-8 -*-

import threading
import queue
import time

class KeyBoard(threading.Thread) :

    def __init__(self) :
        threading.Thread.__init__(self)
        
        self.q = queue.Queue()
        self.is_shutdown = False
        self.timeout_sec = 1

        print('init success')

    def putInput(self) :

        input_number = input()
        if input_number.isdigit() :
            print(f'queue put : {input_number}')
            self.q.put(input_number)
        else :
            print('please enter a number')

    def get(self) :

        if self.q.qsize() > 0 :
            input_number = self.q.get(True, self.timeout_sec)
            print(f'queue get : {input_number}')
            yield input_number

#    def setShutdown(self) :
#
#        if self.max_count == self.cur_count :
#            print('max using and set shutdown')
#            self.is_shutdown = True
        

    def run(self) :
        print('start')

        while not self.is_shutdown :
            self.putInput()
#            self.setShutdown()
            time.sleep(0.1)
        
        print('end')

###########################################################

keyboard = KeyBoard()
keyboard.daemon = True
keyboard.start()

while not keyboard.is_shutdown :
    for input_number in keyboard.get() :
        print(f'keyboard input : {input_number}')

keyboard.join()
