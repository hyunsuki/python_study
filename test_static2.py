class Car:

    def __init__(self):
        self.number = None
        self.brand = None


class CarManager:
    car = Car()
    def __init__(self):
        self.car = CarManager.car

    def getNumber(self):
        return self.car.number

    def setNumber(self, number):
        self.car.number = number


def main():
    cm1 = CarManager()
    cm1.setNumber(1234)
    print(f'CAR NUMBER :: {cm1.getNumber()}')

    # 다른 곳에서 매니저 인스턴스
    cm2 = CarManager()
    print(f'CAR NUMBER :: {cm2.getNumber()}')


if __name__ == '__main__':
    main()
