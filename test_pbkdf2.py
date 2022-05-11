from hashlib import pbkdf2_hmac
from getpass import getpass
from icecream import ic


class LoginManager:

    def verifyUserInfo(self, id_, f):
        verify_result, user_info = self.verifyId(id_, f)

        if verify_result:
            self.verifyPassword(user_info)
                
    def verifyPassword(self, user_info):
        input_pw = pbkdf2_hmac('sha256', bytes(getpass('passward:'), encoding='utf-8'), b'salt', 30, 20)
        user_pw = user_info.split(',')[1]

        if user_pw == str(input_pw):
            print('Login success')
            return

        if not user_pw == str(input_pw):
            print('Login fail')
            return

    def verifyId(self, id_, f):

        for user_info in f.readlines():

            if user_info.split(',')[0] == id_:
                return True, user_info.strip()
                break

            if not user_info.split(',')[0] == id_:
                continue
        print('not found id')
        return False


def main():
    from io import StringIO
    lm = LoginManager()
    user_pw = pbkdf2_hmac('sha256', bytes('kims0206', encoding='utf-8'), b'salt', 30, 20)
    src = f''',
rlagustjr85,{user_pw}
rlagustjr86,{user_pw}'''
    lm.verifyUserInfo('rlagustjr85', StringIO(src))


if __name__ == '__main__':
    main()
