from cgi import print_form


class nombreclaseimp:
    def __init__(self, param1, param2, param3):
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3

    def displayObjeto(self):
        print(f"El parametro es : {self.param1}")
        print(f"Nuestro parametro dos es : {self.param2}")
        print(f"El último parametro es : {self.param3}")

    def adios(self):
        print(f"Mensaje de despedida para {self.param1} {self.param2} {self.param3}")

class hija(nombreclaseimp):
    def greet(self):
        print(f"Hola, mi nombre es {self.param1}")
        super().displayObjeto()
        super().adios()

objeto1 = hija("parametro 1", "parametro 2", "parametro tres")
objeto1.greet()

Objeto2 = hija("Valeriana", "de", "Salcedo")
Objeto2.greet()
