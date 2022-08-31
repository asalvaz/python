#Objetos Clases y Herencias

class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludo(self):
        print("Hola!, me llamo", self.nombre, self.apellido)


class Admin(Usuario):
    def superSaludo(self):
        print("Hola!, me llamo", self.nombre, "y soy Admin")

""" usuario = Usuario("Foca","Feliz")
usuario2 = Usuario("Felipe","Feliz")

print(usuario.nombre, usuario.apellido, usuario2.nombre, usuario2.apellido)
usuario.saludo()
usuario2.saludo()

admin = Admin("Super", "Feliz")
admin.saludo()
admin.superSaludo() """

class Animal:
    def __init__ (self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    def saludo(self):
        print("Hola, soy un", self.tipo, "y mi sonido es:", self.onomatopeya)

class Gato(Animal):
    tipo = "gato"
    def __init__(self,nombre,onomatopeya):
        Animal.__init__(self, nombre, onomatopeya)
        print("alskjdaksjdlkasj")

class Perro(Animal):
    tipo = "perro"
    def __init__(self,nombre,onomatopeya):
        super().__init__(nombre,onomatopeya)
        print("instanciando un perruky")

class Canario(Animal):
    tipo = "canario"
    
class Digestion:
    def __init__ (self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya

gato = Gato("Fluffy", "Miau")
gato.saludo()
perro = Perro("Firulais", "Guau")
perro.saludo()
canario = Canario("El pollito", "piopio")
canario.saludo()