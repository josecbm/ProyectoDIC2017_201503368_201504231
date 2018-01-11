from flask import Flask, session
from flask import request
from flask import make_response


import Reporte

from CargaMasiva import CargaMasiva

app = Flask(__name__)
Carga = None

usuarioLogeado = ""


@app.route('/login', methods=['POST'])
def login():
    usuario = str(request.form['usuario'])
    pas = str(request.form['contra'])
    usuarioLogeado = usuario
    print Carga.getUsuarios().login(usuario, pas)
    return Carga.getUsuarios().login(usuario, pas)


@app.route('/Carga', methods=['POST'])
def Carga():

    path = str(request.form['path'])
    Carga.analizarXML(path)
    return "Si se pudo"

# reporte usuarios


@app.route('/insertarCola', methods=['POST'])
def insertarCola():    
    nombreCancion = str(request.form['cancion'])
    usuario = str(request.form['usuario'])
    print usuario +" : "+ nombreCancion
    Carga.getUsuarios().insertarCola(usuario, nombreCancion)
    return "Si se pudo"

# reporte usuarios


@app.route('/reporteUsuarios', methods=['POST'])
def reporteUsuarios():
    Reporte.reporteUsuarios(Carga.getUsuarios())
    return "Si se pudo"
# reporte matriz


@app.route('/reporteMatriz', methods=['POST'])
def reporteMatriz():
    Reporte.reporteMatriz(Carga.getMatriz())
    return "Si se pudo"

# reporte Cola usuario


@app.route('/reporteColaUsuario', methods=['POST'])
def reporteColaUsuario():
    usuario = str(request.form['usuario'])
    Reporte.reporteCola(Carga.getUsuarios(), usuario)
    return usuario


@app.route('/reporteArtista', methods=['POST'])
def reporteArtista():
    year = str(request.form['anio'])
    gen = str(request.form['genero'])
    Reporte.reporteArtistas(Carga.getMatriz(), year, gen)
    return "Si se pudo"
# reporte abb


@app.route('/reporteAlbumesEspecifico', methods=['POST'])
def reporteAlbumesEspecifico():
    year = str(request.form['anio'])
    genero = str(request.form['genero'])
    artista = str(request.form['artista'])
    Reporte.reporteAlbumes(Carga.getMatriz(), year, genero, artista)
    return "Si se pudo"
# reporte lista


@app.route('/CancionesSistema', methods=['POST'])
def CancionesSistema():
    aux = Carga.listaReporte.obtener()
    titulo = aux.Cancion
    artista = aux.Artistas
    album = aux.Album
    genero = aux.Genero
    Anio = aux.Anio
    path = aux.path

    return str(titulo) + "~" + str(artista) + "~" + str(album) + "~" + str(genero) + "~" + str(Anio) + "~" + str(path)


@app.route('/reporteCanciones', methods=['POST'])
def reporteCanciones():
    anio = str(request.form['anio'])
    genero = str(request.form['genero'])
    nombreArtista = str(request.form['artista'])
    nombreAlbum = str(request.form['album'])
    Reporte.reporteListaCanciones(
        Carga.getMatriz(), anio, genero, nombreArtista, nombreAlbum)
    return "Si se pudo"

'''Modulo de eliminacion'''
@app.route('/eliminarUsr', methods=['POST'])
def eliminarUsr():
    usuario = str(request.form['usuario'])
    
    return usuario

@app.route('/eliminarNodoMatriz', methods=['POST'])
def eliminarNodoMatriz():
    year = str(request.form['anio'])
    gen = str(request.form['genero'])
   
    return "Si se pudo"

@app.route('/eliminarListaDobCancion', methods=['POST'])
def eliminarListaDobCancion():
    anio = str(request.form['anio'])
    genero = str(request.form['genero'])
    nombreArtista = str(request.form['artista'])
    nombreAlbum = str(request.form['album'])
   
    return "Si se pudo"
''' Modulo de Modos de Reproduccion'''

@app.route('/getCancionesArtista', methods=['POST'])
def getCancionesArtista():
    artista = str(request.form['artista'])
    Reporte.reporteAlbumes(Carga.getMatriz(), year, genero, artista)
    return "Si se pudo"


if __name__ == '__main__':
    Carga = CargaMasiva()
    app.run(debug=True)
