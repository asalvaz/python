#Listas y diccionarios
'''
'''

class Inventario:    
    def __init__(self):
        self.buscar = None
    def buscar_producto(self):
        #Inventario con nombre de producto y costo
        producto = {
            'nombre': '',
            'precio': 0.0
        }

        inventario = []

        #Para agregar un elemento a una lista usar append

        inventario.append(
            {
                'nombre':'clavo',
                'precio':0.30
            }
        )

        inventario.append(
            {
                'nombre':'tornillo',
                'precio':0.30
            }
        )

        print(inventario)        
        #print(producto['nombre'] producto for producto in inventario)
        for p in inventario:
            print('_________')
            print("\t producto ", producto['nombre']) 
            print("\t precio ", producto['precio'])
        mensaje = 'Introduce el nombre de un producto a buscar: '
        try:
            self.buscar = input(mensaje)
        except:
            self.buscar =""
        #print([producto if producto['nombre'] == buscar else "No se encontro " + buscar for producto in inventario ])
        arreglo = [producto for producto in inventario if producto['nombre'] == self.buscar]
        if(arreglo):
            print (arreglo)
        else:
            print("No se encontro el articulo:" + self.buscar)


class programacion_ATS:
    def __init__(self):
        self.diccionario = {"azul":"blue","rojo":"red","verde":"green"}
        

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



obj1 = programacion_ATS()
obj1.imprime_diccionario()
obj1.imprime_diccionario("azul")
obj1.agregar_diccionario()
obj1.imprime_diccionario()
obj1.imprime_diccionario("amarillo")
obj1.agregar_diccionario("rosa","pink")
obj1.imprime_diccionario()
obj1.modificar_diccionario("rosa","patricio")
obj1.imprime_diccionario("rosa")
obj1.imprime_diccionario()
obj1.modificar_diccionario("negro","black")
obj1.imprime_diccionario()
obj1.eliminar_diccionario("rosa")
obj1.imprime_diccionario()