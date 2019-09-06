# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'basic.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

ran = 0
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(282, 191)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Input = QtWidgets.QLineEdit(self.centralwidget)
        self.Input.setGeometry(QtCore.QRect(30, 20, 113, 22))
        self.Input.setObjectName("Input")
        self.Output = QtWidgets.QLabel(self.centralwidget)
        self.Output.setGeometry(QtCore.QRect(20, 50, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Output.setFont(font)
        self.Output.setAlignment(QtCore.Qt.AlignCenter)
        self.Output.setWordWrap(True)
        self.Output.setObjectName("Output")
        self.Submit = QtWidgets.QPushButton(self.centralwidget)
        self.Submit.setGeometry(QtCore.QRect(160, 20, 101, 101))
        self.Submit.setObjectName("Submit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 282, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.Submit.clicked.connect(self.buttonClicked)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Caeser"))
        self.Output.setText(_translate("MainWindow", "Input the string to be cyphered"))
        self.Submit.setText(_translate("MainWindow", "Submit"))
    def buttonClicked(self):
        global ran
        global text
        global shift
        _translate = QtCore.QCoreApplication.translate
        if ran == 0:
            text = self.Input.text()
            self.Output.setText(_translate("MainWindow", "Input the number of shifts"))
            ran = ran + 1
        elif ran == 1:
            shift  = int(self.Input.text())
            def splitstr(stri):
                return list(stri)
            textList = splitstr(text)
            alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
            x = 0
            for x in range (len(textList)):
                for i in range (len(alphabet)):
                    if textList[x] == alphabet[i]:
                        textList[x] = alphabet[i+shift]
                        break
                x = 1
            output = str()
            for x in range (len(textList)):
                output = output+(textList[x])
            self.Output.setText(_translate("MainWindow",output))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())