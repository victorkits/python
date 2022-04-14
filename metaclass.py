def howdy(self, you):
    print("Howdy, " + you)


class A:
    class B:
        class C:
            def me(self):
                print(self.__module__)
                print(type(self).__name__)
                print(type(self).__qualname__)
                print(repr(self))


MyList = type('MyList', (list,), dict(x=42, howdy=howdy))

if __name__ == '__main__':
    a = A.B.C()
    a.me()

    # ml = MyList()
    # ml.append("Camembert")
    # print(ml)
    # print(ml.x)
    # ml.howdy("John")
    #
    # print(ml.__class__)
    # print(ml.__class__.__class__)
