import sys

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QVBoxLayout, QScrollArea, QTableWidget, \
    QTableWidgetItem, QPushButton, QApplication
from PyQt5 import QtGui
from cliente import Cliente

class Ventana3(QMainWindow):
     #constructor y guardar ventana anterior
    def __init__(self, anterior):
        super(Ventana3, self).__init__(anterior)

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
        self.imagenFondo = QPixmap("imagenes/homer2.jpg")

        #definimos imagen de fondo
        self.fondo.setPixmap(self.imagenFondo)

        #establecemos modo para escalar la imagen
        self.fondo.setScaledContents(True)

        #hacemos que se adapte al tamaño de la imagen
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        #establecemos la ventana de fondo como fondo central
        self.setCentralWidget(self.fondo)


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

        # En este punto tenemos la lista usuarios con todos los usuarios

        self.numeroUsuarios = len(self.usuarios)

        self.contador = 0

        self.vertical = QVBoxLayout()

        self.letrero1 = QLabel()

        self.letrero1.setText("Usuarios Registrados")

        self.letrero1.setFont(QFont("Arial", 20))

        self.letrero1.setStyleSheet(" color: #FFFFFF;")

        self.vertical.addWidget(self.letrero1)

        self.vertical.addStretch()

        self.scrollArea = QScrollArea()
        #ajustable
        self.scrollArea.setWidgetResizable(True)
        #creamos tabla
        self.tabla = QTableWidget()
        #columnas de la tabla
        self.tabla.setColumnCount(11)

        #indico los 11 elementos
        self.tabla.setColumnWidth(0, 150)
        self.tabla.setColumnWidth(1, 150)
        self.tabla.setColumnWidth(2, 150)
        self.tabla.setColumnWidth(3, 150)
        self.tabla.setColumnWidth(4, 150)
        self.tabla.setColumnWidth(5, 150)
        self.tabla.setColumnWidth(6, 150)
        self.tabla.setColumnWidth(7, 150)
        self.tabla.setColumnWidth(8, 150)
        self.tabla.setColumnWidth(9, 150)
        self.tabla.setColumnWidth(10, 150)

        #los nombres que le corresponden a la tabla
        self.tabla.setHorizontalHeaderLabels(['Nombre',
                                              'Usuario',
                                              'Contraseña',
                                              'Documento',
                                              'Correo',
                                              'Pregunta 1',
                                              'Respuesta 1',
                                              'Pregunta 2',
                                              'Respuesta 2',
                                              'Pregunta 3',
                                              'Respuesta 3'])
        #ESTABLECEMOS EL NUMERO DE FILA
        self.tabla.setRowCount(self.numeroUsuarios)

        #LLENAMOS LA TABLA
        for u in self.usuarios:
            self.tabla.setItem(self.contador, 0, QTableWidgetItem(u.nombrecompleto))
            self.tabla.setItem(self.contador, 1, QTableWidgetItem(u.usuario))
            self.tabla.setItem(self.contador, 2, QTableWidgetItem(u.password))
            self.tabla.setItem(self.contador, 3, QTableWidgetItem(u.documento))
            self.tabla.setItem(self.contador, 4, QTableWidgetItem(u.correo))
            self.tabla.setItem(self.contador, 5, QTableWidgetItem(u.pregunta1))
            self.tabla.setItem(self.contador, 6, QTableWidgetItem(u.respuesta1))
            self.tabla.setItem(self.contador, 7, QTableWidgetItem(u.pregunta2))
            self.tabla.setItem(self.contador, 8, QTableWidgetItem(u.respuesta2))
            self.tabla.setItem(self.contador, 9, QTableWidgetItem(u.pregunta3))
            self.tabla.setItem(self.contador, 10, QTableWidgetItem(u.respuesta3))
            self.contador += 1

        #GUARDAMOS LA TABLA EN EL SCROLL
        self.scrollArea.setWidget(self.tabla)

        #AGREGAMOS EL SCROLL AL LAYOUT
        self.vertical.addWidget(self.scrollArea)

        #agregamos espacio
        self.vertical.addStretch()

        #------------ BOTON VOLVER ----
        self.botonVolver = QPushButton("Volver")

        self.botonVolver.setFixedWidth(90)

        self.botonVolver.setStyleSheet("background-color : #FFFFFF;"
                                       "color : #000000;"
                                       "padding: 10 px;"
                                       )

        self.botonVolver.clicked.connect(self.metodo_botonVolver)

        self.vertical.addWidget(self.botonVolver)

        #-----------OJO PONER AL FINAL DIOS MIO-------------
        self.fondo.setLayout(self.vertical)


    def metodo_botonVolver(self):
        self.hide()
        self.ventanaAnterior.show()

if __name__ == '__main__':

    # hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # crear un objeto de tipo Ventana1 con el nombre ventana1
    ventana3 = Ventana3()

    # hacer que el objeto ventana1 se vea
    ventana3.show()

    # codigo para terminar la aplicacion
    sys.exit(app.exec_())