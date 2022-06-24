import sys
import weakref


class MyDict(dict): pass


def main():
    my_dict = MyDict()
    my_dict['apple'] = 100
    my_dict['orange'] = 30    
   
    print(f'my_dict :: {my_dict}') 
    print(f"my_dict's reference counting :: {sys.getrefcount(my_dict)}")
    proxy_dict = weakref.proxy(my_dict) # 프록시 객체 생성
    print(f'proxy_dict :: {proxy_dict}')
    print(f"my_dict's reference counting :: {sys.getrefcount(my_dict)}")

    my_dict = None
    print(f'proxy_dict :: {proxy_dict}')


if __name__ == '__main__':
    main()
