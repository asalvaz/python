class decremental:
    def __init__(self) -> None:
        pass
    def decremental(self, list, n):
        secuencia = []

        for i in range(len(list)):
            for j in range(len(list)):
                if i != j:
                    if list[i]-1 == list[j]:
                        secuencia.append(list[i])
                        secuencia.append(list[j])
        return secuencia
    def getdays(self, list):
        longitud = len(list)
        return longitud
    def repetidos(self, lista):
        pass

arpropposed = [8,7,5,4,3,5,4,3]
obj = decremental()
long = obj.getdays(arpropposed)
print(str(long))
print(obj.decremental(arpropposed, obj.getdays(arpropposed)))