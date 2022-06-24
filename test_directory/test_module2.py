if __name__ == '__main__':
    from . import test_module

else:
    import test_module



def main():
    tc = test_module.TestClass()
    tc.printDoc()


if __name__ == '__main__':
    main()
