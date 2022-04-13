import argparse # python ver 3.2 추가

class ArgParseManager:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
           # prog='game.py', # default=sys.argv[0]
            usage='''\nCONSOLE MODE -> python game.py console [config file path]
    BOT MODE -> python game.py bot [botcount(default=10)] [config file path]''',
            add_help=False
        )

def main():
    am = ArgParseManager()
    print(am.parser.prog)
    print(am.parser.usage)

if __name__ == '__main__':
    main()
