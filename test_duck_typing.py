class Parrot:
    def fly(self):
        print('Parrot flying')


class Airplane:
    def fly(self):
        print('Airplane flying')


class Whale:
    def swim(self):
        print('Whale swimming')


def lift_off(entity):
    entity.fly()

def main():
    parrot = Parrot()
    airplane = Airplane()
    whale = Whale()

    lift_off(parrot)
    lift_off(airplane)
    lift_off(whale)


if __name__ == '__main__':
    main()
