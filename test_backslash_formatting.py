class testFormat:

    def __init__(self):
        self.back_slash = '\\'

    def useVariable(self):
        my_string = f'This is a backslash :: {self.back_slash}'
        print(my_string)

    def useReplace(self):
        my_string = f'This is a backslash :: target'.replace('target', '\\')
        print(my_string)

    def useChr(self):
        my_string = f'This is a backslash :: {chr(92)}'
        print(my_string)


def main():
    tf = testFormat()
    print('\n**USE VARIABLE**')
    tf.useVariable()
    print('\n**USE REPLACE**')
    tf.useReplace()
    print('\n**USE CHR**')
    tf.useChr()


if __name__ == '__main__':
    main()
