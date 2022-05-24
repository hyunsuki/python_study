class User:
    def __init__(self):
        self.name = None


class SingletonInstance:
    __instance = None

    @classmethod
    def __getInstance(cls):
        return cls.__instance

    @classmethod
    def instance(cls, *args, **kargs):
        cls.__instance = cls(*args, **kargs)
        cls.instance = cls.__getInstance
        return cls.__instance


class MyClass(User, SingletonInstance):
    pass


def main():
    print('\n' + '='*7 + 'Singleton User class' + '='*7)
    user1 = MyClass.instance()
    user2 = MyClass.instance()
    print(f"user1's id :: {id(user1)}")
    print(f"user2's id :: {id(user2)}")
    user1.name = 'hyunsuki'
    user2.name = 'test_user'
    print(f"uesr1's name :: {user1.name}")
    print(f"uesr2's name :: {user2.name}")
    print(f"user1's id :: {id(user1)}")
    print(f"user2's id :: {id(user2)}")
    print('\n' + '='*7 + 'Non Singleton User class' + '='*7)
    user3 = User()
    user4 = User()
    print(f"user3's id :: {id(user3)}")
    print(f"user4's id :: {id(user4)}")


if __name__ == '__main__':
    main()
