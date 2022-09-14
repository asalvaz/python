if __name__ == '__main__':
    lista=[]

    n = "print"
    n = n.split(" ")
    print (len(n))
    if n[0] == "print":
        print(lista)
    else:
        if len(n) == 3:
            comando = "lista." + n[0] + "(" + n[1] + "," + n[2] +")"
        elif len(n) == 2:
            comando = "lista." + n[0] + "(" + n[1] + ")"
        else: 
            comando = "lista." + n[0] + "()"

    print(lista)
    #eval(comando)
    print(lista)


    def insertar(posicion, valor):
        lista.insert(posicion, valor)
        return lista
        
    def imprimir():
        print(lista)

    def agregar(valor):
        lista.append(valor)
    
    def borrar_primero(valor):
        lista.remove(valor)

    def hace_pop():
        lista.pop()
    
    def reversa():
        lista.reverse()
    
    insertar(0, "hola")
    agregar("mundo")
    imprimir()
    