#!/usr/loacal/bin/python3.8
from pyc_test import Color

class StudyManager:
    def __init__(self):
        self.red = Color.RED

    def getRed(self):
        """
        레드의 객체를 리턴한다
        """
        return self.red

    def testAssert(self):
        standard = 100
        input_num = int(input('값을 입력하세요'))
        try:
            assert standard == input_num, '기준값은 %s, 입력값은 %s.'%(standard, input_num)
            print('기준 충족')
        except AssertionError as err:
            print('AssertionError :', err)

def main():
    sm = StudyManager()
    # doc
    print('ColorManager.getRed -> %s' % sm.getRed())
    print(sm.getRed.__doc__)
    
    # assert
    sm.testAssert()


if __name__ == '__main__':
    main()
