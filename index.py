if 5>3:
    print()
 #   print ('5 es mayor a 3')
##
if 3>5:
    print()
  #  print ('5 No es mayor a 3')
##
    

x = 5
y = 'abfasdfadsf'

#print (x, y)

email = 'correo@taf.com'

#print(email)

a,b,c = 'ana', 'beto', 'carla'

#print(a,b,c)


valor1, valor2, valor3 = 'ana1', 'beto2', 'carla3'

#print(valor1, valor2, valor3)

inicio = 'Hola '
final = 'Mundo'

#print(inicio + final)

palabra = 'hola mundo'
oracion = "Hola Mundo comilla doble"

entero = 20 # Integer
conDecimales = 20.2 # Float
complejos = 1j

#print (palabra, oracion, entero, conDecimales, complejos)

lista = [1,2,3]
lista2=lista.copy()
lista.append(4)
#lista.clear()
#print (lista)
#print (lista2)
#print(lista, lista2.count(3))
#print(len(lista))
lista.pop() # Elimina el ultimo elemento
lista2.pop()
#print (lista)
#print (lista2)
#print(lista, lista2.count(3))
#print(len(lista))
lista.remove(1)
#print (lista)
#print (lista2)
#print(lista, lista2.count(3))
#print(len(lista))


lista.reverse()
#print(lista)

lista.sort() #Ordena las listas

tupla = (1,2,3,7,9,10)
#print (tupla)
#print(tupla.count(2))
#print(tupla.index(9))

#podemos transformar una tupla en list para obtener mejores funciones

listadetupla = list(tupla)
listadetupla.append(1241123) #las tuplas no tienen append ni nada más que count e index fin.
#print (listadetupla) 

rango = range(4) #Los rangos sirven para las iteraciones
#print (rango)

#Diccionarios (En ves de indices se usan strings para acceder a un elemento en particular)
diccionario = {
    "marca": "Ford",
    "modelo": "Figo",
    "año": 2016
}

#print(diccionario)
#print(diccionario['modelo'])
#print(diccionario['año'])
#print(diccionario.get('año'))

diccionario['marca'] = "Chevrolet"
diccionario['modelo'] = "Camaro"
diccionario['año'] = "2023"

print(diccionario)

diccionario['color'] = "Guinda"
diccionario['ronronea'] = "Si"
#print(diccionario)

#diccionario.pop('ronronea') #Elimina el elegido
#diccionario.popitem() #Elimina el ultimo
#print(diccionario)
#del diccionario['ronronea']
####diccionario.clear() ## Elimina todos los objetos
#print(diccionario)
#copiadiccionario = diccionario.copy()
#print(copiadiccionario)

dicmayor = diccionario.copy()
print (dicmayor)
otrocarro = dict(
    marca = "Ford",
    modelo = "Figo",
    año = 2016
)
print (otrocarro)