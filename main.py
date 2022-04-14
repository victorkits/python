from unittest.mock import MagicMock

from decorator import classdecorator


@classdecorator
class A:

    def __init__(self):
        self.a = 123

    def x(self, a):
        self.a = a


class B(object):
    pass


def main():
    a = [3, 4, 7, 'a', 90, 3, 5, 6, 7, 8]
    # print(a)
    # a.sort()

    # print(f"sorting {a}")

    b = set(a)
    print(b)


if __name__ == '__main__':
    main()
