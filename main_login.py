import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6 import QtCore, QtGui, QtWidgets
from window_Login import Ui_MainWindow as Ui_login

# Función externa para leer archivo de usuarios
def leer_usuarios():
    usuarios = []
    try:
        with open('usuarios.txt', 'r') as archivo:
            for linea in archivo:
                user_id, nombre, rol = linea.strip().split(',')
                usuario = Usuario(user_id, nombre, rol)  # Asumiendo que existe una clase Usuario
                usuarios.append(usuario)
    except FileNotFoundError:
        QMessageBox.information(None, "Error: El archivo de usuarios no existe.")
    return usuarios


class LoginWindow(QMainWindow, Ui_login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.lineEdit_2.setEchoMode(self.lineEdit_2.EchoMode.Password)  # Hacer que la contraseña no sea visible
        self.pushButton.clicked.connect(self.LOGIN)  # Conectar el botón de login con la función LOGIN
        self.pushButton_Salir.clicked.connect(self.salir)  # Conectar el botón de salir con la función salir
        
        self.Enviar = None  # Esta es la instancia de la ventana principal (Ventana)

    def LOGIN(self):
        nombre = self.lineEdit.text()  # Obtener el nombre del usuario
        user_id = self.lineEdit_2.text()  # Obtener la contraseña (user_id)

        # Verificar credenciales de administrador
        if nombre == "admin" and user_id == "123456":
            from main import Ventana  # Importar Ventana solo cuando sea necesario
            if self.Enviar is None:
                self.Enviar = Ventana()  # Crear la instancia de la ventana principal
                self.Enviar.show()  # Mostrar la ventana principal
                self.close()  # Cerrar la ventana de Login
            return

        # Verificar usuarios registrados
        usuarios = leer_usuarios()
        usuario_valido = None
        for usuario in usuarios:
            if usuario.user_id == user_id and usuario.nombre == nombre:
                usuario_valido = usuario
                break
            
        if usuario_valido:
            self.configurar_rol(usuario_valido.rol)  # Configurar el rol del usuario
            from main import Ventana  # Importar Ventana solo cuando sea necesario
            if self.Enviar is None:
                self.Enviar = Ventana()  # Crear la instancia de la ventana principal
                self.Enviar.show()  # Mostrar la ventana principal
                self.close()  # Cerrar la ventana de Login
        else:
            QMessageBox.information(self, "Error: Usuario no válido.")  # Si las credenciales son incorrectas

    # Habilitar/Deshabilitar tabs para tipo de Usuario
    def configurar_rol(self, rol): 
        if rol == "Lector": 
            self.tabHistor.setEnabled(False) 
            self.tabLibros.setEnabled(False) 
            self.tabUser.setEnabled(False) 
            self.tabPrest.setEnabled(False) 
        elif rol == "Bibliotecario": 
            self.tabHistor.setEnabled(True) 
            self.tabLibros.setEnabled(True) 
            self.tabUser.setEnabled(True) 
            self.tabPrest.setEnabled(True) 
        else: 
            pass

    def salir(self):
        sys.exit()  # Salir de la aplicación


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()  # Mostrar la ventana de login
    sys.exit(app.exec())  # Ejecutar la aplicación

