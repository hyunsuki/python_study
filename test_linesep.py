def main():
    with open('test_linesep.txt', 'a') as f:
         f.write('    test')
         f.write('    \rtest')
         f.write('    \ntest')
         f.write('    \r\ntest')
         f.write('test')
         f.write('test\r\n')
         f.write('test')

    with open('test_linesep.txt', 'r') as f:
         full_contents = f.readlines()
         print(full_contents)
         print(''.join(full_contents).splitlines())


if __name__ == '__main__':
    main()
