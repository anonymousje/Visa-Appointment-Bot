
from PyQt6 import QtCore, QtGui, QtWidgets
import subprocess
import os
import sys

def resource_path(relative_path):
    
    base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class Ui_BLS(object):
    def setupUi(self, BLS):
        BLS.setObjectName("BLS")
        BLS.resize(800, 600)
        self.lineEdit = QtWidgets.QLineEdit(parent=BLS)
        self.lineEdit.setGeometry(QtCore.QRect(170, 170, 281, 26))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(parent=BLS)
        self.label.setGeometry(QtCore.QRect(110, 180, 66, 18))
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(parent=BLS)
        self.pushButton.setGeometry(QtCore.QRect(430, 300, 87, 26))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(BLS)
        QtCore.QMetaObject.connectSlotsByName(BLS)

        self.pushButton.clicked.connect(self.run_script)

    def run_script(self):
    
        while(1):

            argument = self.lineEdit.text()
            print("📄 [INFO] Accepted URL:", argument)
            main_script = resource_path('main.exe')
            
            if os.path.isfile(main_script):
                print("📄 [INFO] Driver Found In: ", main_script)
                print("📄 [INFO] Arguments:", [main_script, argument])
                subprocess.run([main_script, argument])
                print("💀 Exiting.")
            else:
                print("❌ [ERROR] Driver Does Not Exist! Path:", main_script)
                input("Press any key to exit...")
                exit()

    def retranslateUi(self, BLS):
        _translate = QtCore.QCoreApplication.translate
        BLS.setWindowTitle(_translate("BLS", "BLS"))
        self.label.setText(_translate("BLS", "Link"))
        self.pushButton.setText(_translate("BLS", "Start"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BLS = QtWidgets.QWidget()
    ui = Ui_BLS()
    ui.setupUi(BLS)
    BLS.show()
    sys.exit(app.exec())