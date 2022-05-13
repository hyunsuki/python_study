from io import StringIO
from io import BytesIO


class FileManager:

    def __init__(self):
        pass

    def readLine(self, file_object, size=-1):
        return file_object.readline(size).strip()

    def readLines(self, file_object, hint=-1):
            for line in file_object.readlines(hint):
                print(f"line :: {line.strip()}")


def main():
    fm = FileManager()

#    fm.readLine(StringIO(src))
#    for _ in range(10):
#        print(f'readline size={_} :: {fm.readLine(StringIO(src), size=_)}')

#    fm.readLines(StringIO(src))
#    fm.readLines(StringIO(src), -1)
#    fm.readLines(StringIO(src), 1)
#    fm.readLines(StringIO(src), -2)
#    fm.readLines(StringIO(src), 2)
#    fm.readLines(StringIO(src), -3)
    print(len(b'test\n'*10))
    print(len('test\n'*10))
    fm.readLines(BytesIO(b'test\n'*10), 10)
    fm.readLines(StringIO('test\n'*10), 10)


if __name__ == '__main__':
    main()
