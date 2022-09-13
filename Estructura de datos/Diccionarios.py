#Listas y diccionarios
'''
'''

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



buscar = input('Introduce el nombre de un producto a buscar: ')
#print([producto if producto['nombre'] == buscar else "No se encontro " + buscar for producto in inventario ])
arreglo = [producto for producto in inventario if producto['nombre'] == buscar]
if(arreglo):
    print (arreglo)
else:
    print("No se encontro el articulo:" + buscar)