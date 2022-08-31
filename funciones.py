def miFuncion():
    print("Mi primera funcion")
""" miFuncion()
miFuncion()
miFuncion()
miFuncion() """

def imprimeDato(*nombre):
        print("El nombre completo es:", nombre[0], nombre[1])



#imprimeDato("chanchito","feliz","qwser","asdsa")

def nombreCompleto(apellido, nombre):
    print(nombre, apellido)

#nombreCompleto(nombre="chanchito", apellido="Feliz")


def nombreCompleto2(**kwargs): #Keywords args
    print(kwargs['nombre'], kwargs['apellido'])

#nombreCompleto2(nombre = 'Chanchiiito', apellido='feliz')

def mifuncion2(argumento = 'chanchito'):
    print(argumento)

mifuncion2()
mifuncion2('pablito')