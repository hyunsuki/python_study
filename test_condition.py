import functools
import time


class ConditionTest:

    def __init__(self): pass

    def elapsed(original_func):
        @functools.wraps(original_func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = original_func(*args, **kwargs)
            end = time.time()
            print("함수 수행시간: %f 초" % (end - start))
            return result
    
        return wrapper

    @elapsed
    def testAnd(self, num):
        for i in range(num):
            if i % 2 == 0 and i % 3 == 0:
                return 'okay'
            else: 
                return 'No'

    @elapsed
    def testIf(self, num):
        for i in range(num):
            if i % 2 == 0:
                if i % 3 == 0:
                    return 'okay'
            else: 
                return 'No'


def main():
    ct = ConditionTest()
    test_num = 10000000000000000000000000000000000000000000000000000000000000
    ct.testAnd(test_num)
    ct.testIf(test_num)


if __name__ == '__main__':
    main()
