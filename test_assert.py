def main():
    """
    This file is for studing assert
    """
    name = "1KimHyunsuk"
    assert name[0].isalpha(), "이름의 맨 처음은 알파벳으로 시작해주세요"

if __name__ == '__main__':
    print("="*100)
    print(main.__doc__)
    print("="*100)
    main()
