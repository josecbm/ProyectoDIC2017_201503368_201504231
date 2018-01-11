from NodoUsuario import NodoUsuario
import sys
from graphviz import Digraph
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz/bin'


class ListaUsuarios:

    def __init__(self):
        self.Inicio = None

    def vacia(self):
        return self.Inicio == None

    def InsertarFinal(self, Nombre, Contra):
        nuevo = NodoUsuario(Nombre, Contra)
        if self.vacia():
            self.Inicio = nuevo
        else:
            aux = self.Inicio
            while aux.getSiguiente() != None:
                aux = aux.getSiguiente()
            aux.setSiguiente(nuevo)
            nuevo.setAnterior(aux)

    def recorrer(self):
        aux = self.Inicio
        while aux.getSiguiente() != None:
            aux = aux.getSiguiente()

    def login(self, Nombre, Contra):
        aux = self.Inicio
        while aux != None:
            if aux.getNombreUsuario() == Nombre and aux.getContraUsuario() == Contra:
                return "True"
            aux = aux.getSiguiente()
        return "False"

    def getCola(self, nombre):
        aux = self.Inicio
        while aux != None:
            print aux.getNombreUsuario().lower()+" : " +nombre.lower()
            if aux.getNombreUsuario().lower() == nombre.lower():
                return aux.getColaCanciones()
            aux = aux.getSiguiente()
        return None

    def insertarCola(self, usuario, nombre):
        aux = self.Inicio
        while aux != None:
            if aux.getNombreUsuario().lower() == usuario.lower():
                return aux.insertarCanciones(nombre)
            aux = aux.getSiguiente()
        return None

    def graficar(self):
        dot = Digraph(comment='Lista de Usuarios')
        actual = self.Inicio
        i = 0
        while actual != None:
            dot.node(str(i), actual.getNombreUsuario())
            actual = actual.getSiguiente()
            i += 1
            if actual != None:
                dot.edge(str(i - 1), str(i), constraint='false')
                dot.edge(str(i), str(i - 1), constraint='false')

        return dot.source

    def mostrarUsuario(self):
        if self.vacia():
            sys.stdout.write("<==>NULL")
        else:
            aux = self.Inicio
            sys.stdout.write("INICIO")
            while aux != None:
                sys.stdout.write("<==>" + aux.getNombreUsuario())
                aux = aux.getSiguiente()
            sys.stdout.write("<==>NULL")
