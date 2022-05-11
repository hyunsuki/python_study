from character import Warrior
from character import Wizard


class Status:

    def __init__(self):
        self.warrior = Warrior()
        self.wizard = Wizard()


def main():
    status = Status()
    print(status.warrior.getHpInfo())


if __name__ == '__main__':
    main()
