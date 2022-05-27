class Car:
    count = 0

    def __init__(self):
        self.number = None
        self.brand = None
        self.owner = None


class CarManager:

    def __init__(self): pass

    def create(self):
        Car.count += 1
        return Car()

    def scrap(self):
        Car.count -= 1


def main():
    cm = CarManager()
    print(f'CAR COUNT :: {Car.count}')
    print(f'MADE NEW CAR :: {cm.create()}')
    print(f'CAR COUNT :: {Car.count}')
    print(f'SCRAP CAR :: {cm.scrap()}')
    print(f'CAR COUNT :: {Car.count}')



if __name__ == '__main__':
    main()
