import sys
import functools
import time


class FileManager:

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
    def readAllLiineUseObj(self, file_path):
        with open(file_path, 'r', encoding='UTF-8') as f:
             print(f'FILE OBJECT SIZE :: {sys.getsizeof(f)}')
             for line in f:
                 print(line, end='')

    @elapsed
    def readAllLiineUseReadlines(self, file_path):
        with open(file_path, 'r', encoding='UTF-8') as f:
             all_lines = f.readlines()
             print(f'F.READLINES SIZE :: {sys.getsizeof(all_lines)}')
             for line in all_lines:
                 print(line, end='')

    def readAllLiineUseXreadlines(self, file_path):
        with open(file_path, 'r', encoding='UTF-8') as f:
             for line in f.xreadlines():
                 print(line, end='')

    @elapsed
    def readAllLiineUseReadline(self, file_path):
        with open(file_path, 'r', encoding='UTF-8') as f:
             line = None
             while line != '':
                 line = f.readline()
                 print(line, end='')

def main():
    sys.stdout = open('stdout.txt', 'w')

    file_path = 'test_linesep.txt'
    fm = FileManager()
    print('**PRINT ALL LINES USING FILE OBJECT**')
    fm.readAllLiineUseObj(file_path)
    print('**PRINT ALL LINES USING READLINES**')
    fm.readAllLiineUseReadlines(file_path)
    print('**PRINT ALL LINES USING READLINE**')
    fm.readAllLiineUseReadline(file_path)

    sys.stdout.close


if __name__ == '__main__':
    main()
