from NodoReporte import NodoReporte


class ListaReporte:
    """docstring for ListaReporte"""
    correlativo = 1

    def __init__(self):
        self.primero = None
        self.size = 0

    def vacia(self):
        return self.size == 0

    def insertar(self, Cancion, Artistas, Album, Genero, Anio,path):
        nuevo = NodoReporte(Cancion, Artistas, Album, Genero, Anio,path)
        nuevo.setSiguiente(self.primero)
        self.primero = nuevo
        self.size += 1

    def obtener(self):
        aux = self.primero
        if ListaReporte.correlativo < self.size:
            conteo = 0
            while conteo < ListaReporte.correlativo:
                aux = aux.getSiguiente()
                conteo += 1
            ListaReporte.correlativo += 1
            return aux
        return NodoReporte("None", "None", "None", "None", "None","None")
