from turtle import left
import FuncionesT1
class decremental(FuncionesT1.FuncionesT1):
    pass

    def __init__(self):
            pass
    
class Arbol2():
    def __init__(self, key, left, right):
         self.key = key
         self.left = left
         self.right = right

#Lista aplanada preorder
    def addinpreorder(self):
        salida = []
        salida.append(self.key)

        if self.left != None:
            salidaL = self.left.addinpreorder()
            for e in salidaL:
                salida.append(e)
        if self.right != None:
            salidaR = self.right.addinpreorder()
            for e in salidaR:
                salida.append(e)
        return salida

#Arbol bidimencional:
class Nodo:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.arreglo = []
        
class Arbol3():
    def __init__(self, key):
        self.primarykey = Nodo(key)

    def addinpreorder(self, raiz, key):
        if raiz.key >= key:
            if raiz.left is None:
                  raiz.left = Nodo(key)
            else:
                self.addinpreorder(raiz.left, key)
        else:
            if raiz.right is None:
                  raiz.right = Nodo(key)
            else:
                self.addinpreorder(raiz.right, key)
        
    def add(self, key):
        self.addinpreorder(self.primarykey, key)

    def carga_arreglo(self, arreglo):
        
        arbolito = []
        for n in arreglo:
            arbolito = self.add(n)
        return arbolito

    def inorden(self):
        print("Imprimiendo árbol inorden: ")
        self.__inorden_recursivo(self.primarykey)
        print("")

    def __inorden_recursivo(self, nodo):
        if nodo is not None:
            self.__inorden_recursivo(nodo.left)
            print(nodo.key)#, end=", "
            self.arreglo = self.arreglo.append(nodo.key)
            self.__inorden_recursivo(nodo.right)
#Fin Arbol bidimencional


# arpropposed = {1,3,2}
# [8,7,5,4,3,5,4,3]

#objeto = Arbol2(1, Arbol2(2,None, None) , Arbol2(3,None,None))
arreglopropuesto = [8,7,5,4,3,5,4,3]
#objeto2 = FuncionesT1.Arbol3(arreglopropuesto[0])
objeto2 = Arbol3(arreglopropuesto[0])
arreglopropuesto.pop(0)
objeto2.carga_arreglo(arreglopropuesto)
#print(objeto2.primarykey.key)
objeto2.inorden()
#listasalida = objeto2.carga_arreglo(arreglopropuesto[])
#listasalida = objeto2.carga_arreglo(3) 
#print(listasalida)
#print(objeto2.addinpreorder())
#obj = decremental()

#long = obj.getdays(arpropposed) 
#print(str(long))
#print("intento decremental" + str(obj.intentodecremental(arpropposed, obj.getdays(arpropposed))))
#print("Repetidos" + str(obj.repetidos_tardados(arpropposed)))
#print("Repetidos rapido" + str(obj.repetidos_rapida(arpropposed)))
#print("decremental" + str(obj.bidecremental(arpropposed)))
#print("decremental" + str(obj.decremental(arpropposed)))
#print("decremental" + str(obj.couldbedecremental(arpropposed)))
