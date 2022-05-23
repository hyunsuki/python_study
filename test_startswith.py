def test_startswith(string, prefix):
    return string.startswith(prefix)


def main():
    print(f'#USER_ID,USER_PW,NICK_NAME start with # :: {test_startswith("#USER_ID,USER_PW,NICK_NAME", "#")}')
    print(f'#USER_ID,USER_PW,NICK_NAME start with @ :: {test_startswith("#USER_ID,USER_PW,NICK_NAME", "@")}')


if __name__ == '__main__':
    main()
