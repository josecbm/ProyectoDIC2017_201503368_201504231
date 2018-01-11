from ArbolB import ArbolB


class NodoMatriz:

    def __init__(self, dato):
        self.dato = dato
        self.Artistas = ArbolB()
        self.Siguiente = None
        self.Anterior = None
        self.Abajo = None
        self.Arriba = None

    def getArtistas(self):
        return self.Artistas

    def insertarArtista(self, nombre, albumes):
        self.Artistas.insertar(nombre, albumes)

    def getDato(self):
        return self.dato

    def getSiguiente(self):
        return self.Siguiente

    def getAnterior(self):
        return self.Anterior

    def getArriba(self):
        return self.Arriba

    def getAbajo(self):
        return self.Abajo

    def setDato(self, dato):
        self.dato = dato

    def setSiguiente(self, Siguiente):
        self.Siguiente = Siguiente

    def setAnterior(self, Anterior):
        self.Anterior = Anterior

    def setArriba(self, Arriba):
        self.Arriba = Arriba

    def setAbajo(self, Abajo):
        self.Abajo = Abajo
