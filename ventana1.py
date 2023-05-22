import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QApplication, QFormLayout, QLineEdit, \
    QPushButton, QDialog, QDialogButtonBox, QVBoxLayout
from PyQt5 import QtGui, QtCore
from cliente import Cliente


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

        # -----Layout derecho----
        # cramos el layout del lado derecho
        self.ladoDerecho = QFormLayout()

        # se asigna la margen solo a la izquierda
        self.ladoDerecho.setContentsMargins(100, 0, 0, 0)

        # hacemos el letrero
        self.letrero3 = QLabel()

        # le escribimos el texto
        self.letrero3.setText("Recuperar Contraseña")

        # Asignamos tipo de letra
        self.letrero3.setFont(QFont("Andale Mono", 20))

        # Color de texto
        self.letrero3.setStyleSheet("Color: #Black")

        # agregamos el letrero a la primera fila
        self.ladoDerecho.addRow(self.letrero3)

        self.letrero4 = QLabel()

        # establecemos el ancho del label
        self.letrero4.setFixedWidth(400)

        # le escribimos el texto
        self.letrero4.setText("Por favor ingrese la información para recuperar"
                              "\nla contraseña. Los campos marcados "
                              "\ncon asteriscos son obligatorios.")

        # Asignamos tipo de letra
        self.letrero3.setFont(QFont("Andale Mono", 20))

        # Le ponemops color de textos y margenes
        self.letrero4.setStyleSheet("Color: red; margin-bottom: 40px;"
                                    "margin-top:20px;"
                                    "padding-bottom:10px;"
                                    "border: 2px solid #C0C0C0;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "border-top: none;")

        # agregemos el letrero a la fila siguiente
        self.ladoDerecho.addRow(self.letrero4)

        # --1

        # hacemos el letrero de la pregunta 1
        self.labelPregunta1 = QLabel("Pregunta de verificación 1*")
        # agregaos el letrero a la fila siguiente
        self.ladoDerecho.addRow(self.labelPregunta1)
        # hacemnos el campo para ingresar la pregunta 1
        self.pregunta1 = QLineEdit()
        self.pregunta1.setFixedWidth(320)
        # agregemos el p1 a la fila siguiente
        self.ladoDerecho.addRow(self.pregunta1)

        # hacemos el letrero de la respuesta1
        self.labelRespuesta1 = QLabel("Respuesta de verificación 1*")
        # agregaos el letrero a la fila siguiente
        self.ladoDerecho.addRow(self.labelRespuesta1)
        # hacemnos el campo para ingresar la respuesta 1
        self.respuesta1 = QLineEdit()
        self.respuesta1.setFixedWidth(320)
        # agregemos el p1 a la fila siguiente
        self.ladoDerecho.addRow(self.respuesta1)

        # --2
        # hacemos el letrero de la pregunta 2
        self.labelPregunta2 = QLabel("Pregunta de verificación 2*")
        # agregaos el letrero a la fila siguiente
        self.ladoDerecho.addRow(self.labelPregunta2)
        # hacemnos el campo para ingresar la pregunta 2
        self.pregunta2 = QLineEdit()
        self.pregunta2.setFixedWidth(320)
        # agregemos el p2 a la fila siguiente
        self.ladoDerecho.addRow(self.pregunta2)

        # hacemos el letrero de la respuesta2
        self.labelRespuesta2 = QLabel("Respuesta de verificación 2*")
        # agregaos el letrero a la fila siguiente
        self.ladoDerecho.addRow(self.labelRespuesta2)
        # hacemnos el campo para ingresar la respuesta 2
        self.respuesta2 = QLineEdit()
        self.respuesta2.setFixedWidth(320)
        # agregemos el p2 a la fila siguiente
        self.ladoDerecho.addRow(self.respuesta2)

        # ---3
        # hacemos el letrero de la pregunta 3
        self.labelPregunta3 = QLabel("Pregunta de verificación 3*")
        # agregaos el letrero a la fila siguiente
        self.ladoDerecho.addRow(self.labelPregunta3)
        # hacemnos el campo para ingresar la pregunta 3
        self.pregunta3 = QLineEdit()
        self.pregunta3.setFixedWidth(320)
        # agregemos el p3 a la fila siguiente
        self.ladoDerecho.addRow(self.pregunta3)

        # hacemos el letrero de la respuesta3
        self.labelRespuesta3 = QLabel("Respuesta de verificación 3*")
        # agregaos el letrero a la fila siguiente
        self.ladoDerecho.addRow(self.labelRespuesta3)
        # hacemnos el campo para ingresar la respuesta 3
        self.respuesta3 = QLineEdit()
        self.respuesta3.setFixedWidth(320)
        # agregemos el p3 a la fila siguiente
        self.ladoDerecho.addRow(self.respuesta3)

        # hacemos el boton para buscar las preguntas
        self.botonBuscar = QPushButton("Buscar")
        self.botonBuscar.setFixedWidth(90)

        # le establecemos los estilos
        self.botonBuscar.setStyleSheet("background-color: #008B45;"
                                       "color: #FFFFFF;"
                                       "padding: 10px;"
                                       "margin-top: 40px;"
                                       )

        # Hacemos que el boton botonBuscar tenga su metodo:
        self.botonBuscar.clicked.connect(self.accion_botonBuscar)

        # hacemos el boton para recuperar la contraseña:
        self.botonRecuperar = QPushButton("Recuperar")

        # Establecemos el ancho de el boton:

        # Establecemos el ancho de el boton:

        self.botonRecuperar.setFixedWidth(90)

        # le establecemos los estilos
        self.botonRecuperar.setStyleSheet("background-color: #008B45;"
                                          "color: #FFFFFF;"
                                          "padding: 10px;"
                                          "margin-top: 40px;"
                                          )

        # hacemos que el botonRecuperar tenga su metodo
        #self.botonRecuperar.clicked.connect(self.accion_bontonRecuperar)

        # agregamos los botones al layout derecho
        self.ladoDerecho.addRow(self.botonBuscar, self.botonRecuperar)


        # agregamos el layout ladoDerecho al layout horizontal
        self.horizontal.addLayout(self.ladoDerecho)


        #--poner al final siempre  -----------

        # Indicamos que el layout principal del fondo es horizontal
        self.fondo.setLayout(self.horizontal)

        # creamos la ventana de dialogo
        self.ventanaDialogo = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)

        # definimos el tamaño de la ventana
        self.ventanaDialogo.resize(300, 150)

        # creamos el boton para aceptar

        self.botonAceptar = QDialogButtonBox.Ok
        self.opciones = QDialogButtonBox(self.botonAceptar)
        self.opciones.accepted.connect(self.ventanaDialogo.accept)

        # establecemos el titulo de la ventana
        self.ventanaDialogo.setWindowTitle("Formulario de registro")

        # ventana modal
        self.ventanaDialogo.setWindowModality(Qt.ApplicationModal)

        # creamos el layout vertical
        self.vertical = QVBoxLayout()

        # creamos el label para los mensajes
        self.mensaje = QLabel("")

        # le ponemos estilo al label mensaje
        self.mensaje.setStyleSheet("background-color: #008B45; color: #FFFFFF; padding: 10px;")

        # agregamos el label mensajes
        self.vertical.addWidget(self.mensaje)

        # agregamos las opciones de los botones
        self.vertical.addWidget(self.opciones)

        # establecemos el layout para la ventana
        self.ventanaDialogo.setLayout(self.vertical)




    def accion_botonLimpiar(self):
        self.nombrecompleto.setText('')
        self.usuario.setText('')
        self.password.setText('')
        self.password2.setText('')
        self.documento.setText('')
        self.correo.setText('')
        self.pregunta1.setText('')
        self.respuesta1.setText('')
        self.pregunta2.setText('')
        self.respuesta2.setText('')
        self.pregunta3.setText('')
        self.respuesta3.setText('')


    def accion_botonRegistrar(self):

        # variable para controral si el ingreso de los datos estan correctos
        self.datosCorrectos = True


        # validamos que los passwords sean iguales

        # validamos que los passwords sean iguales

        if (self.password.text() != self.password2.text()):
            self.datosCorrectos = False

            # Escribimos el texto explicativo
            self.mensaje.setText("Los passwords no son iguales")

            self.ventanaDialogo.exec_()

            # Se valida para que se ingresen todos los campos
        if (
                self.nombrecompleto.text() == ''
                or self.usuario.text() == ''
                or self.password.text() == ''
                or self.documento.text() == ''
                or self.correo.text() == ''
                or self.pregunta1.text() == ''
                or self.respuesta1.text() == ''
                or self.pregunta2.text() == ''
                or self.respuesta2.text() == ''
                or self.pregunta3.text() == ''
                or self.respuesta3.text() == ''
        ):
            self.datosCorrectos = False

            # escribimos el texto explicativo
            self.mensaje.setText("Debe ingresar todos los campos")

            # hacemos que la ventana de dialogo se vea
            self.ventanaDialogo.exec_()

            # si los datos estan correctos:
        if self.datosCorrectos:

            # abrimos el archivo en modo agregar escribiendo datos en binario

            self.file = open('datos/clientes.txt', 'ab')

            # traer el texto de los QLineEdit y los agrega concatenandolos
            # para escribirlos en formato binario utf-8
            self.file.write(bytes(
                self.nombrecompleto.text() + ";"
                + self.usuario.text() + ";"
                + self.password.text() + ";"
                + self.documento.text() + ";"
                + self.correo.text() + ";"
                + self.pregunta1.text() + ";"
                + self.respuesta1.text() + ";"
                + self.pregunta2.text() + ";"
                + self.respuesta2.text() + ";"
                + self.pregunta3.text() + ";"
                + self.respuesta3.text() + "\n"
                , encoding='UTF-8'))
            # cerramos el archivo
            self.file.close()

            # abrimos en modo lectura el formato bytes
            self.file = open('datos/clientes.txt', 'rb')
            # recorrer el archivo linea por linea
            while self.file:
                linea = self.file.readline().decode('UTF-8')
                print(linea)
                if linea == '':  # para cuando se encuentre una linea vacia

                    break
            self.file.close()

    #metodo del boton buscar

    def accion_botonBuscar(self):

        # variable para controral si el ingreso de los datos estan correctos
        self.datosCorrectos = True

        # Establecemos el título de la ventana:
        self.ventanaDialogo.setWindowTitle("Buscar preguntas de validación")

        # Validar que se haya ingresado el documento:
        if (
                self.documento.text() == ''
        ):
            self.datosCorrectos = False

            # Escribimos el texto explicativo:
            self.mensaje.setText("Si va a buscar las preguntas "
                                 "para recuperar la contraseña. "
                                 "\nDebe primero, ingresar el documento.")

            # Hacemos que la ventana de diálogo se vea:
            self.ventanaDialogo.exec_()

        # Validar si el documento es numérico:
        if (
                not self.documento.text().isnumeric()
        ):
            self.datosCorrectos = False

            # Escribimos el texto explicativo:
            self.mensaje.setText("El documento debe ser numérico. "
                                 "\nNO ingrese letras "
                                 "Ni caracteres especiales.")

            # Hacemos que la ventana de diálogo se vea:
            self.ventanaDialogo.exec_()

            # Limpiamos el campo del documento:
            self.documento.setText('')

        # Si los datos están correctos
        if (
                self.datosCorrectos
        ):
            # Abrimos el archivo en modo lectura:
            self.file = open('datos/clientes.txt', 'rb')

            # Lista vacía para agregar todos los usuarios:
            usuarios = []

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
                usuarios.append(u)

            # Cerramos el archivo:
            self.file.close()

            # En este punto tenemos la lista usuario con todos los usuarios:

            # Variable para controlar si existe el documento:
            existeDocumento = False

            # Buscamos en la lista usuario por usuario si existe la cédula:
            for u in usuarios:

                # Comparamos el documento ingresado:
                # Si corresponde con el documento, es el usuario correcto:
                if u.documento == self.documento.text():
                    # Mostramos las preguntas en el formulario:
                    self.pregunta1.setText(u.pregunta1)
                    self.pregunta2.setText(u.pregunta2)
                    self.pregunta3.setText(u.pregunta3)
                    # Indicamos que encontramos el usuario:
                    existeDocumento = True

                    # Paramos el for:
                    break

            # Si no existe un usuario con este documento:
            if (
                    not existeDocumento
            ):
                # Escribimos el texto explicativo:
                self.mensaje.setText("No existe un usuario con este documento:\n"
                                     + self.documento.text())

                # Hacemos que la ventana de diálogo se vea:
                self.ventanaDialogo.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ventana1 = Ventana1()

    ventana1.show()

    sys.exit(app.exec_())
