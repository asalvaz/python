class Arbol3:
    def __init__(self, key, left, right1, right2):
        self.key = key
        self.left = left
        self.right1 = right1
        self.right2 = right2

#Lista Bruta
    def listasinaplanar(self):
        salida = []
        salida.append(self.key)

        if self.left != None:
            salida.append(self.left.listasinaplanar())
        if self.right1 != None:
            salida.append(self.right1.listasinaplanar())
        if self.right2 != None:
            salida.append(self.right2.listasinaplanar())
        
        return salida

#Lista aplanada
    def preorder(self):
        salida = []
        salida.append(self.key)

        if self.left != None:
            salidaL = self.left.preorder()
            for e in salidaL:
                salida.append(e)
        if self.right1 != None:
            salidaR = self.right1.preorder()
            for e in salidaR:
                salida.append(e)
        if self.right2 != None:
            salidaR = self.right2.preorder()
            for e in salidaR:
                salida.append(e)
        return salida

    def inorder(self):
        salida = []
        
        if self.left != None:
            salidaL = self.left.inorder()
            for e in salidaL:
                salida.append(e)

        salida.append(self.key)

        if self.right1 != None:
            salidaR = self.right1.inorder()
            for e in salidaR:
                salida.append(e)
        if self.right2 != None:
            salidaR = self.right2.inorder()
            for e in salidaR:
                salida.append(e)
        return salida


    def postorder(self):
            salida = []
            
            if self.left != None:
                salidaL = self.left.postorder()
                for e in salidaL:
                    salida.append(e)
            if self.right1 != None:
                salidaR = self.right1.postorder()
                for e in salidaR:
                    salida.append(e)
            if self.right2 != None:
                salidaR = self.right2.postorder()
                for e in salidaR:
                    salida.append(e)

            salida.append(self.key)
            return salida
