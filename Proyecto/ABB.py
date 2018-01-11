from Album import Album


class ABB:
    """docstring for ABB"""

    def __init__(self):
        self.raiz = None

    def insertar(self, nombre):
        if self.raiz == None:
            self.raiz = Album(nombre)
        else:
            self.raiz.insertar(nombre)

    def graficar(self):
        return self.raiz.getCodigoGraphviz()

    def inorden(self):
        print u"Recorrido inorden del arbol binario de busqueda"
        self.inordenAux(self.raiz)
        print "\n"

    def getAlbum(self, nombre):
        return self.getAlbumAux(self.raiz, nombre)

    def getAlbumAux(self, actual, nombre):
        if actual == None:
            return nombre
        elif nombre.lower() == actual.getNombre().lower():
            return actual
        elif nombre.lower() < actual.getNombre().lower():
            return self.getAlbumAux(nombre, actual.getIzquierdo())
        else:
            return self.getAlbumAux(nombre, actual.getDerecho())
        return None

    def inordenAux(self, a):
        if a == None:
            return
        self.inordenAux(a.izquierdo)
        print a.nombre + ","
        self.inordenAux(a.derecho)
