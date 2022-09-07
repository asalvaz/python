class FuncionesT1:
    def __init__(self) -> None:
        pass
    
    def getdays(self, list):
        longitud = len(list)
        return longitud

    def repetidos_tardados(self, lista):
        secuencia = []

        for i in range(len(lista)):
            for j in range(len(lista)):
                if i != j:
                    if lista[i] == lista[j] and lista[i] not in secuencia:
                        secuencia.append(lista[i])
        return secuencia

    def repetidos_rapida(self, lista):
        secuencia = []
        archivo = []

        for n in lista:
            if n not in archivo:
                archivo.append(n)
            else:
                secuencia.append(n)
        return secuencia

    def intentodecremental(self, list, n):
        secuencia = []

        for i in range(len(list)):
            for j in range(len(list)):
                if i != j:
                    if list[i]-1 == list[j]:
                        secuencia.append(list[i])
                        secuencia.append(list[j])
        return secuencia
    
    def bidecremental(self, lista):
        secuencia = []
        archivo = []
        bypass = 0
        thefirstone = False
        for n in lista:
            if thefirstone != False:
                if bypass  == n:
                    archivo.append(n+1)
                    archivo.append(n)
                    if len(secuencia) == 0:
                        secuencia = [archivo]
                    else:
                        secuencia.append(archivo)
                    archivo = []
                    bypass = n-1
                else:
                    bypass = n-1
            else:
                thefirstone = True
                bypass = n-1
        return secuencia

    def decremental(self, lista):
        secuencia = []
        archivo = []
        bypass = 0
        numintegrales = 1
        thefirstone = False
        for j in range(len(lista)):
            if thefirstone != False:
                if bypass  == lista[j]:
                    bypass = lista[j]-1
                    if numintegrales==1:
                        archivo.append(lista[j-1])
                    numintegrales += 1
                    archivo.append(lista[j])
                    print(lista.index)
                    print(lista[j])
                    #En el caso de que termine siendo igual no se esta considerando el realizar la suma del arreglo [5 4 3 fin]
                else:
                    #for i in range(numintegrales):
                    
                    if len(secuencia) == 0:
                        secuencia.append(archivo)
                        numintegrales=1
                    else:
                        secuencia.append(archivo)
                        numintegrales=1
                    archivo = []
                    bypass = lista[j]-1
            else:
                thefirstone = True
                bypass = lista[j]-1
        if numintegrales > 0:
            if len(secuencia) == 0:
                secuencia.append(archivo)
            else:
                secuencia.append(archivo)
        return secuencia

    def couldbedecremental(self, lista):
        secuencia = []
        archivo = []
        bypass = 0
        numintegrales = 1
        thefirstone = False
        for j in range(len(lista)):
            if thefirstone != False:
                if bypass  == lista[j]:
                    bypass = lista[j]-1
                    if numintegrales==1:
                        archivo.append(lista[j-1])
                    numintegrales += 1
                    archivo.append(lista[j])
                    #En el caso de que termine siendo igual no se esta considerando el realizar la suma del arreglo [5 4 3 fin]
                else:
                    secuencia.append(archivo)
                    if numintegrales>2:
                        secuencia.append(decremental().couldbedecremental(archivo))
                    numintegrales=1
                    archivo = []
                    bypass = lista[j]-1
            else:
                thefirstone = True
                bypass = lista[j]-1
        if numintegrales > 0:
                secuencia.append(archivo)
        return secuencia   