class SubjectInterface:
    def add(self, a, b):
        pass

    def sub(self, a, b):
        pass


class RealSubject(SubjectInterface):
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b


class ProxyClass(SubjectInterface):
    def __init__(self):
        self.subject = RealSubject()

    def add(self, a, b):
        return self.subject.add(a, b)

    def sub(self, a, b):
        return self.subject.sub(a, b)


def main():
    '''프록시 객체'''
    pc = ProxyClass()
    print(pc.add(100, 25))
    print(pc.sub(100, 25))


if __name__ == '__main__':
    main()
