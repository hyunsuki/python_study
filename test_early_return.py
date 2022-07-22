#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Test:

    def __init__(self):
        self.input_value = input('Press any key: ')
        self.checkInput()

    def checkInput(self):
        if self.isNum():
            print('Input value is number')
        #    return self.input_value

        if self.isAlpha():
            print('Input value is alphabet')
        return self.input_value
        

    def isNum(self):
        print('isNum check start')
        return self.input_value.isdigit()
    
    def isAlpha(self):
        print('isAlpha check start')
        return self.input_value.isalpha()

def main():
    t = Test()



if __name__ == '__main__':
    main()
