if 2>5 and "a"=="b":
    print("cy")
elif 2>5:
    print("reprosesando...")
else:
    print("ño")

    dato = input('Ingrese el dato: ')

    #print(dato)

    lista = ['Hola','Dato']

    if (lista.count(dato)) > 0:
        print("Hola")
    else:
        print("El dato no existe")


    numero1 = input("Numero: ")
    try:
        numero1 = int(numero1)
    except:
        numero1 = "issue"
    numero2 = input("Numero: ")
    try:
        numero2 = int(numero2)
    except:
        numero2 = "issue"


    if numero1 == "issue" or numero2 == "issue":
        print("solo numeros bro")
    else:
        print(numero1+numero2)