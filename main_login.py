import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from Ventana_Login import Ui_MainWindow as Ui_login

class LoginWindow(QMainWindow, Ui_login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        
        self.pushButton.clicked.connect(self.LOGIN)
        self.pushButton_Salir.clicked.connect(self.salir)
        
        self.Enviar = None

    def LOGIN(self):
        username = self.user_edit.text()  
        password = self.paswr_edit.text()  
        
        if username == "admin" and password == "123456":
            if self.Enviar is None: #Aun no funciona por los usuarios
                self.Enviar = Ventana
            self.Enviar.show()
            self.close()
            self.close()  

    def salir(self):
        sys.exit() 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
