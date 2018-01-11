from Artista import Artista


class Rama:

    def __init__(self):
        self.cuenta = 0
        self.hoja = True
        self.primero = None
        self.tempFlechas = ""

    def insertar(self, nuevo):
        if self.estaEnBlanco():
            self.primero = nuevo
            self.primero.setAnterior(None)
            self.primero.setSiguiente(None)
            self.cuenta = self.cuenta + 1
        else:
            temp = self.primero
            while True:
                if nuevo.getNombre().lower() == temp.getNombre().lower():
                    break
                elif nuevo.getNombre().lower() < temp.getNombre().lower():
                    self.cuenta = self.cuenta + 1
                    if (temp == self.primero):
                        self.primero.setAnterior(nuevo)
                        self.primero.setIzquierda(nuevo.getDerecha())
                        nuevo.setSiguiente(self.primero)
                        self.primero = nuevo
                        break
                    else:
                        nuevo.setAnterior(temp.getAnterior())
                        nuevo.setSiguiente(temp)
                        temp.getAnterior().setSiguiente(nuevo)
                        temp.getAnterior().setDerecha(nuevo.getIzquierda())
                        temp.setAnterior(nuevo)
                        temp.setIzquierda(nuevo.getDerecha())
                        break
                elif (temp.getSiguiente() == None):
                    self.cuenta = self.cuenta + 1
                    temp.setSiguiente(nuevo)
                    temp.setDerecha(nuevo.getIzquierda())
                    nuevo.setAnterior(temp)
                    nuevo.setSiguiente(None)
                    break
                temp = temp.getSiguiente()
                if not (temp != None):
                    break

    def estaEnBlanco(self):
        return self.primero == None

    def getGraphNodo(self):
        self.tempFlechas = ""
        temp = "nodo" + self.primero.getNombre() + " [ label =\""
        tempRecorre = self.primero
        detalles = ""
        i = 0
        while i < self.cuenta:
            temp += "<C" + str(i) + ">|<D" + str(i) + \
                ">Nombre Artista: " + tempRecorre.getNombre() + "|"
            if tempRecorre.getIzquierda() != None:
                self.tempFlechas += "nodo" + self.primero.getNombre() + ":C" + str(i) + "->nodo" + \
                    tempRecorre.getIzquierda().primero.getNombre() + "\n"
            tempRecorre = tempRecorre.getSiguiente()
            i = i + 1
        temp += "<C" + str(i) + ">\" fillcolor=\"#CCCCCC\"]\n"
        tempRecorre = self.primero
        while tempRecorre.getSiguiente() != None:
            tempRecorre = tempRecorre.getSiguiente()
        if tempRecorre.getDerecha() != None:
            self.tempFlechas += "nodo" + self.primero.getNombre() + ":C" + str(i) + "->nodo" + \
                tempRecorre.getDerecha().primero.getNombre() + "\n"
        temp += self.tempFlechas
        temp += detalles
        return temp

    def esHoja(self):
        return self.hoja

    def setHoja(self, hoja):
        self.hoja = hoja

    def getCuenta(self):
        return self.cuenta

    def getPrimero(self):
        return self.primero
