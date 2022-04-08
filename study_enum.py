from enum import Enum
from enum import unique
from enum import auto

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

def main():
    print(Color.RED.name)

if __name__ == '__main__':
    main()
