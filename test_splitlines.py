from icecream import ic


def main():
    ic('ab c\n\nde fg\rkl\r\n'.splitlines())
    ic('ab c\n\nde fg\rkl\r\n'.splitlines(keepends=True))
    ic('ab c\n\nde fg\rkl\r\n'.split('\n'))


if __name__ == '__main__':
    main()
