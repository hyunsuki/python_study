class Singleton(object):
    __instance = None

    def __init__(self):

        if not Singleton.__instance:
            print('No object yet')

        else:
            print('Object already exist', self.get_instance())

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


def main():
    s = Singleton()  # 클래스 초기화는 했지만, 아직 객체 생성x
    print('Create Object', Singleton.get_instance())
    s1 = Singleton()


if __name__ == '__main__':
    main()
