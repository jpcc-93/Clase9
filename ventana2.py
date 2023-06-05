import math
import sys

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QVBoxLayout, QLabel, QApplication, QScrollArea, QWidget, \
    QGridLayout, QButtonGroup, QPushButton
from PyQt5 import QtGui

from cliente import Cliente
from ventana3 import Ventana3
from ventana4 import Ventana4


class Ventana2(QMainWindow):

    #metodo constructor
    def __init__(self, anterior):
        super(Ventana2, self).__init__(anterior)


        #guardamos la ventana naterior
        self.ventanaAnterior = anterior


        #titulo
        self.setWindowTitle("Usuarios Registrados")


        #iconos
        self.setWindowIcon(QtGui.QIcon("imagenes/iconop.png"))

        #alto ancho
        self.ancho = 900
        self.alto = 600

        self.resize(self.ancho, self.alto)

        #centrar
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        #para que no se cambie
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)


        #establecemos el fondo principal
        self.fondo = QLabel(self)
        #malo aproposito
        self.imagenFondo = QPixmap("imagenes/homer2..jpg")

        #definimos imagen de fondo
        self.fondo.setPixmap(self.imagenFondo)

        #establecemos modo para escalar la imagen
        self.fondo.setScaledContents(True)

        #hacemos que se adapte al tamaño de la imagen
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        #establecemos la ventana de fondo como fondo central
        self.setCentralWidget(self.fondo)

        #establecemos la distribucion como vertical
        self.vertical = QVBoxLayout()

        #hacemos el letrero
        self.letrero1 = QLabel()

        #le escribimos el texto
        self.letrero1.setText("Usuarios Registrados")

        #le asignamos el tipo de letra
        self.letrero1.setFont(QFont("Arial", 20))

        # Color de texto
        self.letrero1.setStyleSheet(" color: #black;")

        #agregamos el eltrero a la primera linea
        self.vertical.addWidget(self.letrero1)

        #agregamos espacio
        self.vertical.addStretch()

        #creamos un scroll
        self.scrollArea = QScrollArea()

        #le ponemos transparente el fondo del scroll:
        self.scrollArea.setStyleSheet("background-color : transparent;")

        #hacemos que le scroll se adpte a diferentes tamaños
        self.scrollArea.setWidgetResizable(True)

        #creamos una ventana contenedora para cada celda
        self.contenedora = QWidget()

        #creamos un layout de grid para poner una cuadricula de elmentos:
        self.cuadricula = QGridLayout(self.contenedora)

        #metemos la ventana contenedora en el scroll
        self.scrollArea.setWidget(self.contenedora)

        #metemos en el layout vertical el scroll
        self.vertical.addWidget(self.scrollArea)

        # Abrimos el archivo en modo lectura:
        self.file = open('datos/clientes.txt', 'rb')

        # Lista vacía para agregar todos los usuarios:
        self.usuarios = []

        #recorremos el archivo linea por linea
        while self.file:
            linea = self.file.readline().decode('UTF-8')

            # Obtenemos del string una lista con 11 datos separados por;
            lista = linea.split(";")
            # Se para si ya no hay más registros en el archivo
            if linea == '':
                break
            # Creamos un objeto de tipo cliente llamado u:
            print(linea)
            u = Cliente(
                lista[0],
                lista[1],
                lista[2],
                lista[3],
                lista[4],
                lista[5],
                lista[6],
                lista[7],
                lista[8],
                lista[9],
                lista[10]
            )

            # Metemos el objeto en la lista de usuarios:
            self.usuarios.append(u)

        # Cerramos el archivo:
        self.file.close()

        # En este punto tenemos la lista usuario con todos los usuarios:

        #obtenemos el numero de usuarios registrados
        #consultamos el tamaño de la lista usuarios
        self.numeroUsuarios = len(self.usuarios)

        #contador de elementos para controlar a los usuarios en la lista usuarios:
        self.contador = 0

        #Definimos la cantidad de elementos a mostrar
        self.elementosPorColumna = 3

        #Calculamos el numero de filas:
        #Redondeamos el entero superior + 1, dividimos por elementosporcolumna:
        self.numeroFilas = math.ceil(self.numeroUsuarios / self.elementosPorColumna) + 1

        #controlamos todos los botones por una variable
        self.botones = QButtonGroup()

        #Definimos que el controlador de los botones
        #debe agrupar a todos los botones internos:
        self.botones.setExclusive(False)

        for fila in range(1, self.numeroFilas):
            for columna in range(1, self.elementosPorColumna + 1):

                #validamos que se estan ingresando la cantidad de usuarios correcta:
                if self.contador < self.numeroUsuarios:
                    #en cada celda de la cuadricula va una ventana:
                    self.ventanaAuxiliar = QWidget()

                    #se determina su alto y su ancho
                    self.ventanaAuxiliar.setFixedWidth(200)
                    self.ventanaAuxiliar.setFixedHeight(100)

                    #creamos un layout vertical para cada elemento de la cuadricula
                    self.verticalCuadricula = QVBoxLayout()

                    #creamos un boton por cada usuario mostrando su cedula:
                    self.botonAccion = QPushButton(self.usuarios[self.contador].documento)

                    #establecemos el ancho del boton
                    self.botonAccion.setFixedWidth(150)
                    #estilo de los botones
                    self.botonAccion.setStyleSheet("background-color : #000000;"
                                                   "color : #FFFFFF;"
                                                   "padding: 10 px;"
                                                   )
                    #agregamos los botones a la cuadricula
                    self.verticalCuadricula.addWidget(self.botonAccion)
                    #agregamos el boton al grupo, con su cedula como id
                    self.botones.addButton(self.botonAccion, int(self.usuarios[self.contador].documento))
                    #agregamos espacio
                    self.verticalCuadricula.addStretch()
                    #A la ventana le asignamos el layout vertical:
                    self.ventanaAuxiliar.setLayout(self.verticalCuadricula)
                    # A la cuadricula le agregamos la ventana en la fila y columna actual
                    self.cuadricula.addWidget(self.ventanaAuxiliar, fila, columna)
                    #aumentamos el contador:
                    self.contador += 1

        #Establecemos el metodo para que funcionen los botones:
        self.botones.idClicked.connect(self.metodo_accionBotones)
        #------ BOTON FORMA TABULAR------

        #nombre
        self.botonFormaTabular = QPushButton("Forma Tabular")
        #tamaño
        self.botonFormaTabular.setFixedWidth(125)
        #estilo
        self.botonFormaTabular.setStyleSheet("background-color : #000000;"
                                             "color : #FFFFFF;"
                                             "padding: 10 px;"
                                             )
        #metodo
        self.botonFormaTabular.clicked.connect(self.metodo_botonFormaTabular)
        #lo agregamos
        self.vertical.addWidget(self.botonFormaTabular)

        #------- BOTON VOLVER ------
        #creamos
        self.botonVolver = QPushButton("Volver")
        #tamaño del boton
        self.botonVolver.setFixedWidth(90)
        #estilo del boton
        self.botonVolver.setStyleSheet("background-color : #000000;"
                                        "color : #FFFFFF;"
                                        "padding: 10 px;"
                                        )
        #METODO
        self.botonVolver.clicked.connect(self.metodo_botonVolver)
        # LO AGREGAMOS A VERTICAL
        self.vertical.addWidget(self.botonVolver)




        #--poner al final siempre  -----------

        # Indicamos que el layout principal del fondo es horizontal
        self.fondo.setLayout(self.vertical)


    #para controlar las acciones de los botones
    def metodo_accionBotones(self, cedulaUsuario):
        self.hide()
        self.ventana4 = Ventana4(self, cedulaUsuario)
        self.ventana4.show()

    def metodo_botonVolver(self):
        self.hide()
        self.ventanaAnterior.show()

    def metodo_botonFormaTabular(self):
        self.hide()
        self.ventana3 = Ventana3(self)
        self.ventana3.show()

if __name__ == '__main__':

    # hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # crear un objeto de tipo Ventana1 con el nombre ventana1
    ventana2 = Ventana2()

    # hacer que el objeto ventana1 se vea
    ventana2.show()

    # codigo para terminar la aplicacion
    sys.exit(app.exec_())


