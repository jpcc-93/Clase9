import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QVBoxLayout, QLabel, QApplication
from PyQt5 import QtGui


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



        #--poner al final siempre  -----------

        # Indicamos que el layout principal del fondo es horizontal
        self.fondo.setLayout(self.vertical)

        
if __name__ == '__main__':

    # hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # crear un objeto de tipo Ventana1 con el nombre ventana1
    ventana2 = Ventana2()

    # hacer que el objeto ventana1 se vea
    ventana2.show()

    # codigo para terminar la aplicacion
    sys.exit(app.exec_())


