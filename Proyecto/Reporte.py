from MatrizBidimensional import MatrizBidimensional
import os


def generarImagen(nombre):

    dotPath = "\"C:\\Graphviz\\bin\\dot.exe\""
    fileInputPath = nombre + ".txt"
    fileOutputPath = nombre + ".png"
    tParam = " -Tpng "
    tOParam = " -o "
    tuple = (dotPath + tParam + fileInputPath + tOParam + fileOutputPath)
    os.system(tuple)
    os.system(fileOutputPath)


def generarTxt(nombre, dot):
    archivo = open(nombre + ".txt", 'w')
    archivo.write(dot)
    archivo.close()
    generarImagen(nombre)


def reporteMatriz(matriz):
    dot = matriz.graficar()
    generarTxt("reporteMatriz", dot)


def reporteArtistas(matriz, anio, genero):
    dot = matriz.getArtistas(anio, genero).getDot()
    generarTxt("reporteArtistas", dot)


def reporteAlbumes(matriz, anio, genero, nombreArtista):
    dot = matriz.getArtistas(anio, genero).busqueda(
        nombreArtista).getAlbumes().graficar()
    generarTxt("reporteAlbumes", dot)


def reporteListaCanciones(matriz, anio, genero, nombreArtista, nombreAlbum):
    dot = matriz.getArtistas(anio, genero).busqueda(
        nombreArtista).getAlbumes().getAlbum(nombreAlbum).getCanciones().graficar()
    generarTxt("reporteCanciones", dot)


def reporteUsuarios(listaUsuarios):
    dot = listaUsuarios.graficar()
    generarTxt("reporteUsuarios", dot)


def reporteCola(listaUsuarios, nombre):
    dot = listaUsuarios.getCola(nombre).graficar()
    generarTxt("reporteCola", dot)
