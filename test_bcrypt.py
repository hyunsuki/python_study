import bcrypt


class PasswordManager:

    def __init__(self):
        self.__salt = bcrypt.gensalt()

    def create_hashed_password(self):
        hashed_password = bcrypt.hashpw(bytearray(input('input your password: '), 'utf-8'), self.__salt)

    def check_password(self):


def main():
    pm = PasswordManager()


if __name__ == '__main__':
    main()
