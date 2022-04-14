class Singleton:
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print(" __init__ method called..")
        else:
            print("Instance already created:", self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


# =========================================================

class OnlyOne(object):
    class __OnlyOne:
        def __init__(self):
            self.val = None

        def __str__(self):
            return 'self ' + self.val

    instance = None

    def __new__(cls):  # __new__ always a classmethod
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__OnlyOne()
        return OnlyOne.instance

    # def __getattr__(self, name):
    #     return getattr(self.instance, name)
    #
    # def __setattr__(self, name):
    #     return setattr(self.instance, name)


class Borg:
    __shared_state = {"1": "2"}

    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state
        pass


if __name__ == '__main__':
    # s = Singleton()  ## class initialized, but object not created
    # print("Object created", Singleton.getInstance())  # Object gets created here

    # x = OnlyOne()
    # x.val = 'sausage'
    # print(x)
    # y = OnlyOne()
    # y.val = 'eggs'
    # print(y)
    # z = OnlyOne()
    # z.val = 'spam'
    # print(z)
    # print(x)
    # print(y)

    b = Borg()
    b1 = Borg()
    b.x = 4
    b.y = 5
    print("Borg Object 'b': ", b)  ## b and b1 are distinct objects
    print("Borg Object 'b1': ", b1)
    print("Object State 'b':", b.__dict__)  ## b and b1 share same state
    print("Object State 'b1':", b1.__dict__)  ## b and b1 share same state
