import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.QtCore import QDateTime
from window_biblio import Ui_MainWindow
from main_login import LoginWindow
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
        # Configurar el menú de "Salir"
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~@ 
        # Conectar el botón de salida con la función salir
        self.menuSalir.triggered.connect(self.salir)
        
        # Instancia de la ventana de Login (aún no visible)
        self.login_window = LoginWindow()  # Crear la instancia de LoginWindow

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~@
        # Acciones de Botones en Tab de Libros
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~@
        self.agr_lib_btm.clicked.connect(self.agregar_libro)
        self.consultar_libro_btm.clicked.connect(self.consultar_libro)
        self.edit_lib_btm.clicked.connect(self.editar_libro)
        self.selct_isbn_comboBx.currentIndexChanged.connect(self.cargar_datos_libro)

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~@
        # Acciones de Botones en Tab de Usuarios
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~@
        self.reg_usr_btm.clicked.connect(self.registrar_usuario)
        self.consultar_usuarios_btm.clicked.connect(self.consultar_usuarios)
        self.edit_usr_btm.clicked.connect(self.editar_usuario)
        self.selct_usrID_comboBx.currentIndexChanged.connect(self.cargar_datos_usuario)

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~@
        # Acciones de Botones en Tab de Préstamos
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~@
        self.reg_prestamo_btm.clicked.connect(self.registrar_prestamo)
        self.reg_devolucion_btm.clicked.connect(self.registrar_devolucion)

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~@
        # Acciones de Botones en Tab de Historial
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~@
        self.consultar_historial_btm.clicked.connect(self.consultar_historial)

        # Inicializar ComboBox
        self.actualizar_combo_isbn()
        self.actualizar_combo_usuarios()
        self.actualizar_combo_libros_prestamo()

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
    # Funciones para Gestión de Libros
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~@
    def agregar_libro(self):
        titulo = self.Ag_LibTitulo_LEdit.text()
        autor = self.Ag_LibAutor_LEdit.text()
        isbn = self.Ag_LibISBN_LEdit.text()
        estado = "Disponible"
        datos = f"{isbn},{titulo},{autor},{estado}"
        guardar_en_archivo('libros.txt', datos)
        self.Ag_LibTitulo_LEdit.clear()
        self.Ag_LibAutor_LEdit.clear()
        self.Ag_LibISBN_LEdit.clear()
        self.consultar_libro()
        self.actualizar_combo_isbn()

    def consultar_libro(self):
        libros = leer_archivo('libros.txt')
        self.list_libros.clear()
        for libro in libros:
            self.list_libros.addItem(libro)

    def cargar_datos_libro(self):
        isbn_seleccionado = self.selct_isbn_comboBx.currentText()
        if not isbn_seleccionado:
            return
        libros = leer_archivo('libros.txt')
        for linea in libros:
            isbn, titulo, autor, estado = linea.split(',')
            if isbn == isbn_seleccionado:
                self.edit_LibTitulo_LEdit.setText(titulo)
                self.edit_LibAutor_LEdit.setText(autor)
                self.edit_LibEstado_LEdit.setText(estado)
                break

    def editar_libro(self):
        isbn_seleccionado = self.selct_isbn_comboBx.currentText()
        if not isbn_seleccionado:
            QMessageBox.warning(self, "Error", "Selecciona un ISBN para editar.")
            return
        titulo = self.edit_LibTitulo_LEdit.text()
        autor = self.edit_LibAutor_LEdit.text()
        estado = self.edit_LibEstado_LEdit.text()

        libros = leer_archivo('libros.txt')
        nuevo_estado_libros = []
        for linea in libros:
            isbn, titulo_actual, autor_actual, estado_actual = linea.split(',')
            if isbn == isbn_seleccionado:
                nuevo_estado_libros.append(f"{isbn},{titulo},{autor},{estado}")
            else:
                nuevo_estado_libros.append(linea)

        with open('libros.txt', 'w') as archivo:
            archivo.write('\n'.join(nuevo_estado_libros) + '\n')

        QMessageBox.information(self, "Libro Editado", f"El libro con ISBN '{isbn_seleccionado}' ha sido actualizado.")
        self.consultar_libro()

    def actualizar_combo_isbn(self):
        libros = leer_archivo('libros.txt')
        self.selct_isbn_comboBx.clear()
        for linea in libros:
            isbn, _, _, _ = linea.split(',')
            self.selct_isbn_comboBx.addItem(isbn)

    def actualizar_combo_libros_prestamo(self):
        libros = leer_archivo('libros.txt')
        self.Reg_libPrestamo_comboBox.clear()
        self.Reg_libDevolucion_comboBox.clear()
        for linea in libros:
            isbn, _, _, estado = linea.split(',')
            if estado == "Disponible":
                self.Reg_libPrestamo_comboBox.addItem(isbn)
            elif estado == "No Disponible":
                self.Reg_libDevolucion_comboBox.addItem(isbn)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~@
    # Funciones para Gestión de Usuarios
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~@
    def validar_entrada(self, valor):
        """Validar que un campo no tenga caracteres no validos."""
        if not re.match(r'^[\w\s\u00C0-\u017F]*$', valor):
            return False
        return True

    def registrar_usuario(self):
        try:
            id_usuario = self.Reg_UsrID_LEdit.text().strip()
            nombre = self.Reg_UsrName_LEdit.text().strip()
            rol = self.Reg_UsrRol_LEdit.text().strip()

            # Validar campos
            if not id_usuario:
                QMessageBox.warning(self, "Error", "El campo 'ID de Usuario' no puede estar vacio.")
                return
            if not self.validar_entrada(nombre):
                QMessageBox.critical(self, "Error de Caracteres", "El campo 'Nombre' contiene caracteres no validos.")
                return
            if not self.validar_entrada(rol):
                QMessageBox.critical(self, "Error de Caracteres", "El campo 'Rol' contiene caracteres no validos.")
                return

            # Guardar datos
            datos = f"{id_usuario},{nombre},{rol}"
            self.guardar_en_archivo('usuarios.txt', datos)

            # Limpiar campos y actualizar vista
            self.Reg_UsrID_LEdit.clear()
            self.Reg_UsrName_LEdit.clear()
            self.Reg_UsrRol_LEdit.clear()
            self.consultar_usuarios() 
            self.actualizar_combo_usuarios() 

            QMessageBox.information(self, "Usuario Registrado", f"El usuario '{nombre}' ha sido registrado exitosamente.")
        
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Ocurrió un error inesperado: {str(e)}")

    def consultar_usuarios(self):
        usuarios = leer_archivo('usuarios.txt')
        self.listUsuarios.clear()
        for usuario in usuarios:
            self.listUsuarios.addItem(usuario)

    def cargar_datos_usuario(self):
        id_usuario_seleccionado = self.selct_usrID_comboBx.currentText()
        if not id_usuario_seleccionado:
            return
        usuarios = leer_archivo('usuarios.txt')
        for linea in usuarios:
            id_usuario, nombre, rol = linea.split(',')
            if id_usuario == id_usuario_seleccionado:
                self.Edit_Reg_UsrName_LEdit.setText(nombre)
                self.Edit_Reg_UsrRol_LEdit.setText(rol)
                break

    def editar_usuario(self):
        id_usuario_seleccionado = self.selct_usrID_comboBx.currentText()
        if not id_usuario_seleccionado:
            QMessageBox.warning(self, "Error", "Selecciona un ID de Usuario para editar.")
            return
        nombre = self.Edit_Reg_UsrName_LEdit.text()
        rol = self.Edit_Reg_UsrRol_LEdit.text()

        usuarios = leer_archivo('usuarios.txt')
        nuevo_estado_usuarios = []
        for linea in usuarios:
            id_usuario, nombre_actual, rol_actual = linea.split(',')
            if id_usuario == id_usuario_seleccionado:
                nuevo_estado_usuarios.append(f"{id_usuario},{nombre},{rol}")
            else:
                nuevo_estado_usuarios.append(linea)

        with open('usuarios.txt', 'w') as archivo:
            archivo.write('\n'.join(nuevo_estado_usuarios) + '\n')

        QMessageBox.information(self, "Usuario Editado", f"El usuario con ID '{id_usuario_seleccionado}' ha sido actualizado.")
        self.consultar_usuarios()

    def actualizar_combo_usuarios(self):
        usuarios = leer_archivo('usuarios.txt')
        self.selct_usrID_comboBx.clear()
        for linea in usuarios:
            id_usuario, _, _ = linea.split(',')
            self.selct_usrID_comboBx.addItem(id_usuario)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~@
    # Funciones para Gestión de Préstamos
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~@
    def registrar_prestamo(self):
        isbn = self.Reg_libPrestamo_comboBox.currentText()
        usuario = self.Reg_usrPrestamo_LEdit.text()
        fecha_prestamo = QDateTime.currentDateTime().toString("yyyy-MM-dd HH:mm:ss")

        if not isbn or not usuario:
            QMessageBox.warning(self, "Error", "Completa todos los campos para registrar el préstamo.")
            return

        # Actualizar estado del libro a "No Disponible"
        libros = leer_archivo('libros.txt')
        nuevo_estado_libros = []
        for linea in libros:
            isbn_actual, titulo, autor, estado = linea.split(',')
            if isbn_actual == isbn:
                nuevo_estado_libros.append(f"{isbn_actual},{titulo},{autor},No Disponible")
            else:
                nuevo_estado_libros.append(linea)

        with open('libros.txt', 'w') as archivo:
            archivo.write('\n'.join(nuevo_estado_libros) + '\n')

        # Registrar el préstamo en el historial
        registro = f"Préstamo - ISBN: {isbn}, Usuario: {usuario}, Fecha: {fecha_prestamo}"
        guardar_en_archivo('historial_prestamos.txt', registro)

        QMessageBox.information(self, "Préstamo Registrado", f"El préstamo del libro con ISBN '{isbn}' ha sido registrado.")
        self.actualizar_combo_libros_prestamo()
        self.consultar_historial()

    def registrar_devolucion(self):
        isbn = self.Reg_libDevolucion_comboBox.currentText()
        fecha_devolucion = QDateTime.currentDateTime().toString("yyyy-MM-dd HH:mm:ss")

        if not isbn:
            QMessageBox.warning(self, "Error", "Selecciona un libro para registrar la devolución.")
            return

        # Actualizar estado del libro a "Disponible"
        libros = leer_archivo('libros.txt')
        nuevo_estado_libros = []
        for linea in libros:
            isbn_actual, titulo, autor, estado = linea.split(',')
            if isbn_actual == isbn:
                nuevo_estado_libros.append(f"{isbn_actual},{titulo},{autor},Disponible")
            else:
                nuevo_estado_libros.append(linea)

        with open('libros.txt', 'w') as archivo:
            archivo.write('\n'.join(nuevo_estado_libros) + '\n')

        # Registrar la devolución en el historial
        registro = f"Devolución - ISBN: {isbn}, Fecha: {fecha_devolucion}"
        guardar_en_archivo('historial_prestamos.txt', registro)

        QMessageBox.information(self, "Devolución Registrada", f"La devolución del libro con ISBN '{isbn}' ha sido registrada.")
        self.actualizar_combo_libros_prestamo()
        self.consultar_historial()

    def consultar_historial(self):
        historial = leer_archivo('historial_prestamos.txt')
        self.listPrestamos.clear()
        for registro in historial:
            self.listPrestamos.addItem(registro)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~@
    # Funciones de Inicialización de ComboBox
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~@
    def actualizar_combo_isbn(self):
        libros = leer_archivo('libros.txt')
        self.selct_isbn_comboBx.clear()
        for linea in libros:
            isbn, _, _, _ = linea.split(',')
            self.selct_isbn_comboBx.addItem(isbn)

    def actualizar_combo_usuarios(self):
        usuarios = leer_archivo('usuarios.txt')
        self.selct_usrID_comboBx.clear()
        for linea in usuarios:
            id_usuario, _, _ = linea.split(',')
            self.selct_usrID_comboBx.addItem(id_usuario)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~@
    # Funciones de Cerrar Sesion
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~@
    def salir(self):
        self.close()  # Cerrar la ventana principal (Ventana principal)
        self.login_window.show()  # Mostrar la ventana de login
    def regresar_a_login(self):
        self.login_window.show()  # Asegurarse de mostrar la ventana de login
        self.close()  # Cerrar la ventana actual (Ventana principal)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~@
# Mostrar Ventana
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~@
def main():
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
