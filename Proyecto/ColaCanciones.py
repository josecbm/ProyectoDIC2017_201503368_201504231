import sys
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz/bin'

from graphviz import Digraph


from NodoCola import Nodo_Cola


class ColaCanciones:

    def __init__(self):
        self.Primero = None
        self.Ultimo = None

    def vacia(self):
        return self.Primero == None

    def encolar(self, Nombre):
        nuevo = Nodo_Cola(Nombre)
        if self.vacia():
            self.Primero = nuevo
            self.Ultimo = nuevo
        else:
            self.Ultimo.setSiguiente(nuevo)
            self.Ultimo = self.Ultimo.getSiguiente()
            self.Ultimo.setSiguiente(self.Primero)

    def desencolar(self):
        if self.vacia():
            return None
        elif self.Primero == self.Ultimo:
            self.Primero = None
            self.Ultimo = None
            sys.stdout.write("la cola esta vacia")

        else:
            self.Primero = self.Primero.getSiguiente()
            self.Ultimo.setSiguiente(self.Primero)

    def graficar(self):
        dot = Digraph(comment='Lista Circular de Canciones')
        actual = self.Primero
        i = 0
        while actual:
            dot.node(str(i), actual.getNombreCola())
            actual = actual.getSiguiente()
            i += 1
            if actual == self.Primero:
                break
            dot.edge(str(i - 1), str(i), constraint='false')
        dot.edge(str(i - 1), str(0), constraint='false')
        return dot.source

    def mostrarCola(self):
        if self.vacia():
            return None
        else:
            aux = self.Primero
            sys.stdout.write("INICIO")
            while aux:
                sys.stdout.write("<==>" + aux.getNombreCola())
                aux = aux.getSiguiente()
                if aux == self.Primero:
                    break
            sys.stdout.write("<==>NULL")
