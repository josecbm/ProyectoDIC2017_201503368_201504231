from ListaMatrizBidimensional import ListaMatrizBidimensional


class MatrizBidimensional:

    def __init__(self, altura, anchura):
        self.ultima = None
        self.altura = altura
        self.anchura = anchura

        if anchura > 0 and altura > 0:
            self.ultima = ListaMatrizBidimensional(anchura)
            for i in xrange(1, altura):
                aux = ListaMatrizBidimensional(anchura)
                recorrerAux = aux.getPrimero()
                recorrerUltima = self.ultima.getPrimero()
                while recorrerAux != None and recorrerUltima != None:
                    recorrerAux.setArriba(recorrerUltima)
                    recorrerUltima.setAbajo(recorrerAux)
                    recorrerUltima = recorrerUltima.getSiguiente()
                    recorrerAux = recorrerAux.getSiguiente()
                self.ultima = aux

    def setDato(self, dato, fila, columna):
        if fila < self.altura and columna < self.anchura:
            cabeza = self.ultima.getPrimero()
            while cabeza.getArriba() != None:
                cabeza = cabeza.getArriba()
            for x in xrange(0, fila):
                cabeza = cabeza.getAbajo()
            for x in xrange(0, columna):
                cabeza = cabeza.getSiguiente()
            cabeza.setDato(dato)

    def getDato(self, fila, columna):
        cabeza = self.ultima.getPrimero()
        while cabeza.getArriba() != None:
            cabeza = cabeza.getArriba()
        for x in xrange(0, fila):
            cabeza = cabeza.getAbajo()
        for x in xrange(0, columna):
            cabeza = cabeza.getSiguiente()
        return cabeza.getDato()

    def getArtistas(self, anio, genero):
        cabeza = self.ultima.getPrimero()
        x=self.getIndexGenero(genero)
        y=self.getIndexAnio(anio)
        while cabeza.getArriba() != None:
            cabeza = cabeza.getArriba()
        for i in xrange(0, y):
            cabeza = cabeza.getAbajo()
        for j in xrange(0, x):
            cabeza = cabeza.getSiguiente()
        cabeza.setDato(anio+"-"+genero)
        return cabeza.getArtistas()

    def insertarArtista(self, anio, genero, nombre):
        cabeza = self.ultima.getPrimero()
        x=self.getIndexGenero(genero)
        y=self.getIndexAnio(anio)
        while cabeza.getArriba() != None:
            cabeza = cabeza.getArriba()
        for i in xrange(0, y):
            cabeza = cabeza.getAbajo()
        for j in xrange(0, x):
            cabeza = cabeza.getSiguiente()
        cabeza.setDato(anio+"-"+genero)
        cabeza.insertarArtista(nombre)

    def getIndexAnio(self, anio):
        for x in xrange(0, self.altura):
            if self.getDato(x, 0) == anio:
                return x
        return -1

    def getIndexGenero(self, genero):
        for x in xrange(0, self.anchura):
            if self.getDato(0, x) == genero:
                return x
        return -1

    def getAltura(self):
        return self.altura

    def getAnchura(self):
        return self.anchura

    def getUltima(self):
        return self.ultima

    def graficar(self):
        dot = "digraph lista{ \n"
        dot += "rankdir = TB; \n"
        dot += "node [shape = record];\n"
        dot += "Matriz[shape = record,label=\"{"
        for i in xrange(0, self.altura - 1):
            dot += "{"
            for j in xrange(0, self.anchura - 1):
                dot += "{" + str(self.getDato(i, j)) + "}|"
            dot += "{" + str(self.getDato(i, self.anchura - 1)) + "}"
            dot += "}|"
        dot += "{"
        for j in xrange(0, self.anchura - 1):
            dot += "{" + str(self.getDato(self.altura - 1, j)) + "}|"
        dot += "{" + str(self.getDato(self.altura - 1, self.anchura - 1)) + "}"
        dot += "}"
        dot += "}\"]; \n"
        dot += "}"
        return dot
