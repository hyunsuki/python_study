import time
import functools
from io import StringIO
import sys

def elapsed(original_func):
    @functools.wraps(original_func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = original_func(*args, **kwargs)
        end = time.time()
        print("함수 수행시간: %f 초" % (end - start))
        return result
    
    return wrapper

#  +를 이용한 연결
@elapsed
def concatWithPlus(n):
    out_str = ''
    for num in range(1, n):
        out_str += 'num'
    print(f'Memory :: {sys.getsizeof(out_str)}')
    return out_str

#  list join을 이용한 방법
@elapsed
def concatWithJoin(n):
    str_list = []
    for num in range(1, n):
        str_list.append('num')
    print(f'Memory :: {sys.getsizeof(str_list)}')
    return ''.join(str_list)

#  수도 파일 이용하는 방법
@elapsed
def concatWithStingIO(n):
    file_str = StringIO()
    for num in range(1, n):
        file_str.write('num')
    print(f'Memory :: {sys.getsizeof(file_str)}')
    return file_str.getvalue()

#  join과 복합 리스트 이용한 방법
@elapsed
def concatWithJoinAndCon(n):
    output = ''.join(['num' for num in range(1, n)])
    print(f'Memory :: {sys.getsizeof(output)}')
    return output


def main():
    concatWithPlus(100000)
    concatWithJoin(100000)
    concatWithStingIO(100000)
    concatWithJoinAndCon(100000)


if __name__ == '__main__':
    main()
