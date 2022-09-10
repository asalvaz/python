# Patrones de diseño con Python y PHP

#ABSTRACT FACTORY

class FactoryPatternDemo(object):
    """docstring for FactoryPatternDemo"""
    def __init__(self):
        pass

    def execute(self):
        #get shape factory
        shapeFactory = FactoryProducer.getFactory(False)
        #get an object of Shape Rectangle
        shape1 = shapeFactory.getShape("RECTANGLE")
        #call draw method of Shape Rectangle
        shape1.draw()
        #get an object of Shape Square 
        shape2 = shapeFactory.getShape("SQUARE")
        #call draw method of Shape Square
        shape2.draw()
        #get shape factory
        shapeFactory1 = FactoryProducer.getFactory(True)
        #get an object of Shape Rectangle
        shape3 = shapeFactory1.getShape("RECTANGLE")
        #call draw method of Shape Rectangle
        shape3.draw()
        #get an object of Shape Square 
        shape4 = shapeFactory1.getShape("SQUARE")
        #call draw method of Shape Square
        shape4.draw()

# Paso 3
class AbstractShapeFactory(object):
    """docstring for AbstractShapeFactory"""
    def __init__(self):
        pass

    def getShape(self, shapeType):
        pass
##Fin Paso 3

#Paso 4
class ShapeFactory(AbstractShapeFactory):
    def getShape(self, shapeType):
        if(shapeType is None):
            return None
          
        if(shapeType == "CIRCLE"):
            return  Circle()    
        elif(shapeType == "RECTANGLE"):
            return Rectangle()
        elif(shapeType == "SQUARE"):
            return Square()
          
        return None

class RoundedShapeFactory(AbstractShapeFactory):
    def getShape(self, shapeType):
        if(shapeType is None):
            return None
          
        if(shapeType == "CIRCLE"):
            return  RoundedCircle()    
        elif(shapeType == "RECTANGLE"):
            return RoundedRectangle()
        elif(shapeType == "SQUARE"):
            return RoundedSquare()
          
        return None
# Fin Paso 4

# Shape Interface
class Shape(object):
    """docstring for Shape"""
    def __init__(self):
        pass

    def draw(self):
        print("Dentro de Shape::draw metodo")

# Paso 1
# RoundedShape Interface
class RoundedShape(Shape):
    def draw(self):
        print("Dentro de RoundedShape::draw metodo")
# Fin Paso 1


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



##  Paso 2
# implements
class RoundedCircle(RoundedShape):
    """docstring for Circle"""
    def __init__(self):
        super(RoundedShape, self).__init__()
    
    def draw(self):
        print("Dentro de RoundedCircle::draw metodo")

class RoundedSquare(RoundedShape):
    """docstring for Square"""
    def __init__(self):
        super(RoundedShape, self).__init__()
    
    def draw(self):
        print("Dentro de RoundedSquare::draw metodo")

class RoundedRectangle(RoundedShape):
    """docstring for Rectangle"""
    def __init__(self):
        super(RoundedShape, self).__init__()
    
    def draw(self):
        print("Dentro de RoundedRectangle::draw metodo")
## Fin Paso 2

# Paso 5
class FactoryProducer(object):
    """docstring for FactoryProducer"""
    def __init__(self, arg):
        pass

    def getFactory(isRounded = True):
        if isRounded:
            return RoundedShapeFactory()
        else:
            return ShapeFactory()
# Fin Paso 5


factoryPatternDemo = FactoryPatternDemo()
factoryPatternDemo.execute()