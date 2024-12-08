import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from window_biblio import Ui_MainWindow
import os

# Funciones auxiliares para manejo de archivos
def guardar_en_archivo(nombre_archivo, datos):
    with open(nombre_archivo, 'a') as archivo:
        archivo.write(datos + '\n')


def leer_archivo(nombre_archivo):
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'r') as archivo:
            return [line.strip() for line in archivo.readlines()]
    return []

class Ventana(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~@
        # Acciones de Botones en Tab de Libros
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~@
        self.agr_lib_btm.clicked.connect(self.agregar_libro)
        self.consultar_libro_btm.clicked.connect(self.consultar_libro)
        #self.cancel_agr_lib_btm.clicked.connect(self.cancelar_agregar_libro)
        self.edit_lib_btm.clicked.connect(self.editar_libro)
        #self.cancel_edit_lib_btm.clicked.connect(self.cancelar_editar_libro)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~@
        # Acciones de Botones en Tab de Usuarios
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~@
        self.reg_usr_btm.clicked.connect(self.registrar_usuario)
        self.consultar_usuarios_btm.clicked.connect(self.consultar_usuarios)
        #self.cancel_reg_usr_btm.clicked.connect(self.cancelar_registro_usuario)
        self.edit_usr_btm.clicked.connect(self.editar_usuario)
        #self.cancel_edit_usr_btm.clicked.connect(self.cancelar_editar_usuario)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~@
        # Acciones de Botones en Tab de Prestamos
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~@
        self.reg_prestamo_btm.clicked.connect(self.registrar_prestamo)
        #self.cancel_reg_prestamo_btm.clicked.connect(self.cancelar_prestamo)
        self.reg_devolucion_btm.clicked.connect(self.registrar_devolucion)
        #self.cancel_reg_devolucion_btm.clicked.connect(self.cancelar_devolucion)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~@
        # Acciones de Botones en Tab de Historial
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~@
        self.consultar_historial_btm.clicked.connect(self.consultar_historial)
    
#=> Habilitar/Deshabilitar tabs para tipo de Usuario
    def configurar_rol(self): 
        if self.rol == "Lector": 
            self.tabHistor.setEnabled(False) 
            self.tabLibros.setEnabled(False) 
            self.tabUser.setEnabled(False) 
            self.tabPrest.setEnabled(False) 
        elif self.rol == "Bibliotecario": 
            self.tabHistor.setEnabled(True) 
            self.tabLibros.setEnabled(True) 
            self.tabUser.setEnabled(True) 
            self.tabPrest.setEnabled(True) 
        else: 
            pass

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~@
    # Acciones de Botones en Tab de Libros
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~@
    def agregar_libro(self):
        titulo = self.Ag_LibTitulo_LEdit.text()
        autor = self.Ag_LibAutor_LEdit.text()
        isbn = self.Ag_LibISBN_LEdit.text()
        estado = "Disponible"
        datos = f"{isbn},{titulo},{autor},{estado}"
        guardar_en_archivo('libros.txt', datos)
        self.Ag_LibTitulo_LEdit.setText("")
        self.Ag_LibAutor_LEdit.setText("")
        self.Ag_LibISBN_LEdit.setText("")
        self.consultar_libro()  # Actualizar la lista de libros

    def consultar_libro(self):
        libros = leer_archivo('libros.txt')
        self.list_libros.clear()  # Limpiar la lista actual
        for libro in libros:
            self.list_libros.addItem(libro)  # Añadir cada libro a la lista

    def editar_libro(self):
        isbn = self.selct_isbn_comboBx.currentText()
        titulo = self.edit_LibTitulo_LEdit.text()
        autor = self.edit_LibAutor_LEdit.text()
        estado = self.edit_LibEstado_LEdit.text()
        libros = leer_archivo('libros.txt')
        nuevo_estado_libros = []
        for linea in libros:
            campos = linea.split(',')
            if campos[0] == isbn:
                nuevo_estado_libros.append(f"{isbn},{titulo},{autor},{estado}")
            else:
                nuevo_estado_libros.append(linea)
        with open('libros.txt', 'w') as archivo:
            archivo.write('\n'.join(nuevo_estado_libros) + '\n')
        self.edit_LibTitulo_LEdit.setText("")
        self.edit_LibAutor_LEdit.setText("")
        self.edit_LibEstado_LEdit.setText("")
        self.consultar_libro()  # Actualizar la lista de libros

    # Funciones para Gestión de Usuarios
    def registrar_usuario(self):
        id_usuario = self.Reg_UsrID_LEdit.text()
        nombre = self.Reg_UsrName_LEdit.text()
        rol = self.Reg_UsrRol_LEdit.text()
        datos = f"{id_usuario},{nombre},{rol}"
        guardar_en_archivo('usuarios.txt', datos)
        self.Reg_UsrID_LEdit.setText("")
        self.Reg_UsrName_LEdit.setText("")
        self.Reg_UsrRol_LEdit.setText("")
        self.consultar_usuarios()  # Actualizar la lista de usuarios

    def consultar_usuarios(self):
        usuarios = leer_archivo('usuarios.txt')
        self.listUsuarios.clear()  # Limpiar la lista actual
        for usuario in usuarios:
            self.listUsuarios.addItem(usuario)  # Añadir cada usuario a la lista

    def editar_usuario(self):
        id_usuario = self.selct_usrID_comboBx.currentText()
        nombre = self.Edit_Reg_UsrName_LEdit.text()
        rol = self.Edit_Reg_UsrRol_LEdit.text()
        usuarios = leer_archivo('usuarios.txt')
        nuevo_estado_usuarios = []
        for linea in usuarios:
            campos = linea.split(',')
            if campos[0] == id_usuario:
                nuevo_estado_usuarios.append(f"{id_usuario},{nombre},{rol}")
            else:
                nuevo_estado_usuarios.append(linea)
        with open('usuarios.txt', 'w') as archivo:
            archivo.write('\n'.join(nuevo_estado_usuarios) + '\n')
        self.Edit_Reg_UsrName_LEdit.setText("")
        self.Edit_Reg_UsrRol_LEdit.setText("")
        self.consultar_usuarios()  # Actualizar la lista de usuarios

    # Funciones para Gestión de Préstamos
    def registrar_prestamo(self):
        usuario = self.Reg_UsrName_LEdit.text()
        libro = self.selct_isbn_comboBx.currentText()
        fecha_prestamo = "01/01/2024"  # Sustituir por una fecha real
        libros = leer_archivo('libros.txt')
        nuevo_estado_libros = []
        prestado = False
        for linea in libros:
            isbn, titulo, autor, estado = linea.split(',')
            if titulo == libro and estado == "Disponible":
                nuevo_estado_libros.append(f"{isbn},{titulo},{autor},No Disponible")
                prestado = True
            else:
                nuevo_estado_libros.append(linea)
        if not prestado:
            return
        datos_prestamo = f"{usuario},{libro},{fecha_prestamo}"
        guardar_en_archivo('prestamos.txt', datos_prestamo)
        with open('libros.txt', 'w') as archivo:
            archivo.write('\n'.join(nuevo_estado_libros) + '\n')
        self.consultar_libro()
        self.consultar_historial()

    def registrar_devolucion(self):
        usuario = self.Reg_UsrName_LEdit.text()
        libro = self.selct_isbn_comboBx.currentText()
        libros = leer_archivo('libros.txt')
        nuevo_estado_libros = []
        devuelto = False
        for linea in libros:
            isbn, titulo, autor, estado = linea.split(',')
            if titulo == libro and estado == "No Disponible":
                nuevo_estado_libros.append(f"{isbn},{titulo},{autor},Disponible")
                devuelto = True
            else:
                nuevo_estado_libros.append(linea)
        if not devuelto:
            return
        with open('libros.txt', 'w') as archivo:
            archivo.write('\n'.join(nuevo_estado_libros) + '\n')
        self.consultar_libro()
        self.consultar_historial()

    # Función para consultar historial
    def consultar_historial(self):
        historial = leer_archivo('prestamos.txt')
        self.listPrestamos.clear()  # Limpiar la lista actual
        for prestamo in historial:
            self.listPrestamos.addItem(prestamo)  # Añadir cada préstamo a la lista


def main():
    app = QApplication(sys.argv) 
    login_window = Ventana() 
    login_window.show() 
    sys.exit(app.exec()) 
if __name__ == "__main__": 
    main()

