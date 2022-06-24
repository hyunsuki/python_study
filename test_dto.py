class Test1 :

    def __init__(self) :
        self.__color = 'red'

    def getColor(self) :
        return self.__color

    def setColor(self, color) :
        self.__color = color

class Test2 :
    def __init__(self) :
        self.__color = 'red'

    @property
    def color(self) :
        return self.__color

    @color.setter
    def color(self, color) :
        self.__color = color

def main() :
    t1 = Test1()
    print(t1.getColor())
    t1.setColor('bule')
    print(t1.getColor())

    t2 = Test2()
    print(t2.color)
    t2.color = 'blue'
    print(t2.color)

if __name__ == '__main__' :
    main()
