import pdb 


class Calculator:

    def __init__(self):
        pass

    def add(self, x, y):
       pdb.set_trace()
       print(x + y)
       return x + y

    def subtract(self, x, y):
       return x - y

    def multiply(self, x, y):
       return x * y

    def divide(self, x, y):
       return x / y


def main():
    c = Calculator()
    c.add(1, 2)


if __name__ == '__main__':
    main()    
