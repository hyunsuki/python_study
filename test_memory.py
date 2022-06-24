import sys
from time import time

class MemoryTest :

    def __init__(self, test_num) :
        self.test_num = test_num

    def logging_time(original_fn):
        def wrapper_fn(*args, **kwargs):
            start_time = time()
            result = original_fn(*args, **kwargs)
            end_time = time()
            print("WorkingTime[{}]: {} sec".format(original_fn.__name__, end_time-start_time))
            return result
        return wrapper_fn

    @logging_time
    def testInt(self) :
        int_list = []
        int_list = [num for num in range(0, self.test_num)]
        print(sys.getsizeof(int_list))

    @logging_time
    def testStr(self) :
        str_list = []
        str_list = [str(num) for num in range(0, self.test_num)]
        print(sys.getsizeof(str_list))

    @logging_time
    def testObj(self) :
        obj_dict = {}
        for i in range(0, self.test_num) :
            obj_dict.setdefault(i, i) 
        print(sys.getsizeof(obj_dict))
        

def main():
    memory_test = MemoryTest(1000000)
    memory_test.testInt()
    memory_test.testStr()
    memory_test.testObj()

if __name__ == '__main__' :
    main()
