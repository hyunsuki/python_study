import sys
import weakref


class Dict(dict):
    pass


class List(list):
    pass


def main():
    print('\n' + '='*28 + 'WEAKREF LIST' + '='*28)
    list_obj = List([1, 2, 3])
    print(f'obj reference count :: {sys.getrefcount(list_obj)}')
    copy_list_obj = weakref.ref(list_obj)
    print(f'copy_list_obj :: {copy_list_obj()}')
    print(f'after weakref, obj reference count :: {sys.getrefcount(list_obj)}')

    print('\n' + '='*28 + 'WEAKREF DICT' + '='*28)
    dict_obj = Dict(red=1, green=2, blue=3)
    print(f'obj reference count :: {sys.getrefcount(dict_obj)}')
    copy_dict_obj = weakref.ref(dict_obj)
    print(f'copy_dict_obj :: {copy_dict_obj()}')
    print(f'after weakref, obj reference count :: {sys.getrefcount(dict_obj)}')


if __name__ == '__main__':
    main()
