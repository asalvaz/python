import FuncionesT1
class decremental:
    def __init__(self) -> None:
        pass

#Alternativa (Tomar una copia de arreglo y Sumar al arreglo un campo para mover a la derecha y comparar ambos casos a la vez.)

arpropposed = [8,7,5,4,3,5,4,3]
obj = decremental()
long = obj.getdays(arpropposed) 
#print(str(long))
#print("intento decremental" + str(obj.intentodecremental(arpropposed, obj.getdays(arpropposed))))
#print("Repetidos" + str(obj.repetidos_tardados(arpropposed)))
#print("Repetidos rapido" + str(obj.repetidos_rapida(arpropposed)))
#print("decremental" + str(obj.bidecremental(arpropposed)))
#print("decremental" + str(obj.decremental(arpropposed)))
print("decremental" + str(obj.couldbedecremental(arpropposed)))
