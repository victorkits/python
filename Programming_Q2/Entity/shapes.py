from abc import abstractmethod, ABC


class Shape(ABC):

    @staticmethod
    @abstractmethod
    def draw() -> None:
        raise NotImplemented


class Circle(Shape):

    @staticmethod
    def draw() -> None:
        print('Drawing circle')


class Square(Shape):

    @staticmethod
    def draw() -> None:
        print('Drawing square')


class Rectangle(Shape):

    @staticmethod
    def draw() -> None:
        print('Drawing rectangle')
