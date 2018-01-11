class Cancion:

    def __init__(self, Nombre, Path):
        self.Nombre = Nombre
        self.Path = Path
        self.Siguiente = None
        self.Anterior = None

    def getNombre(self):
        return self.Nombre

    def getPath(self):
        return self.Path

    def getSiguiente(self):
        return self.Siguiente

    def getAnterior(self):
        return self.Anterior

    def setSiguiente(self, Siguiente):
        self.Siguiente = Siguiente

    def setAnterior(self, Anterior):
        self.Anterior = Anterior
