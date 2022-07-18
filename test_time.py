#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time


class Time:

    @classmethod
    def measureTime(cls, func):
        def wrapper_fn(*args, **kwargs):
            start_time = time.time()
            resul = func(*args, **kwargs)
            end_time = time.time()
            
