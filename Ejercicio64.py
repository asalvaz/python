#Multiplicar 2 números sin utilizar el simbolo de multiplicación
a=2
b=9
resultado = 0

for x in range(a):
    resultado += b

print (resultado)

# ingresar nombre y apellido e imprimirlo al reves
nombre = 'Valeria'
apellido = 'Feliz'

concatenacion = nombre + ' ' + apellido

print(concatenacion)
print(concatenacion[::-1])

# escribir una función que encuentre el elemento menor de una lista

lista = [1, 2, 5, 3, 55, -24, -13]

menor = 'init'

for x in lista:
    if menor == 'init':
        menor = x
    else:
        menor = x if x < menor else menor

print('menor', menor)
# escribir una función que devuelva el volumen de una esfera por su radio
# 4/3 * pi * r ** 3

def calculaVolumen(r):
    return 4 / 3 * 3.14 * r ** 3

resultado = calculaVolumen(6)
print(resultado)
resultado = calculaVolumen(8)
print(resultado)
resultado = calculaVolumen(9)
print(resultado)
# escribir una función que indique si el usuario es mayor de edad

def esMayor(usuario):
    return usuario.edad > 17

class Usuario:
    def __init__(self, edad):
        self.edad = edad

usuario = Usuario(18)
usuario2 = Usuario(17)

resultado1 = esMayor(usuario)
resultado2 = esMayor(usuario2)

print(resultado1, resultado2)
# escribir una función que indique si un número es par o impar

def esPar(n):
    return n % 2 == 0

resultado3 = esPar(16)
print(resultado3)
# escribir una función que indique cuantas vocales tiene una palabra
palabra = 'Valeria'
vocales = 0
for x in palabra:
    y = x.upper()
    vocales += 1 if y == 'A' or y == 'E' or y == 'I' or y == 'O' or y == 'U' else 0

print(vocales)

# escribir una aplicación que reciba una cantidad infinita de números hasta
# decir basta, luego que devuelva la suma de los números ingresados

lista = []
print('Ingrese números y para salir escriba "basta"')
while True:
     valor = input('Ingrese valor: ')
     if valor == 'basta':
         break
     else:
         try:
             valor = int(valor)
             lista.append(valor)
         except:
             print('Dato no válido')
             exit()
             
resultado4 = 0 
for x in lista:

    resultado4 += x

print(resultado4)
# escribir una función que reciba nombre y apellido y los vaya agregando a
# un archivo
def agregaNombreAArchivo(nombre, apellido):
    c = open('nombrecompleto.txt', 'a')
    c.write(nombre + ' ' + apellido + '\n')
    c.close()

agregaNombreAArchivo('Valeria', 'Feliz')
agregaNombreAArchivo('Andres', 'Feliz')
agregaNombreAArchivo('Valeria', 'y Andres')
