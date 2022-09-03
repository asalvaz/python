# Patrones de diseño con Python y PHP

# SINGLETON

class OnlyOne(object):
    
    #Paso 1
    class __OnlyOne:
        def __init__(self):
            self.val = None
        def __str__(self):
            return 'self: ' + self.val
    #Fin Paso 1
    instance = None

    #Paso 2
    def __new__(cls): # __new__ always a classmethod. 
    # Este método se llama antes que __init__ y es el único que sirve para customizar la creación del objeto
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__OnlyOne() # Creo la instancia
        return OnlyOne.instance # Devuelvo
    #Fin Paso 2

    #Paso 3
    def __getattr__(self, name): 
    # Se llama cuando el atributo no se encuentra 
    # en el lugar usual getattr()
        return getattr(self.instance, name)
    def __setattr__(self, name): 
    # Se llama cuando se tiene que guardar un atributo. 
    # Se llama en vez de la forma normal setattr()
        return setattr(self.instance, name)
    #Fin Paso 3

x = OnlyOne()
x.val = 'tomate'
print(x)


y = OnlyOne()
y.val = 'lechuga'
print(y)

z = OnlyOne()
z.val = 'zanahoria'
print(z)

print(x)
print(y)