# Form implementation generated from reading ui file 'Designer/Ventana_Login.ui'
#
# Created by: PyQt6 UI code generator 6.8.0.dev2410141303
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(310, 425)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 190, 35, 10))
        self.label_2.setStyleSheet("background-color: rgba(0, 0, 0, 0%);\n"
"border:None;")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(70, 210, 151, 20))
        self.lineEdit.setStyleSheet("border-radius: 10px;\n"
"")
        self.lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 240, 35, 10))
        self.label_3.setStyleSheet("background-color: rgba(0, 0, 0, 0%);\n"
"border:None;")
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 260, 151, 20))
        self.lineEdit_2.setStyleSheet("border-radius: 10px;\n"
"")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(115, 296, 61, 21))
        self.pushButton.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1.5px solid #dcdcdc\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_Salir = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_Salir.setGeometry(QtCore.QRect(120, 350, 56, 17))
        self.pushButton_Salir.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1.5px solid #dcdcdc;\n"
"")
        self.pushButton_Salir.setObjectName("pushButton_Salir")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 241, 131))
        self.label.setStyleSheet("background-color: rgb(0,0,0,0%);\n"
"border-radius: 10px;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Designer/../assets/Biblioteca_fondo_Editada.jpg"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Usuario"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Ingrese Usuario"))
        self.label_3.setText(_translate("MainWindow", "ID"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Ingrese ID"))
        self.pushButton.setText(_translate("MainWindow", "Aceptar"))
        self.pushButton_Salir.setText(_translate("MainWindow", "Salir"))
