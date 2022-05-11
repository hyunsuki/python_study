from io import StringIO


class FileManager:

    def __init__(self):
        pass

    def reader(self, f):
        for line in f.readlines()[::-1]:
            
            print(line.strip().split(','))


def main():
    fm = FileManager()
    src = '''\
    20,40
    50,90
    77,22
    '''
    fm.reader(StringIO(src))


if __name__ == '__main__':
    main()
