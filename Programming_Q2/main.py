from Prueba_FactoryPattern.ClassFactorys.ShapeFactory import ShapeFactory


def main():
    shapes = ['circle', 'triangle', 'square']
    for shape in shapes:
        shape = ShapeFactory.getShape(shape)
        shape.draw()

    pass


if __name__ == '__main__':
    main()
