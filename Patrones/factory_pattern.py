# Patrones de diseño con Python y PHP

#FACTORY

class FactoryPatternDemo(object):
    """docstring for FactoryPatternDemo"""
    def __init__(self):
        pass

    def execute(self):
        shapeFactory = ShapeFactory()

        #get an object of Circle and call its draw method.
        shape1 = shapeFactory.getShape("CIRCLE")

        #call draw method of Circle
        shape1.draw()

        #get an object of Rectangle and call its draw method.
        shape2 = shapeFactory.getShape("RECTANGLE")

        #call draw method of Rectangle
        shape2.draw()

        #get an object of Square and call its draw method.
        shape3 = shapeFactory.getShape("SQUARE")

        #call draw method of square
        shape3.draw()


class ShapeFactory(object):
    """docstring for ShapeFactory"""
    def __init__(self):
        pass

    def getShape(self, shapeType):
        if(shapeType is None):
            return null
          
        if(shapeType == "CIRCLE"):
            return Circle()
        elif(shapeType == "RECTANGLE"):
            return Rectangle()
        elif(shapeType == "SQUARE"):
            return Square()
          
        return null

# Shape Interface
class Shape(object):
    """docstring for Shape"""
    def __init__(self):
        pass

    def draw(self):
        pass

# implements
class Circle(Shape):
    """docstring for Circle"""
    def __init__(self):
        super(Shape, self).__init__()
    
    def draw(self):
        print("Dentro de Circle::draw metodo")

class Square(Shape):
    """docstring for Square"""
    def __init__(self):
        super(Shape, self).__init__()
    
    def draw(self):
        print("Dentro de Square::draw metodo")

class Rectangle(Shape):
    """docstring for Rectangle"""
    def __init__(self):
        super(Shape, self).__init__()
    
    def draw(self):
        print("Dentro de Rectangle::draw metodo")




factoryPatternDemo = FactoryPatternDemo()
factoryPatternDemo.execute()