
class SingletonMeta(type):
    """
    В Python класс Одиночка можно реализовать по-разному. Возможные способы
    включают себя базовый класс, декоратор, метакласс. Мы воспользуемся
    метаклассом, поскольку он лучше всего подходит для этой цели.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        else:
            cls._instances[cls].__init__(*args, **kwargs)
        return cls._instances[cls]


class Singleton1(metaclass=SingletonMeta):

    def __init__(self):
        print(f'a =')


if __name__ == "__main__":
    # Клиентский код.

    s1 = Singleton1()
    # s2 = Singleton1()
