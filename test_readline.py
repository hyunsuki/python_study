import sys


class FileManager:

    def testReadline(self, file_path):
        with open(file_path, 'r', encoding='UTF-8') as f:
            one_line = f.readline()
            print(f'read file use read line :: {one_line}')
            print(f'len of line :: {len(one_line)}')

    def testReadlineWithSize(self, file_path, size=-1):
        with open(file_path, 'r', encoding='UTF-8') as f:
            print(f'size of line {size} :: {f.readline(size)}')

    def testReadlines(self, file_path):
        with open(file_path, 'r', encoding='UTF-8') as f:
            all_line = f.readlines()
            print(f'read all line :: {all_line}')
            print(f'size of first line :: {len(all_line[0])}')
            print(f'size of all line :: {len("".join(all_line))}')

    def testReadlinesWithHint(self, file_path, hint=-1):
        with open(file_path, 'r', encoding='UTF-8') as f:
            print(f'hint of line {hint} :: {f.readlines(hint)}')

    def testFileIter(self, file_path): 
        with open(file_path, 'r', encoding='UTF-8') as f:
            for line in f:
                print(line, end='')

        with open(file_path, 'r', encoding='UTF-8') as f:
            print(f'size of file object :: {sys.getsizeof(f)}')

        with open(file_path, 'r', encoding='UTF-8') as f:
            print(f'size of readlines(file object) :: {sys.getsizeof(f.readlines())}')

    def testRead(self, file_path, size=-1):
        with open(file_path, 'r', encoding='UTF-8') as f:
            print(f'f.read() :: {f.read()}')
            print(f'type(f.read()) :: {type(f.read())}')


def main():
    fm = FileManager()
#    print('**TEST READLINE**')
#    fm.testReadline('test_linesep.txt')
#    print('\n**TEST READLINE WITH SIZE**')
#    fm.testReadlineWithSize('test_linesep.txt', size=7)
#    fm.testReadlineWithSize('test_linesep.txt', size=8)
#    print('\n**TEST READLINES**')
#    fm.testReadlines('test_linesep.txt')
#    print('\n**TEST READLINES WITH HINT**')
#    fm.testReadlinesWithHint('test_linesep.txt', hint=12)
#    fm.testReadlinesWithHint('test_linesep.txt', hint=13)
#    fm.testFileIter('test_linesep.txt')
    fm.testRead('test_linesep.txt')


if __name__ == '__main__':
    main()


