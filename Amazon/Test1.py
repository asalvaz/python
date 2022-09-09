from cgi import FieldStorage
from operator import index
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
         #   self.arreglo = self.arreglo.append(nodo.key)
            self.__inorden_recursivo(nodo.right)
#Fin Arbol bidimencional

#Arbol experimental
class Nodo:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.arreglo = []
        
class Arbol():
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
         #   self.arreglo = self.arreglo.append(nodo.key)
            self.__inorden_recursivo(nodo.right)
    
    def recorridoB(self, lista, numrecorridos=800000):
        anterior = lista[0]
        marcha=0
        firstone = 0
        indice = 0
        for n in lista:
            if indice > 0:
                if n+1 == lista[indice-1] and marcha < numrecorridos:
                    marcha +=1
                    #print("enlistado en: " + str(marcha+1))
                    #print(lista[indice])
                else:
                    firstone=indice-marcha-1
                    lastone= indice
                    print(str(firstone) + " " + str(lastone))
                    extraccion = lista[firstone:lastone]
                    print(extraccion)
                    if marcha > 1:
                        self.recorridoB(extraccion,len(extraccion)-2)
                    elif numrecorridos != 800000 and  len(lista)> 2:
                        #print(str(lista) + " [ " + str(len(lista)) + " - " + str(marcha) + " : " + str(len(lista)) + ", " +  str(len(lista)) + "-2")
                        #print(lista[len(lista)-marcha-1:len(lista)])
                        self.recorridoB(lista[len(lista)-marcha-1:len(lista)],len(lista)-2)
                    marcha=0
            indice = indice +1
        if indice == len(lista) and marcha>0:
            firstone=indice-marcha-1
            lastone= indice
            print(str(firstone) + " " + str(lastone))
            extraccion = lista[firstone:lastone]
            print(extraccion)
            if marcha > 1:
                self.recorridoB(extraccion,len(extraccion)-2)
            elif numrecorridos != 800000 and  len(lista)> 2:
                #print(str(lista) + " [ " + str(len(lista)) + " - " + str(marcha) + " : " + str(len(lista)) + ", " + str(len(lista)) + "-2")
                #print(lista[len(lista)-marcha-1:len(lista)])
                self.recorridoB(lista[len(lista)-marcha-1:len(lista)],len(lista)-2)
                
            marcha=0
            
#Ya se tiene la extracción. ahora toca realizar el arbol.
#Fin Arbol experimental

#
# Recorridos "decrementales":
# #
class recorridos:
    def obtiene_arreglo(self, n):
        lista=list(n)
        arreglo_esperado = []
        #if(n < lista):
        if(lista):
            #for i in n:
                #print(i, end=", ")
            #return n
            arreglo_esperado = self.obtiene_datos(lista)
            ###for i in arreglo_esperado:
                ###print(i, end=", ")
            ###print("\n" + str(arreglo_esperado))
            #Aquí podría ir un return del valor final
            return arreglo_esperado
        else:
            raise Exception("Dato no es una lista, favor de ingresar una lista")

    def obtiene_datos(self, lista):
        longitud_arreglo = len(lista)
        inicio = 2
        contador = 1
        contador_2 = 1
        tamano_arreglo_a_extraer = 0
        arreglo_inicio = []
        arreglo_final_final = []
        primero_comparar = 0
        ultimo_comparar = 0
        #Este ciclo se usa para realizar las comparaciones en cada longitud posible
        for inicio in lista:
            ###print("Inicio for: " + str(contador))
            if(False):
                pass
            #if contador == 1:  #ACTIVAR ESTE IF SI REQUERIMOS EL ARREGLO INICIAL EN UN SOLO MOMENTO [1 2 3 4 5 6 7 8], desactivarlo si requerimos el arreglo separado [1] [2] [3]... [n]
            #    for inicio in lista:
            #        arreglo_inicio.append(inicio)
            #    arreglo_final_final.append(arreglo_inicio)
            else:
                tamano_arreglo_a_extraer = contador
                #Este ciclo se usa para obtener los datos de la lista la cantidad de veces requerida según el contador 
                arreglo_temporal=[]
                Flag_todos_son_consecutivos = False
                temp_numero_anterior = 0
                for indice in lista:
                    #comparacion = checador_relaciones_polimorficas = Número de veces a comparar
                    #lista_extraida_a_revisar = la extracción [1,2] [2,3] [2,4]
                    #if(checador_relaciones_polimorficas<=lista_extraida_a_revisar):
                    lucky_number =(longitud_arreglo+1-tamano_arreglo_a_extraer)
                    if(lucky_number >= contador_2):
                        ###print("Generará el list siempre y cuando sean iguales los números " + str(indice) + " " + str(contador_2))
                        Flag_todos_son_consecutivos = self.extraer_arreglo_si_decrece(lista[(contador_2-1):(contador_2-1+contador)])
                        if(Flag_todos_son_consecutivos):
                            arreglo_temporal.append(lista[(contador_2-1):(contador_2-1+contador)])
                #        #En el primero solo asigna el valor al circuito mediante la variable principal
                #        if(contador_2==1):
                #            temp_numero_anterior = indice
                #            Flag_todos_son_consecutivos=True
                #        #si es uno más que el anterior continua y agregalo al arreglo temporal"
                #        elif(temp_numero_anterior-1 == indice):
                #            arreglo_temporal.append(indice)
                #            Flag_todos_son_consecutivos=True
                #        else:
                #            Flag_todos_son_consecutivos=False
                #            contador_2 = lucky_number+1
                #            continue
                        contador_2 = contador_2 + 1
                        #compararla()
                        #for indice in range(contador):
                        #pass
                            #En este ciclo se ingresara el arreglo dividido en la fracción correspondiente y se comparará si el ciclo se agrega o no
                    else:
                        #print("No se genera porque: LN:" + str(lucky_number) + "es mayor al " + str(contador_2))
                        #print(str(longitud_arreglo) + "+1 -" + str(tamano_arreglo_a_extraer) + "< " + str(contador_2))
                        #print(str(lucky_number) + " Esto no lo genera porque ya sobrepaso el limite:"+ str(tamano_arreglo_a_extraer) + " " + str(longitud_arreglo))
                        continue
                #print("contador", end=":")
                #print(indice)
                if(not arreglo_temporal):
                    pass
                else:
                    #print(arreglo_temporal)
                    arreglo_final_final.append(arreglo_temporal)
                contador_2 = 1
            contador +=1
        return arreglo_final_final

    ## HACE FALTA MEJORAR ESTE METODO PARA QUE CONFIRME LOS DECREMENTALES
    def extraer_arreglo_si_decrece(self, lista):
        #print("Se hace recorrido de la lista: " + str(lista) + " Y se confirma que es aceptable")
        listavacia = []
        lista_ordenada = lista.copy()
        lista_ordenada.sort(reverse=True)
        if(lista != listavacia and lista == lista_ordenada):
            if(self.decrece(lista)):
                return True
            else:
                return False
        else:
            return False



    # Decrece
    # 
    #         
    def decrece(self, lista):
        longitud = len(lista)
        contador = 0
        temp_numero_anterior = 0
        Flag_todos_son_consecutivos = False
        if longitud == 1:
            return True
        for indice in lista:
            if(contador==0):
                temp_numero_anterior = indice
                Flag_todos_son_consecutivos=True
                contador += contador + 1
            #si es uno más que el anterior continua y agregalo al arreglo temporal"
            elif(temp_numero_anterior-1 == indice):
                temp_numero_anterior = indice
                Flag_todos_son_consecutivos=True
                contador += 1
            else:
                Flag_todos_son_consecutivos=False
                return Flag_todos_son_consecutivos
        return Flag_todos_son_consecutivos
    


#entrada = input ("Ingrese un arreglo")
entrada =  [8,7,5,4,3,5,4,3]
entrada2 =  [3,2,1]
objeto_recorrido = recorridos()
#bandera = objeto_recorrido.decrece(entrada2)
#if (bandera):
    #print (entrada2)
arreglo_final = objeto_recorrido.obtiene_arreglo(entrada)
print(arreglo_final)
print(len(arreglo_final))


listaplana = []
listaplana = [item for l in arreglo_final for item in l]
print(listaplana)

print(len(listaplana))


#objeto_recorrido.extraer_arreglo_si_decrece(entrada)

#arreglopropuesto = [8,7,5,4,3,5,4,3]
#arreglopropuesto2 = [5,4,3,2,1,0]
#ObjetoArbol = Arbol(arreglopropuesto2)
#ObjetoArbol.recorridoB(arreglopropuesto2)
#ObjetoArbol.inorden()
#primero tengo que hacer el recorrido y partir los datos. esto hasta que ya no haya más






# arpropposed = {1,3,2}
# [8,7,5,4,3,5,4,3]

#objeto = Arbol2(1, Arbol2(2,None, None) , Arbol2(3,None,None))
#arreglopropuesto = [8,7,5,4,3,5,4,3]
#objeto2 = FuncionesT1.Arbol3(arreglopropuesto[0])
#objeto2 = Arbol3(arreglopropuesto[0])
#objeto3 = Arbol3(arreglopropuesto)
#objeto3.inorden()
#arreglopropuesto.pop(0)
#objeto2.carga_arreglo(arreglopropuesto)
#print(objeto2.primarykey.key)
#objeto2.inorden()
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
