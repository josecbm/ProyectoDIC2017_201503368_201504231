class Nodo_Cola:

    def __init__(self,Nombre):
        self.Nombre = Nombre
        self.Siguiente = None
        self.Anterior = None

    def getNombreCola(self):
        return self.Nombre

    def getSiguiente(self):
        return self.Siguiente

    def getAnterior(self):
        return self.Anterior

    def setAnterior(self,Anterior):
        self.Anterior = Anterior

    def setSiguiente(self,Siguiente):
        self.Siguiente = Siguiente

