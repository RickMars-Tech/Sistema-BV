import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import QtCore, QtGui, QtWidgets
from Ventana_Login import Ui_MainWindow as Ui_login
from main import Ventana

#Funcion externa para leer archivo de usuarios
def leer_usuarios():
    usuarios = []
    try:
        with open('usuarios.txt', 'r') as archivo:
            for linea in archivo:
                user_id, nombre, rol = linea.strip().split(',')
                usuario = usuario(user_id, nombre, rol)
                usuarios.append(usuario)
    except FileNotFoundError:
        print("Error: El archivo de usuarios no existe.")
    return usuarios


class LoginWindow(QMainWindow, Ui_login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pushButton.clicked.connect(self.LOGIN)
        self.pushButton_Salir.clicked.connect(self.salir)
        
        self.Enviar = None

    def LOGIN(self):
        nombre = self.lineEdit.text()
        user_id = self.lineEdit_2.text()
        usuarios = leer_usuarios()
        
        usuario_valido = None
        #Inicio de sesion
        for usuario in usuarios:
            if usuario.user_id == user_id and usuario.nombre == nombre:
                usuario_valido = usuario
                break
            
        if usuario_valido:
            self.Configurar_rol(usuario_valido.rol)
            if self.Enviar is None:
                self.Enviar = Ventana()
                self.Enviar.show()
        else:
            print("Usuario no valido")
        
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

    def salir(self):
        sys.exit() 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
