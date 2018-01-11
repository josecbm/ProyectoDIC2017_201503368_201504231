from ColaCanciones import ColaCanciones

class NodoUsuario:

    def __init__(self,Nombre,Contra):
        self.Nombre = Nombre
        self.Contra = Contra
        self.Siguiente = None
        self.Anterior = None
        self.Canciones = ColaCanciones()

    def getColaCanciones(self):
        return self.Canciones

    def insertarCanciones(self,nombre):
        self.Canciones.encolar(nombre)
        
    def getNombreUsuario(self):
        return  self.Nombre

    def getContraUsuario(self):
        return self.Contra

    def getSiguiente(self):
        return self.Siguiente

    def getAnterior(self):
        return self.Anterior

    def setSiguiente(self,Siguiente):
        self.Siguiente = Siguiente

    def setAnterior(self,Anterior):
        self.Anterior = Anterior
