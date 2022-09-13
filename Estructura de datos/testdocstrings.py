from msilib.schema import CustomAction


def custom_max(n1: int, n2: int):
    """#Obtiene número máximo de dos enteros

    Args:
        n1 (int): Parametro 1, Valor numerico
        n2 (int): Parametro 2, valor numerico

    Raises:
        Exception: Excepción si dos valores son iguales
        Exception: Excepción adicional

    Returns:
        _type_: Regresa el Número mayor MAX()
    """
    if n2>n1:
        return n2
    elif n1>n2:
        return n1
    elif n1==n2:
        raise Exception("Los valores no pueden ser iguales")
    else:
        raise Exception("Algo salió mal")


#print(custom_max(1,2,3))
print(custom_max(1,2))
#print(custom_max(a,b))
print(custom_max(2,1))
print(custom_max(2,2))


def max_de_3 (n1: int, n2: int, n3:int):
    pre_mayor = 0
    mayor = 0
    pre_mayor = (custom_max(n1,n2))
    mayor = (custom_max(n1, n3))

<<<<<<< HEAD
    return n1
        

=======
        return n1
        
>>>>>>> f970fdc727fff5a8c6bebab31b598c7f42862441
