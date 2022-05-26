class User:

    def __init__(self):
        self.name = None


class UserManager:

    user = User()

    def __init__(self):
        self.user = UserManager.user

    def getUserName(self):
        return self.user.name

    def setUserName(self, name):
        self.user.name = name


class Action:

    def __init__(self):
        self.user_manager = UserManager()

    def login(self):
        print(self.user_manager.getUserName())
        self.user_manager.setUserName('hyunsuki')
        print(self.user_manager.getUserName())

class Page:

    def __init__(self):
        self.user_manager = UserManager()

    def setPage(self):
        print(self.user_manager.getUserName())
        self.user_manager.setUserName('user2')
        print(self.user_manager.getUserName())


def main():
    action = Action()
    action.login()
    page = Page()
    page.setPage()

if __name__ == '__main__':
    main()

