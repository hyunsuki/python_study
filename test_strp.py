#!/usr/bin/python3
# -*- coding: utf-8 -*-

from datetime import datetime


class Converter:

    def convertDate(self, date):
        date_data = None
        if isinstance(date, int):
            date_data = str(date)[:4] + '-' + str(date)[-2:]

        if isinstance(date, str):
            date_data = date[:4] + '-' + date[-2:] 

#        return date_data
        print(date_data)
        return self.strToDateTime(date_data)

    def strToDateTime(self, date_string, format_="%Y-%U"):
        return datetime.strptime(date_string, format_)


def main():
    test_date_format = 201530
    c = Converter()
    date = c.convertDate(test_date_format)
    print(f'date :: {date}')
    print(f'date type :: {type(date)}')


if __name__ == '__main__':
    main()
