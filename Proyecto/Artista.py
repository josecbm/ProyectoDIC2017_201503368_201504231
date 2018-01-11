from ABB import ABB


class Artista:

    def __init__(self, nombre):
        self.nombre = nombre
        self.albumes = ABB()
        self.anterior = None
        self.siguiente = None
        self.derecha = None
        self.izquierda = None

    def insertarAlbum(self, nombre):
        self.albumes.insertar(nombre)

    def getAlbum(self, nombre):
        return self.albumes.getAlbum(nombre)

    def getAlbumes(self):
        return self.albumes

    def getNombre(self):
        return self.nombre

    def getSiguiente(self):
        return self.siguiente

    def setSiguiente(self, siguiente):
        self.siguiente = siguiente

    def getAnterior(self):
        return self.anterior

    def setAnterior(self, anterior):
        self.anterior = anterior

    def getDerecha(self):
        return self.derecha

    def setDerecha(self, derecha):
        self.derecha = derecha

    def getIzquierda(self):
        return self.izquierda

    def setIzquierda(self, izquierda):
        self.izquierda = izquierda
