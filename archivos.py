""" c = open("archivo.txt", "r") #Permiso de read = r | agregar más texto = a | # Modificar todo el archivo = w | crear archivo = x ( Si no esta creado lo creará si existe genera error)
#print(c.read()) #Read lee tood el archivo

print(c.readline()) # lee linea por linea
print(c.readline()) # lee linea por linea
print(c.readline()) # lee linea por linea
print(c.readline()) # lee linea por linea
print(c.readline()) # lee linea por linea 

c.write("\n linea nueva agregada")

#for x in c:
#    print(x)


c.close() #libera memoria

x = open("archivo.txt")

print(x.read())
 """

import os

if os.path.exists ("archivo.txt"):
    os.remove("archivo.txt") #Borra el archivo seleccionado
else:
    print("No existe")

#os.rmdir y ("elnombredelacarpeta") borra la carpeta seleccionada