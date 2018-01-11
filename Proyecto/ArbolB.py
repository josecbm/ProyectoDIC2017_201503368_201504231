from Artista import Artista
from Rama import Rama


class ArbolB(object):

    def __init__(self):
        self.raiz = None
        self.nodos = ""

    def estaVacio(self):
        return self.raiz == None

    def insertar(self, nombre):
        nodo = Artista(nombre)
        if self.estaVacio():
            self.raiz = Rama()
            self.raiz.insertar(nodo)
        else:
            obj = self.inserta(nodo, self.raiz)
            if isinstance(obj, Artista):
                self.raiz = Rama()
                self.raiz.insertar(obj)
                self.raiz.setHoja(False)

    def inserta(self, nodo, rama):
        if rama.esHoja():
            rama.insertar(nodo)
            if rama.getCuenta() == 5:
                return self.dividir(rama)
            else:
                return rama
        else:
            temp = rama.getPrimero()
            while True:
                if nodo.getNombre().lower() == temp.getNombre().lower():
                    return rama
                elif nodo.getNombre().lower() < temp.getNombre().lower():
                    obj = self.inserta(nodo, temp.getIzquierda())
                    if isinstance(obj, Artista):
                        rama.insertar(obj)
                        if (rama.getCuenta() == 5):
                            return self.dividir(rama)
                    return rama
                elif temp.getSiguiente() == None:
                    obj = self.inserta(nodo, temp.getDerecha())
                    if isinstance(obj, Artista):
                        rama.insertar(obj)
                        if (rama.getCuenta() == 5):
                            return self.dividir(rama)
                    return rama
                temp = temp.getSiguiente()
                if not(temp != None):
                    break
        return rama

    def dividir(self, rama):
        derecha = Rama()
        izquierda = Rama()
        medio = None
        temp = rama.getPrimero()
        i = 1
        while i < 6:
            nodo = Artista(temp.getNombre())
            nodo.setIzquierda(temp.getIzquierda())
            nodo.setDerecha(temp.getDerecha())
            if (nodo.getDerecha() != None and nodo.getIzquierda() != None):
                izquierda.setHoja(False)
                derecha.setHoja(False)
            if i == 1 or i == 2:
                izquierda.insertar(nodo)
            elif i == 3:
                medio = nodo
            elif i == 4 or i == 5:
                derecha.insertar(nodo)
            temp = temp.getSiguiente()
            i = i + 1
        medio.setIzquierda(izquierda)
        medio.setDerecha(derecha)
        return medio

    def getDot(self):
        aux = "digraph lista{ \nnode [shape = record, style=filled];\n"
        aux += "splines=line; \n"
        self.getGrafNodos(self.raiz)
        aux += self.nodos
        aux += "}"
        return aux

    def getGrafNodos(self, raiz):
        if raiz == None:
            return
        self.nodos += raiz.getGraphNodo()
        aux = raiz.getPrimero()
        while aux != None:
            self.getGrafNodos(aux.getIzquierda())
            aux = aux.getSiguiente()
        aux = raiz.getPrimero()
        while aux.getSiguiente() != None:
            aux = aux.getSiguiente()
        self.getGrafNodos(aux.getDerecha())

    def busqueda(self, nombre):
        if not(self.estaVacio()):
            return self.busca(nombre, self.raiz)
        else:
            print "retorno nulo en busqueda"
            return None

    def busca(self, nombre, rama):
        nodo = rama.getPrimero()
        while nodo != None:
            if nombre.lower() < nodo.getNombre().lower():
                if rama.esHoja():
                    return None
                else:
                    return self.busca(nombre, nodo.getIzquierda())
            elif nombre.lower() == nodo.getNombre().lower():
                return nodo
            elif nodo.getSiguiente() == None:
                if rama.esHoja():
                    return None
                else:
                    return self.busca(nombre, nodo.getDerecha())
            nodo = nodo.getSiguiente()
        return None
