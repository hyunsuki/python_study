def main():
    test_text = 'ab c\n\nde fg\rkl\r\n'
    sep = '\n'
    print(f'test text :: {test_text}')
    print(f'use split() by \\n :: {test_text.split(sep)}')
    print(f'test_text.splitlines() :: {test_text.splitlines()}')
    print(f'test_text.splitlines(keepends=True) :: {test_text.splitlines(keepends=True)}')


if __name__ == '__main__':
    main()
