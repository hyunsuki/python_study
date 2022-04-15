def returnInput():
    """This is docstring"""
    input_num = int(input('input wish number'))
    print('Input number :: %s'%input_num)

if __name__ == '__main__':
#    returnInput()
#    print(returnInput.__doc__)

    f = returnInput
    f()
    print(f.__doc__)


