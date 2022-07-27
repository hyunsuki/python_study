#!/usr/bin/python3
# -*- coding: utf-8 -*-

import math
import traceback


class Test:
    def __init__(self): pass

    def getLandingPosition(self, velocity, angle, g_constant):
        if velocity < 0: raise Exception('velocity는 0과 같거나 커야합니다.')

        velocity_x = velocity * math.cos(angle / 180 * math.pi)
        velocity_y = velocity * math.sin(angle / 180 * math.pi)

        terminal_time = velocity_y / g_constant
        landing_position = velocity_x * terminal_time

        return landing_position


def main():
    test_list = [1, 2, 3]
    print(isinstance(test_list[3], IndexError))
#    t = Test()
#    t.getLandingPosition(-1, 10, 10)
    


if __name__ == '__main__':
    main()
