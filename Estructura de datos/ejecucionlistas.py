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
        eval(comando)

    print(lista)
    
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
    
"""
    -------------

if __name__ == '__main__':
    n = int(input())
    lista=[]
    
    
    total_comandos = [input().split() for comandos_a_separar in range(n)]
    
    def ejecutar(lista_comandosxlinea):
        if lista_comandosxlinea[0] == "print":
            print(lista)
        else:
            if len(lista_comandosxlinea) == 3:
                comando = "lista." + lista_comandosxlinea[0] + "(" + lista_comandosxlinea[1] + "," + lista_comandosxlinea[2] +")"
            elif len(lista_comandosxlinea) == 2:
                comando = "lista." + lista_comandosxlinea[0] + "(" + lista_comandosxlinea[1] + ")"
            else: 
                comando = "lista." + lista_comandosxlinea[0] + "()"
            eval(comando)
            
    [ejecutar(lista_comandosxlinea) for lista_comandosxlinea in total_comandos]
"""
""" Imprime listado de segundos lugares de un listado de estudiantes segunda alternativa
if __name__ == '__main__':
    names = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names.append(name)
        scores.append(score)
    
    second_lowest = sorted(set(scores))[1]

    for i in sorted(zip(names, scores)):
        [name, score] = i
        if score == second_lowest:
            print(name)
"""


""" Imprime listado de segundos lugares de un listado de estudiantes mejor respuesta
if __name__ == '__main__':
    estudiantes = []
    calificacion = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        estudiantes.append({'nombre':name,'calificacion':score})
        calificacion.append(score)
    segundo_lugar = sorted(set(calificacion))[1]
    nombres_segundos = [alumno['nombre'] for alumno in estudiantes if alumno['calificacion'] == segundo_lugar]
    nombres_segundos.sort()
    for nombre in nombres_segundos:
        print(nombre)
"""