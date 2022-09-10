from Arbol3 import Arbol3

sencillo = Arbol3("1",Arbol3("2",None,None,None),Arbol3("3",None,None,None),Arbol3("4",None,None,None))

Roble = Arbol3(
    "1",
    Arbol3("2",None,None,None),
    Arbol3("3",
        Arbol3("5",None,None,None),
        Arbol3("6",
            Arbol3("9",None,None,None),
            Arbol3("10",None,None,None),
            Arbol3("11",None,None,None)),
        Arbol3("7",None,None,None)),
    Arbol3("4",None,None,None)
)


print(sencillo.key)
print(Roble.left.key)
print(Roble.listasinaplanar())
print(Roble.preorder())
print(Roble.inorder())
print(Roble.postorder())
