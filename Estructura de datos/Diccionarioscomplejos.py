
class programacion_ATS2:
    def __init__(self):
        self.diccionario = {"Andres":{"edad":32,"altura":1.83},"Valeria":{"edad":30,"altura":1.75}}
        

    def imprime_diccionario(self, color="Todos"):
        #print(self.diccionario)
        if color == "Todos":
            print(self.diccionario)
        else:
            print(self.diccionario[color])


    def agregar_diccionario(self, nombre="amarillo", valor="yellow"):
        #print(self.diccionario)
        self.diccionario[nombre] = valor

    def modificar_diccionario(self, nombre, valor):
        #print(self.diccionario)
        self.diccionario[nombre] = valor

    def eliminar_diccionario(self, nombre):
        #print(self.diccionario)
        del self.diccionario[nombre]

obj2 = programacion_ATS2()
obj2.imprime_diccionario("Andres")
obj2.imprime_diccionario("Valeria")
