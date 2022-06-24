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
    user1.name = 'hyunsuki'
    user2.name = 'test_user'
    print(f"user1's id :: {id(user1)}")
    print(f"uesr1's name :: {user1.name}")
    print(f"user2's id :: {id(user2)}")
    print(f"uesr2's name :: {user2.name}")

    print('\n' + '='*7 + 'Non Singleton User class' + '='*7)
    user3 = User()
    user4 = User()
    user3.name = 'hyunsuki'
    user4.name = 'test_user'
    print(f"user3's id :: {id(user3)}")
    print(f"uesr3's name :: {user3.name}")
    print(f"user4's id :: {id(user4)}")
    print(f"uesr4's name :: {user4.name}")


if __name__ == '__main__':
    main()
