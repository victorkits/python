if __name__ == '__main__':
    Terminator = type('Terminator', (object,), {'foo': 'bar'})


    class Meta(type):
        def __new__(mcs, name, base, dict):
            x = super().__new__(mcs, name, base, dict)
            x.attr = 100
            return x

    class New(metaclass=Meta):
        pass

    m = New()
    print(New.attr)
    print(m.attr)



    class T1(Terminator):
        pass

    x = T1
    print(x.foo)
    print(T1.foo)

