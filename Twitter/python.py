import textwrap

def wrap(string, max_width):
    cont = 0
    impresion = ""
    for x in string:
        cont += 1
        if (cont == max_width):
            impresion = impresion + x
            impresion = impresion + "\n"
            cont = 0
        else:
            impresion = impresion + x
            
#    if (impresion != ""):
#        print(impresion)
    return impresion

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)