from NodoMatriz import NodoMatriz


class ListaMatrizBidimensional:

    def __init__(self, anchura):
        self.primero = None
        for i in xrange(0, anchura):
            self.push()

    def getPrimero(self):
        return self.primero

    def vacia(self):
        return self.primero == None

    def push(self):
        if self.vacia():
            self.primero = NodoMatriz(0)
        else:
            nuevo = NodoMatriz(0)
            nuevo.setSiguiente(self.primero)
            self.primero = nuevo
