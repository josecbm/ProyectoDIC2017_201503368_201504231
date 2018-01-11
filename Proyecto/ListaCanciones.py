from Cancion import Cancion

import sys
from graphviz import Digraph
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz/bin'

class ListaCanciones:

    def __init__(self):
        self.Inicio = None

    def vacia(self):
        return self.Inicio == None

    def InsertarFinal(self, Nombre, Path):
        nuevo = Cancion(Nombre, Path)
        if self.vacia():
            self.Inicio = nuevo
            self.Inicio.Siguiente = self.Inicio
            self.Inicio.Anterior = self.Inicio
        else:
            aux = self.Inicio
            while aux.Siguiente != self.Inicio:
                aux = aux.Siguiente
            aux.Siguiente = nuevo
            nuevo.Anterior = aux
            nuevo.Siguiente = self.Inicio
            self.Inicio.Anterior = nuevo

    def graficar(self):
        dot = Digraph(comment='Lista Canciones')
        actual = self.Inicio
        i = 0
        while actual:
            dot.node(str(i), actual.getNombre())
            actual = actual.getSiguiente()
            i += 1
            if actual == self.Inicio:
                break
            dot.edge(str(i - 1), str(i), constraint='false')
            dot.edge(str(i), str(i - 1), constraint='false')
        dot.edge(str(i - 1), str(0), constraint='false')
        dot.edge(str(0), str(i - 1), constraint='false')
        return dot.source


    # aqui deberia de ir el metodo mostrar pero no estoy seguro si agregarlo
    # posiblemente lo agregie mas tarde





