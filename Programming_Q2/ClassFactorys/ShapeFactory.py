from Prueba_FactoryPattern.Entity.shapes import *


class ShapeFactory:

    @staticmethod
    def getShape(shape_type):
        shape_types = {
            'circle': Circle,
            'square': Square,
            'triangle': Rectangle
        }
        return shape_types.get(shape_type, None)
