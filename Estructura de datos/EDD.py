class EDD:
    pass
    def __init__(self):
        self.lista = [1,2,3,'abc']
        self.numero = 30
        self.estrin = "haha"

    def imprimelista(self):
        print(self.lista)

nombre = input("Hola. Como te llamas?\n")
edad = input("Cuantos años tienes?\n")
esMayorDeEdad = int(edad) >= 18
if(esMayorDeEdad):
    print ("Es mayor de edad")
else:
    print("Página solo para mayores de edad")
Estructura = EDD()
Estructura.imprimelista()
print(f"Hola núm  {Estructura.estrin} {Estructura.numero} ")
print("Hola " + Estructura.estrin + "núm" +  str(Estructura.numero) )

