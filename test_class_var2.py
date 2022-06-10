class Dog:

    tricks = []

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)


def main():
    dog1 = Dog('Fido') 
    dog2 = Dog('Buddy')
    dog1.add_trick('roll over')
    dog2.add_trick('play dead')
    print(dog1.tricks)


if __name__ == '__main__':
    main()
