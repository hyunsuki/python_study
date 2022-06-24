from status import *


class Characters:

    def __init__(self, hp=100, mp=100):
        self.hp = hp
        self.mp = mp

    def getHpInfo(self):
        return self.hp

    def getMpInfo(self):
        return self.mp


class Warrior(Characters):

    def __init__(self, hp=200, mp=100):
        super(Warrior, self).__init__(hp, mp)


class Wizard(Characters):

    def __init__(self, hp=100, mp=200):
        super(Wizard, self).__init__(hp, mp)


def main():
    wizard = Wizard()
    print(f'WIZARD HP :: {wizard.getHpInfo()}')


if __name__ == '__main__':
    main()
