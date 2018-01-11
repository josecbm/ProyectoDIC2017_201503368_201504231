import os
import codecs
from xml.etree import ElementTree

from ListaUsuarios import ListaUsuarios
from ListaCanciones import ListaCanciones
from ListaReporte import ListaReporte
from MatrizBidimensional import MatrizBidimensional
from ABB import ABB
import Reporte
from ArbolB import ArbolB


class CargaMasiva:
    """docstring for CargaMasiva"""

    def __init__(self,):
        self.usuarios = ListaUsuarios()
        self.matriz = None
        self.listaReporte = ListaReporte()

    def getUsuarios(self):
        return self.usuarios

    def getMatriz(self):
        return self.matriz

    def getListaReporte(self):
        return self.listaReporte

    def cargarUsuarios(self, root):
        coleccionUsuarios = root.findall('usuarios')
        for usuarios in coleccionUsuarios:
            coleccionUsuario = usuarios.findall('usuario')
            for usuario in coleccionUsuario:
                self.usuarios.InsertarFinal(usuario.find(
                    'nombre').text.lower(), usuario.find('pass').text.lower())

    def crearMatriz(self, root):
        generos = ["--- Matriz ---"]
        anios = ["--- Matriz ---"]
        coleccionArtistas = root.findall('artistas')
        for artistas in coleccionArtistas:
            coleccionArtista = artistas.findall('artista')
            for artista in coleccionArtista:
                coleccionAlbumes = artista.findall('albumes')
                for albumes in coleccionAlbumes:
                    coleccionAlbum = albumes.findall('album')
                    for album in coleccionAlbum:
                        gen = album.find('genero').text
                        anio = album.find('anio').text
                        if not(gen in generos):
                            generos.append(gen)
                        if not(anio in anios):
                            anios.append(anio)
        altura = len(anios)
        anchura = len(generos)
        anios.sort()
        self.matriz = MatrizBidimensional(altura, anchura)
        for x in xrange(0, altura):
            self.matriz.setDato(anios[x], x, 0)
        for y in xrange(0, anchura):
            self.matriz.setDato(generos[y], 0, y)

    def llenarMatriz(self, root):
        coleccionArtistas = root.findall('artistas')
        for artistas in coleccionArtistas:
            coleccionArtista = artistas.findall('artista')
            for artista in coleccionArtista:
                nombreArtista = artista.find('nombre').text
                abbAlbumes = ABB()
                coleccionAlbumes = artista.findall('albumes')
                for albumes in coleccionAlbumes:
                    coleccionAlbum = albumes.findall('album')
                    for album in coleccionAlbum:
                        nombreAlbum = album.find('nombre').text
                        gen = album.find('genero').text
                        anio = album.find('anio').text
                        self.matriz.getArtistas(
                            anio, gen).insertar(nombreArtista)
                        if nombreAlbum != None:
                            self.matriz.getArtistas(anio, gen).busqueda(
                                nombreArtista).insertarAlbum(nombreAlbum)
                            listaCanciones = ListaCanciones()
                            coleccionCanciones = album.findall('canciones')
                            for canciones in coleccionCanciones:
                                coleccionCancion = canciones.findall(
                                    'cancion')
                                for cancion in coleccionCancion:
                                    can = cancion.find('nombre').text
                                    path = cancion.find('path').text
                                    listaCanciones.InsertarFinal(can, path)
                                    self.matriz.getArtistas(anio, gen).busqueda(
                                        nombreArtista).getAlbum(nombreAlbum).insertarCancion(can, path)
                                    self.listaReporte.insertar(
                                        can, nombreArtista, nombreAlbum, gen, anio, path)
        self.listaReporte.insertar(
            "None", "None", "None", "None", "None", "None")

    def analizarXML(self, cadena):
        full_file = os.path.abspath(cadena)
        with codecs.open(full_file, "r",  errors='ignore') as fdata:
            contenido = fdata.read().replace('\n', '')
        root = ElementTree.fromstring(contenido)
        self.cargarUsuarios(root)
        self.crearMatriz(root)
        self.llenarMatriz(root)
        print "Exito!"
#arch = CargaMasiva()
#arch.analizarXML("entradaEDD2.xml")
#matriz = arch.getMatriz()
#listaUsuarios=arch.getUsuarios()
#listaUsuarios.insertarCola("marco", "gema")
#listaUsuarios.insertarCola("marco", "despues de ti, quien")
#Reporte.reporteCola(listaUsuarios, "marco")