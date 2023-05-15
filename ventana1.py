import sys

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QApplication, QFormLayout, QLineEdit, \
    QPushButton
from PyQt5 import QtGui, QtCore


class Ventana1(QMainWindow):
    # hacer el metodo de construccion de la ventana

    def __init__(self, parent=None):
        super(Ventana1, self).__init__(parent)

        # poner el titulo
        self.setWindowTitle("Formulario de registro")

        # poner icono
        self.setWindowIcon(QtGui.QIcon('imagenes/iconop.png'))

        # Estableciendo las propiedades de ancho y alto:
        self.ancho = 900
        self.alto = 600

        # Establecer el tamaño de la ventana:
        self.resize(self.ancho, self.alto)

        # Hacer que la ventana se vea en el centro:
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        # Fijar el ancho y el alto de la ventana:
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        # EstabLecemos el fondo principal:
        self.fondo = QLabel(self)

        # Defínimos la imagen de fondo:
        self.imagenFondo = QPixmap('imagenes/homer2..jpg')

        # Defínimos la imagen de fondo:
        self.fondo.setPixmap(self.imagenFondo)

        # Establecemos el modo para escalar la imagen:
        self.fondo.setScaledContents(True)

        # Hacemos que se adapte el tamaño de la imagen:
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        # Establecemos la ventana de fondo como la ventana central
        self.setCentralWidget(self.fondo)

        # Establecemos la distribución de los elementos en layout horizontal:
        self.horizontal = QHBoxLayout()

        # Le ponenos las margenes:
        self.horizontal.setContentsMargins(30, 30, 30, 30)

        # ----- LAYOUT IZQUIERDO-------

        # Creamos el layout del lado izquierdo
        self.ladoIzquierdo = QFormLayout()

        # Hacemos un letrero
        self.letrero1 = QLabel()

        # Le escribimos el texto
        self.letrero1.setText("Información del Cliente")

        # Asignamos tito de letra
        self.letrero1.setFont(QFont("Arial", 20))

        # Color de texto
        self.letrero1.setStyleSheet("Color: #FF0000")

        # Agregamos el letrero en la primera linea
        self.ladoIzquierdo.addRow(self.letrero1)

        # letrero2
        self.letrero2 = QLabel()

        # establecemos el ancho del lanel
        self.letrero2.setFixedWidth(340)

        # le escribimos el texto
        self.letrero2.setText("Por favor ingrese la información del cliente"
                              "\nen el formulario de abajo. Los campos marcados"
                              "\ncon asteriscos son obligatorios.")

        # Asignamos tito de letra
        self.letrero2.setFont(QFont("Andale Mono", 10))

        # Le ponemops color de textos y margenes
        self.letrero2.setStyleSheet("Color: red; margin-bottom: 40px;"
                                    "margin-top:20px;"
                                    "padding-bottom:10px;"
                                    "border: 2px solid #C0C0C0;"
                                    #solo pone la margen en el lado indicado
                                    "border-left: none;"
                                    "border-right: none;"
                                    "border-top: none;")

        # Agregamos el letrero en la primera linea
        self.ladoIzquierdo.addRow(self.letrero2)

        # Hacemos el campo para ingresar el nombre:
        self.nombrecompleto = QLineEdit()
        self.nombrecompleto.setFixedWidth(250)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Nombre Completo*", self.nombrecompleto)

        # Hacemos el campo para ingresar el usurio:
        self.usuario = QLineEdit()
        self.usuario.setFixedWidth(250)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Usuario*", self.usuario)

        # Hacemos el campo para ingresar el password:
        self.password = QLineEdit()
        self.password.setFixedWidth(250)
        self.password.setEchoMode(QLineEdit.Password)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Password*", self.password)

        # Hacemos el campo para ingresar el possword2:
        self.password2 = QLineEdit()
        self.password2.setFixedWidth(250)
        self.password2.setEchoMode(QLineEdit.Password)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Password*", self.password2)

        # Hacemos el campo para ingresar el documento:
        self.documento = QLineEdit()
        self.documento.setFixedWidth(250)

        # Agregamos estos en el fotmulario:
        self.ladoIzquierdo.addRow("Documento*", self.documento)

        # Hacemos el campo para ingresar el correo:
        self.correo = QLineEdit()
        self.correo.setFixedWidth(250)
        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Correo*", self.correo)

        # Agregamos el layout lado Izquierdo al layout horicontal
        self.horizontal.addLayout(self.ladoIzquierdo)

        # hacemos un boton para registrar los datos
        self.botonRegistrar = QPushButton("Registrar")
        # establecemos el ancho del botton
        self.botonRegistrar.setFixedWidth(90)

        # le establecemos los estilos
        self.botonRegistrar.setStyleSheet("background-color: #008B45;"
                                          "color: #FFFFFF;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")

        self.botonRegistrar.clicked.connect(self.accion_botonRegistrar)

        # hacemos el boton para limpiar los datos
        self.botonLimpiar = QPushButton("Limpiar")
        self.botonLimpiar.setFixedWidth(90)

        # le establecemos los estilos
        self.botonLimpiar.setStyleSheet("background-color: #008B45;"
                                        "color: #FFFFFF;"
                                        "padding: 10px;"
                                        "margin-top: 40px;")
        self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)

        # agregamos los botones al layout izquierdo
        self.ladoIzquierdo.addRow(self.botonRegistrar, self.botonLimpiar)


        #--poner al final siempre  -----------

        # Indicamos que el layout principal del fondo es horizontal
        self.fondo.setLayout(self.horizontal)

    def accion_botonLimpiar(self):
        pass

    def accion_botonRegistrar(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ventana1 = Ventana1()

    ventana1.show()

    sys.exit(app.exec_())
