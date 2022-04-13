from enum import Enum

class Color(Enum):
    RED = 0
    BLUE = 1
    GREEN = 2

def main():
    print(Color.RED.name)

if __name__ == '__main__':
    main()
