# Form implementation generated from reading ui file 'Interface.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import subprocess

class Ui_BLS(object):
    def setupUi(self, BLS):
        BLS.setObjectName("BLS")
        BLS.resize(800, 600)
        self.lineEdit = QtWidgets.QLineEdit(parent=BLS)
        self.lineEdit.setGeometry(QtCore.QRect(170, 170, 281, 26))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=BLS)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 210, 281, 26))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.label = QtWidgets.QLabel(parent=BLS)
        self.label.setGeometry(QtCore.QRect(110, 180, 66, 18))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=BLS)
        self.label_2.setGeometry(QtCore.QRect(90, 220, 66, 18))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(parent=BLS)
        self.pushButton.setGeometry(QtCore.QRect(430, 300, 87, 26))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(BLS)
        QtCore.QMetaObject.connectSlotsByName(BLS)

        self.pushButton.clicked.connect(self.run_script)
    def run_script(self):
        while(1):
            argument1 = self.lineEdit.text()
            argument2 = self.lineEdit_2.text()
            arguments = ["/home/anonymousje/Downloads/codes/selenium/main.py", argument1, argument2]
            subprocess.run(arguments)
            #subprocess("python", "main.py", self.lineEdit.text(), self.lineEdit_2.text())


    def retranslateUi(self, BLS):
        _translate = QtCore.QCoreApplication.translate
        BLS.setWindowTitle(_translate("BLS", "BLS"))
        self.label.setText(_translate("BLS", "Email"))
        self.label_2.setText(_translate("BLS", "Password"))
        self.pushButton.setText(_translate("BLS", "Start"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BLS = QtWidgets.QWidget()
    ui = Ui_BLS()
    ui.setupUi(BLS)
    BLS.show()
    sys.exit(app.exec())
