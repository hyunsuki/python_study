from io import StringIO


def main():
    output = StringIO()
    output.write('First line.\n')
    print('Second line.', file=output)

    contents = output.getvalue()

    output.close()

    print(contents)


if __name__ == '__main__':
    main()
