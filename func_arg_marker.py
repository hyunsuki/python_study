class FuncTest:
    def __init__(self):pass

    def standard_arg(self, arg):
        print(arg)

    def positional_only_arg(self, arg, /):
        print(arg)

    def kwd_only(self, *, arg):
        print(arg)

    def combined_example(self, positional_only, /, standard, *, kwd_only):
        print(positional_only, standard, kwd_only)

class UseCase:
    def foo(self, name, /, **kwds):
        return 'name' in kwds

def main():

     uc = UseCase()
     print(uc.foo(1, **{'name':2}))

#    ft = FuncTest()
# 
#    ft.combined_example(1, 2, 3)
#    ft.combined_example(1, 2, kwd_only=3)
#    ft.combined_example(1, standard=2, kwd_only=3)
#    ft.combined_example(positional_only=1, standard=2, kwd_only=3)

if __name__ == '__main__':
    main() 
