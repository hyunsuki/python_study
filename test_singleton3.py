class User:

    def __init__(self):
        self.uid = None


class UserManager:
    __user_instance = None

    def __init__(self):
        self.user = self.getInstance()

    def getInstance(self):
        return self.__createUser() if UserManager.__user_instance is None else UserManager.__user_instance

    def __createUser(self):
        UserManager.__user_instance = User()
        return UserManager.__user_instance


def main():
    um1 = UserManager()
    um2 = UserManager()
    um1.user.name = 'hyunsuki'
    print(f'um1.user.name :: {um1.user.name}')
    print(f'um2.user.name :: {um2.user.name}')


if __name__ == '__main__':
    main()
