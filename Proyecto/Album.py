from ListaCanciones import ListaCanciones


class Album:
    """docstring for Album"""
    correlativo = 1

    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = ListaCanciones()
        self.izquierdo = None
        self.derecho = None
        Album.correlativo = Album.correlativo + 1
        self.id = Album.correlativo

    def insertarCancion(self,Nombre, Path):
        self.canciones.InsertarFinal(Nombre, Path)

    def getCanciones(self):
        return self.canciones

    def getNombre(self):
        return self.nombre

    def getIzquierdo(self):
        return self.izquierdo

    def getDerecho(self):
        return self.derecho

    def getId(self):
        return self.id

    def setNombre(self, nombre):
        self.nombre = nombre

    def setIzquiero(self, izquierdo):
        self.izquierdo = izquierdo

    def setDerecho(self, derecho):
        self.derecho = derecho

    def setId(self, idd):
        self.id = idd

    def insertar(self, nombre, canciones):
        if nombre < self.nombre:
            if self.izquierdo == None:
                self.izquierdo = Album(nombre, canciones)
            else:
                self.izquierdo.insertar(nombre, canciones)
        elif nombre > self.nombre:
            if self.derecho == None:
                self.derecho = Album(nombre, canciones)
            else:
                self.derecho.insertar(nombre, canciones)
        else:
            print "No se permiten los valores duplicados"

    def getCodigoGraphviz(self):
        return "digraph grafica{\nrankdir=TB;\nnode [shape = record, style=filled, fillcolor=seashell2];\n" + self.getCodigoInterno() + "}\n"

    def getCodigoInterno(self):
        etiqueta = ""
        if self.izquierdo == None and self.derecho == None:
            etiqueta = "Album" + str(self.id) + \
                " [ label =\"" + self.nombre + "\"];\n"
        else:
            etiqueta = "Album" + str(self.id) + \
                " [ label =\"<C0>|" + self.nombre + "|<C1>\"];\n"
        if self.izquierdo != None:
            etiqueta = etiqueta + self.izquierdo.getCodigoInterno() + "Album" + str(self.id) + \
                ":C0->Album" + str(self.izquierdo.id) + "\n"
        if self.derecho != None:
            etiqueta = etiqueta + self.derecho.getCodigoInterno() + "Album" + str(self.id) + \
                ":C1->Album" + str(self.derecho.id) + "\n"
        return etiqueta
