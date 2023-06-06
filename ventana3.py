import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QFormLayout, QApplication, QLineEdit, \
    QPushButton, QDialog, QDialogButtonBox, QVBoxLayout, QWidget, QButtonGroup, QGridLayout, QScrollArea, QTableWidget, \
    QTableWidgetItem, QToolBar, QAction, QMessageBox
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

        # ---- Construccion del toolbar----
        self.toolbar = QToolBar('Main Toolbar')
        self.toolbar.setIconSize(QSize(20, 20))
        self.addToolBar(self.toolbar)

        # toolbar eliminar
        self.delete = QAction(QIcon('imagenes/eliminar.png'), "&borrar", self)
        self.delete.triggered.connect(self.accion_delete)
        self.toolbar.addAction(self.delete)

        # toolbar agregar
        self.agregar = QAction(QIcon('imagenes/boton-agregar.png'), "&agregar", self)
        self.agregar.triggered.connect(self.accion_agregar)
        self.toolbar.addAction(self.agregar)

        # toolbar editar
        self.editar = QAction(QIcon('imagenes/editar.png'), "&editar", self)
        self.editar.triggered.connect(self.accion_editar)
        self.toolbar.addAction(self.editar)

        # ---- Fin toolbar------

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
            # evitar que se deje modificar
            self.tabla.item(self.contador, 0).setFlags(Qt.ItemIsEnabled)
            self.tabla.setItem(self.contador, 1, QTableWidgetItem(u.usuario))
            self.tabla.setItem(self.contador, 2, QTableWidgetItem(u.password))
            self.tabla.setItem(self.contador, 3, QTableWidgetItem(u.documento))
            # evitar que se deje modificar
            self.tabla.item(self.contador, 3).setFlags(Qt.ItemIsEnabled)
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

    def accion_delete(self):
        #me muestra la fila en la cual estoy ubicado
        filaActual = self.tabla.currentRow()

        #si la fila no existe
        if filaActual < 0:
            #ventana de warning
            return QMessageBox.warning(self, "Warning", "Para borrar, debe seleccionar un registro")

        #se hace una ventana mas sencilla, para confirmar
        boton = QMessageBox.question(
            self,
            'Confirmation',
            '¿Estas seguro de borrar este registro?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if boton == QMessageBox.StandardButton.Yes:

            if (
                    self.tabla.item(filaActual, 0).text() != '' and
                    self.tabla.item(filaActual, 1).text() != '' and
                    self.tabla.item(filaActual, 2).text() != '' and
                    self.tabla.item(filaActual, 3).text() != '' and
                    self.tabla.item(filaActual, 4).text() != '' and
                    self.tabla.item(filaActual, 5).text() != '' and
                    self.tabla.item(filaActual, 6).text() != '' and
                    self.tabla.item(filaActual, 7).text() != '' and
                    self.tabla.item(filaActual, 8).text() != '' and
                    self.tabla.item(filaActual, 9).text() != '' and
                    self.tabla.item(filaActual, 10).text() != ''
            ):
                # se abre el archivo solo lectura
                self.file = open('datos/clientes.txt', 'rb')

                usuarios = []

                while self.file:
                    linea = self.file.readline().decode('UTF-8')

                    lista = linea.split(';')

                    if linea == '':
                        break

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

                    usuarios.append(u)
                # se cierra el archivo
                self.file.close()

                for u in usuarios:

                    if (
                            u.documento == self.tabla.item(filaActual, 3).text()
                    ):
                        # sacamos el usuario
                        usuarios.remove(u)
                        #paramos el for
                        break
                #se abre el archivo en modo escritura
                self.file = open('datos/clientes.txt', 'wb')

                for u in usuarios:
                    self.file.write(bytes(u.nombrecompleto + ';' +
                                          u.usuario + ';' +
                                          u.password + ';' +
                                          u.documento + ';' +
                                          u.correo + ';' +
                                          u.pregunta1 + ';' +
                                          u.respuesta1 + ';' +
                                          u.pregunta2 + ';' +
                                          u.respuesta2 + ';' +
                                          u.pregunta3 + ';' +
                                          u.respuesta3, encoding='UTF-8'))
                #cerramos el archivo
                self.file.close()

                # hacemos que la tabla no se vea en el registro en la tabla
                self.tabla.removeRow(filaActual)

                #ventana de confirmacion
                return QMessageBox.question(
                    self,
                    'confirmation',
                    'El registro ha sido eliminado exitosamente.',
                    QMessageBox.StandardButton.Yes
                )
            else:
                # Hacemos que en la tabla no se vea el registro en caso de tratarse de na fila vacia
                self.tabla.removeRow(filaActual)

    def accion_agregar(self):
        #obtenemos el numero de filas que tiene la tabla
        ultimafila = self.tabla.rowCount()

        # insertas una fila nueva despues de la ultima fila
        self.tabla.insertRow(ultimafila)

        # LLenamos las celdas con espacios en blancos

        self.tabla.setItem(ultimafila, 0, QTableWidgetItem(''))
        self.tabla.setItem(ultimafila, 1, QTableWidgetItem(''))
        self.tabla.setItem(ultimafila, 2, QTableWidgetItem(''))
        self.tabla.setItem(ultimafila, 3, QTableWidgetItem(''))
        self.tabla.setItem(ultimafila, 4, QTableWidgetItem(''))
        self.tabla.setItem(ultimafila, 5, QTableWidgetItem(''))
        self.tabla.setItem(ultimafila, 6, QTableWidgetItem(''))
        self.tabla.setItem(ultimafila, 7, QTableWidgetItem(''))
        self.tabla.setItem(ultimafila, 8, QTableWidgetItem(''))
        self.tabla.setItem(ultimafila, 9, QTableWidgetItem(''))
        self.tabla.setItem(ultimafila, 10, QTableWidgetItem(''))

    def accion_editar(self):

        #me indica en que fila estoy
        filaActual = self.tabla.currentRow()

        # si es menor que 0 quiere decir que no tome nada
        if filaActual < 0:
            return QMessageBox.warning(
                self,
                'Warning',
                'Para ingresar debe seleccionar un registro.',

            )

        boton = QMessageBox.question(
            self,
            'Confirmation',
            '¿Seguro que quiere ingresar este nuevo registro?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        datosVacios = True

        if boton == QMessageBox.StandardButton.Yes:

            if (
                    self.tabla.item(filaActual, 0).text() != '' and
                    self.tabla.item(filaActual, 1).text() != '' and
                    self.tabla.item(filaActual, 2).text() != '' and
                    self.tabla.item(filaActual, 3).text() != '' and
                    self.tabla.item(filaActual, 4).text() != '' and
                    self.tabla.item(filaActual, 5).text() != '' and
                    self.tabla.item(filaActual, 6).text() != '' and
                    self.tabla.item(filaActual, 7).text() != '' and
                    self.tabla.item(filaActual, 8).text() != '' and
                    self.tabla.item(filaActual, 9).text() != '' and
                    self.tabla.item(filaActual, 10).text() != ''
            ):
                #Actualizamos la variable para indicar que se ingresaron todos los datos:
                datosVacios = False

                #abrimos en modo lectura
                self.file = open('datos/clientes.txt', 'rb')
                #la lista
                usuarios = []

                while self.file:
                    linea = self.file.readline().decode('UTF-8')
                    lista = linea.split(';')

                    if linea == '':
                        break

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

                    usuarios.append(u)

                self.file.close()

                # variables controladoras si existe registro y si se va a editar
                existeRegistro = False
                existeDocumento = False

                for u in usuarios:

                    if (
                            u.nombrecompleto == self.tabla.item(filaActual, 0).text() and
                            u.usuario == self.tabla.item(filaActual, 1).text() and
                            u.password == self.tabla.item(filaActual, 2).text() and
                            u.documento == self.tabla.item(filaActual, 3).text() and
                            u.correo == self.tabla.item(filaActual, 4).text() and
                            u.pregunta1 == self.tabla.item(filaActual, 5).text() and
                            u.respuesta1 == self.tabla.item(filaActual, 6).text() and
                            u.pregunta2 == self.tabla.item(filaActual, 7).text() and
                            u.respuesta2 == self.tabla.item(filaActual, 8).text() and
                            u.pregunta3 == self.tabla.item(filaActual, 9).text() and
                            u.respuesta3 == self.tabla.item(filaActual, 10).text()
                    ):
                        existeRegistro = True

                        return QMessageBox.warning(
                            self,
                            'Warning',
                            'Resgistro duplicado, no se pude registrar')
                        break

                if not existeRegistro:

                    for u in usuarios:

                        if (
                                u.documento == self.tabla.item(filaActual, 3).text()
                        ):

                            existeDocumento = True

                            #volvemos a actualizar todos los datos del usuario:
                            u.nombrecompleto = self.tabla.item(filaActual, 0).text()
                            u.usuario = self.tabla.item(filaActual, 1).text()
                            u.password = self.tabla.item(filaActual, 2).text()
                            u.documento = self.tabla.item(filaActual, 3).text()
                            u.correo = self.tabla.item(filaActual, 4).text()
                            u.pregunta1 = self.tabla.item(filaActual, 5).text()
                            u.respuesta1 = self.tabla.item(filaActual, 6).text()
                            u.pregunta2 = self.tabla.item(filaActual, 7).text()
                            u.respuesta2 = self.tabla.item(filaActual, 8).text()
                            u.pregunta3 = self.tabla.item(filaActual, 9).text()
                            u.respuesta3 = self.tabla.item(filaActual, 10).text()

                            #abrimos el archivo en escritura
                            self.file = open('datos/clientes.txt', 'wb')

                            for u in usuarios:
                                self.file.write(bytes(
                                    u.nombrecompleto + ';' +
                                    u.usuario + ';' +
                                    u.password + ';' +
                                    u.documento + ';' +
                                    u.correo + ';' +
                                    u.pregunta1 + ';' +
                                    u.respuesta1 + ';' +
                                    u.pregunta2 + ';' +
                                    u.respuesta2 + ';' +
                                    u.pregunta3 + ';' +
                                    u.respuesta3 +"\n", encoding='UTF-8'
                                ))

                            self.file.close()

                            return QMessageBox.question(
                                self,
                                'Confirmation',
                                'Los datos del registro se han editados exitosamente.',
                                QMessageBox.StandardButton.Ok
                            )
                            #paramos el for
                            break

                    if not existeDocumento:
                        #abrimos el archivo en modo agregar
                        self.file = open('datos/clientes.txt', 'ab')

                        self.file.write(bytes(
                            self.tabla.item(filaActual, 0).text() + ';' +
                            self.tabla.item(filaActual, 1).text() + ';' +
                            self.tabla.item(filaActual, 2).text() + ';' +
                            self.tabla.item(filaActual, 3).text() + ';' +
                            self.tabla.item(filaActual, 4).text() + ';' +
                            self.tabla.item(filaActual, 5).text() + ';' +
                            self.tabla.item(filaActual, 6).text() + ';' +
                            self.tabla.item(filaActual, 7).text() + ';' +
                            self.tabla.item(filaActual, 8).text() + ';' +
                            self.tabla.item(filaActual, 9).text() + ';' +
                            self.tabla.item(filaActual, 10).text() + '\n', encoding='UTF-8'))
                        #poner el cursor al final
                        self.file.seek(0, 2)
                        self.file.close()
                    return QMessageBox.question(
                        self,
                        'Confirmation',
                        'Los datos del registro se han ingresado correctamente.',
                        QMessageBox.StandardButton.Ok

                    )

            if datosVacios:
                return QMessageBox.warning(
                    self,
                    'Warning',
                    'Debe ingresar todos los datos en el registro'
                )

if __name__ == '__main__':

    # hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # crear un objeto de tipo Ventana1 con el nombre ventana1
    ventana3 = Ventana3()

    # hacer que el objeto ventana1 se vea
    ventana3.show()

    # codigo para terminar la aplicacion
    sys.exit(app.exec_())