from abc import ABCMeta
from abc import abstractmethod


class Command(metaclass=ABCMeta):

    @abstractmethod
    def excute(self):
        pass


class KeyBoardCommand(Command):

    @classmethod
    def excute(self):
        return KeyBoard.getInput()


class KeyBoard:

    @classmethod
    def getInput(cls):
        client_input = input('INPUT: ')

        if client_input.strip() == '':
            raise Exception('Input is empty')

        if not client_input.isdigit():
            raise Exception('Input is not isdigit')

        return int(client_input)


def main():
    kbc = KeyBoardCommand.excute()


if __name__ == '__main__':
    main()
