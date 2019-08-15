# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\ultra\Documents\GitHub\A-Level\SummerAssignment\GUIFiles\loginUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_LoginMenu(object):
    def setupUi(self, LoginMenu):
        LoginMenu.setObjectName("LoginMenu")
        LoginMenu.resize(327, 132)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        LoginMenu.setFont(font)
        self.centralwidget = QtWidgets.QWidget(LoginMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.SubmitButton = QtWidgets.QPushButton(self.centralwidget)
        self.SubmitButton.setGeometry(QtCore.QRect(200, 60, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.SubmitButton.setFont(font)
        self.SubmitButton.setObjectName("SubmitButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 60, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.LoginInfo = QtWidgets.QLabel(self.centralwidget)
        self.LoginInfo.setGeometry(QtCore.QRect(10, 10, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.LoginInfo.setFont(font)
        self.LoginInfo.setObjectName("LoginInfo")
        LoginMenu.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(LoginMenu)
        self.statusbar.setObjectName("statusbar")
        LoginMenu.setStatusBar(self.statusbar)

        self.retranslateUi(LoginMenu)
        QtCore.QMetaObject.connectSlotsByName(LoginMenu)

        self.SubmitButton.clicked.connect(self.submitUsername)
    def retranslateUi(self, LoginMenu):
        _translate = QtCore.QCoreApplication.translate
        LoginMenu.setWindowTitle(_translate("LoginMenu", "Enter Username"))
        self.SubmitButton.setText(_translate("LoginMenu", "Submit"))
        self.LoginInfo.setText(_translate("LoginMenu", "Username e.g JohnSmith:"))
    def submitUsername(self):
        global username
        username = (self.lineEdit.text())
        self.lineEdit.clear()
        f = open('user.pak','a')
        f.write(username)
        f.close()
        sys.exit(app.exec_())
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginMenu = QtWidgets.QMainWindow()
    ui = Ui_LoginMenu()
    ui.setupUi(LoginMenu)
    LoginMenu.show()
    sys.exit(app.exec_())