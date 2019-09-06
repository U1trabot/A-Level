# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tictack.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

pb2 = ""
pb3 = ""
pb4 = ""
pb5 = ""
pb6 = ""
pb7 = ""
pb8 = ""
pb9 = ""
pb10 = ""

turns = "X"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(224, 325)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 10, 60, 60))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 10, 60, 60))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(150, 10, 60, 60))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 80, 60, 60))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(80, 80, 60, 60))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(150, 80, 60, 60))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 150, 60, 60))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(80, 150, 60, 60))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(150, 150, 60, 60))
        self.pushButton_10.setObjectName("pushButton_10")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(14, 225, 201, 41))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 224, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton_2.clicked.connect(self.turn2)
        self.pushButton_3.clicked.connect(self.turn3)
        self.pushButton_4.clicked.connect(self.turn4)
        self.pushButton_5.clicked.connect(self.turn5)
        self.pushButton_6.clicked.connect(self.turn6)
        self.pushButton_7.clicked.connect(self.turn7)
        self.pushButton_8.clicked.connect(self.turn8)
        self.pushButton_9.clicked.connect(self.turn9)
        self.pushButton_10.clicked.connect(self.turn10)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", " "))
        self.pushButton_2.setText(_translate("MainWindow", ""))
        self.pushButton_3.setText(_translate("MainWindow", ""))
        self.pushButton_4.setText(_translate("MainWindow", ""))
        self.pushButton_5.setText(_translate("MainWindow", ""))
        self.pushButton_6.setText(_translate("MainWindow", ""))
        self.pushButton_7.setText(_translate("MainWindow", ""))
        self.pushButton_8.setText(_translate("MainWindow", ""))
        self.pushButton_9.setText(_translate("MainWindow", ""))
        self.pushButton_10.setText(_translate("MainWindow", ""))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.pushButton_2.setFont(font)
        self.pushButton_3.setFont(font)
        self.pushButton_4.setFont(font)
        self.pushButton_5.setFont(font)
        self.pushButton_6.setFont(font)
        self.pushButton_7.setFont(font)
        self.pushButton_8.setFont(font)
        self.pushButton_9.setFont(font)
        self.pushButton_10.setFont(font)
        self.label.setText(_translate("MainWindow", "X - Turn"))
    def turn2(self):
        global turns
        global pb2
        global pb3
        global pb4
        global pb5
        global pb6
        global pb7
        global pb8
        global pb9
        global pb10
        if turns == "X":
            self.pushButton_2.setText(turns)
            self.pushButton_2.setDisabled(True)
            pb2 = "X"
            turns = "O"
            self.label.setText("O - Turn")
        elif turns == "O":
            self.pushButton_2.setText(turns)
            self.pushButton_2.setDisabled(True)
            pb2 = "O"
            turns = "X"
            self.label.setText("X - Turn")
        if pb2 == "X" and pb3 == ("X") and pb4 == ("X"):
            self.label.setText("X wins")
        elif pb2 == "O" and pb3 == ("O") and pb4 == ("O"):
            self.label.setText("O wins")
        elif pb2 == "X" and pb5 == "X" and pb8 == "X":
            self.label.setText("X Wins")
        elif pb2 == "O" and pb5 == "O" and pb8 == "O":
            self.label.setText("O Wins")
        elif pb8 == "X" and pb9 == "X" and pb10 == "X":
            self.label.setText("X Wins")
        elif pb8 == "O" and pb9 == "O" and pb10 == "O":
            self.label.setText("O Wins")
        elif pb10 == "X" and pb7 == "X" and pb4 == "X":
            self.label.setText("X Wins")
        elif pb10 == "O" and pb7 == "O" and pb4 == "O":
            self.label.setText("O Wins")
        elif pb2 == "X" and pb6 == "X" and pb10 == "X":
            self.label.setText("X Wins")
        elif pb2 == "O" and pb6 == "O" and pb10 == "O":
            self.label.setText("O Wins")
        elif pb4 == "X" and pb6 == "X" and pb8 == "X":
            self.label.setText("X Wins")
        elif pb4 == "O" and pb6 == "O" and pb8 == "O":
            self.label.setText("O Wins")
        elif pb3 == "X" and pb6 == "X" and pb9 == "X":
            self.label.setText("X Wins")
        elif pb3 == "O" and pb6 == "O" and pb9 == "O":
            self.label.setText("O Wins")
        elif pb5 == "X" and pb6 == "X" and pb7 == "X":
            self.label.setText("X Wins")
        elif pb5 == "O" and pb6 == "O" and pb7 == "O":
            self.label.setText("O Wins")
    def turn3(self):
        global turns
        global pb2
        global pb3
        global pb4
        global pb5
        global pb6
        global pb7
        global pb8
        global pb9
        global pb10
        if turns == "X":
            self.pushButton_3.setText(turns)
            self.pushButton_3.setDisabled(True)
            pb3 = "X"
            turns = "O"
            self.label.setText("O - Turn")
        elif turns == "O":
            self.pushButton_3.setText(turns)
            self.pushButton_3.setDisabled(True)
            pb3 = "O"
            turns = "X"
            self.label.setText("X - Turn")
        if pb2 == "X" and pb3 == ("X") and pb4 == ("X"):
            self.label.setText("X wins")
        elif pb2 == "O" and pb3 == ("O") and pb4 == ("O"):
            self.label.setText("O wins")
        elif pb2 == "X" and pb5 == "X" and pb8 == "X":
            self.label.setText("X Wins")
        elif pb2 == "O" and pb5 == "O" and pb8 == "O":
            self.label.setText("O Wins")
        elif pb8 == "X" and pb9 == "X" and pb10 == "X":
            self.label.setText("X Wins")
        elif pb8 == "O" and pb9 == "O" and pb10 == "O":
            self.label.setText("O Wins")
        elif pb10 == "X" and pb7 == "X" and pb4 == "X":
            self.label.setText("X Wins")
        elif pb10 == "O" and pb7 == "O" and pb4 == "O":
            self.label.setText("O Wins")
        elif pb2 == "X" and pb6 == "X" and pb10 == "X":
            self.label.setText("X Wins")
        elif pb2 == "O" and pb6 == "O" and pb10 == "O":
            self.label.setText("O Wins")
        elif pb4 == "X" and pb6 == "X" and pb8 == "X":
            self.label.setText("X Wins")
        elif pb4 == "O" and pb6 == "O" and pb8 == "O":
            self.label.setText("O Wins")
        elif pb3 == "X" and pb6 == "X" and pb9 == "X":
            self.label.setText("X Wins")
        elif pb3 == "O" and pb6 == "O" and pb9 == "O":
            self.label.setText("O Wins")
        elif pb5 == "X" and pb6 == "X" and pb7 == "X":
            self.label.setText("X Wins")
        elif pb5 == "O" and pb6 == "O" and pb7 == "O":
            self.label.setText("O Wins")
    def turn4(self):
        global turns
        global pb2
        global pb3
        global pb4
        global pb5
        global pb6
        global pb7
        global pb8
        global pb9
        global pb10
        if turns == "X":
            self.pushButton_4.setText(turns)
            self.pushButton_4.setDisabled(True)
            pb4 = "X"
            turns = "O"
            self.label.setText("O - Turn")
        elif turns == "O":
            self.pushButton_4.setText(turns)
            self.pushButton_4.setDisabled(True)
            pb4 = "O"
            turns = "X"
            self.label.setText("X - Turn")
        if pb2 == "X" and pb3 == ("X") and pb4 == ("X"):
            self.label.setText("X wins")
        elif pb2 == "O" and pb3 == ("O") and pb4 == ("O"):
            self.label.setText("O wins")
        elif pb2 == "X" and pb5 == "X" and pb8 == "X":
            self.label.setText("X Wins")
        elif pb2 == "O" and pb5 == "O" and pb8 == "O":
            self.label.setText("O Wins")
        elif pb8 == "X" and pb9 == "X" and pb10 == "X":
            self.label.setText("X Wins")
        elif pb8 == "O" and pb9 == "O" and pb10 == "O":
            self.label.setText("O Wins")
        elif pb10 == "X" and pb7 == "X" and pb4 == "X":
            self.label.setText("X Wins")
        elif pb10 == "O" and pb7 == "O" and pb4 == "O":
            self.label.setText("O Wins")
        elif pb2 == "X" and pb6 == "X" and pb10 == "X":
            self.label.setText("X Wins")
        elif pb2 == "O" and pb6 == "O" and pb10 == "O":
            self.label.setText("O Wins")
        elif pb4 == "X" and pb6 == "X" and pb8 == "X":
            self.label.setText("X Wins")
        elif pb4 == "O" and pb6 == "O" and pb8 == "O":
            self.label.setText("O Wins")
        elif pb3 == "X" and pb6 == "X" and pb9 == "X":
            self.label.setText("X Wins")
        elif pb3 == "O" and pb6 == "O" and pb9 == "O":
            self.label.setText("O Wins")
        elif pb5 == "X" and pb6 == "X" and pb7 == "X":
            self.label.setText("X Wins")
        elif pb5 == "O" and pb6 == "O" and pb7 == "O":
            self.label.setText("O Wins")
    def turn5(self):
        global turns
        global pb2
        global pb3
        global pb4
        global pb5
        global pb6
        global pb7
        global pb8
        global pb9
        global pb10
        if turns == "X":
            self.pushButton_5.setText(turns)
            self.pushButton_5.setDisabled(True)
            pb5 = "X"
            turns = "O"
            self.label.setText("O - Turn")
        elif turns == "O":
            self.pushButton_5.setText(turns)
            self.pushButton_5.setDisabled(True)
            pb5 = "O"
            turns = "X"
            self.label.setText("X - Turn")
        if pb2 == "X" and pb3 == ("X") and pb4 == ("X"):
            self.label.setText("X wins")
        elif pb2 == "O" and pb3 == ("O") and pb4 == ("O"):
            self.label.setText("O wins")
        elif pb2 == "X" and pb5 == "X" and pb8 == "X":
            self.label.setText("X Wins")
        elif pb2 == "O" and pb5 == "O" and pb8 == "O":
            self.label.setText("O Wins")
        elif pb8 == "X" and pb9 == "X" and pb10 == "X":
            self.label.setText("X Wins")
        elif pb8 == "O" and pb9 == "O" and pb10 == "O":
            self.label.setText("O Wins")
        elif pb10 == "X" and pb7 == "X" and pb4 == "X":
            self.label.setText("X Wins")
        elif pb10 == "O" and pb7 == "O" and pb4 == "O":
            self.label.setText("O Wins")
        elif pb2 == "X" and pb6 == "X" and pb10 == "X":
            self.label.setText("X Wins")
        elif pb2 == "O" and pb6 == "O" and pb10 == "O":
            self.label.setText("O Wins")
        elif pb4 == "X" and pb6 == "X" and pb8 == "X":
            self.label.setText("X Wins")
        elif pb4 == "O" and pb6 == "O" and pb8 == "O":
            self.label.setText("O Wins")
        elif pb3 == "X" and pb6 == "X" and pb9 == "X":
            self.label.setText("X Wins")
        elif pb3 == "O" and pb6 == "O" and pb9 == "O":
            self.label.setText("O Wins")
        elif pb5 == "X" and pb6 == "X" and pb7 == "X":
            self.label.setText("X Wins")
        elif pb5 == "O" and pb6 == "O" and pb7 == "O":
            self.label.setText("O Wins")
    def turn6(self):
        global turns
        global pb2
        global pb3
        global pb4
        global pb5
        global pb6
        global pb7
        global pb8
        global pb9
        global pb10
        if turns == "X":
            self.pushButton_6.setText(turns)
            self.pushButton_6.setDisabled(True)
            pb6 = "X"
            turns = "O"
            self.label.setText("O - Turn")
        elif turns == "O":
            self.pushButton_6.setText(turns)
            self.pushButton_6.setDisabled(True)
            pb6 = "O"
            turns = "X"
            self.label.setText("X - Turn")
        if pb2 == "X" and pb3 == ("X") and pb4 == ("X"):
            self.label.setText("X wins")
        elif pb2 == "O" and pb3 == ("O") and pb4 == ("O"):
            self.label.setText("O wins")
        elif pb2 == "X" and pb5 == "X" and pb8 == "X":
            self.label.setText("X Wins")
        elif pb2 == "O" and pb5 == "O" and pb8 == "O":
            self.label.setText("O Wins")
        elif pb8 == "X" and pb9 == "X" and pb10 == "X":
            self.label.setText("X Wins")
        elif pb8 == "O" and pb9 == "O" and pb10 == "O":
            self.label.setText("O Wins")
        elif pb10 == "X" and pb7 == "X" and pb4 == "X":
            self.label.setText("X Wins")
        elif pb10 == "O" and pb7 == "O" and pb4 == "O":
            self.label.setText("O Wins")
        elif pb2 == "X" and pb6 == "X" and pb10 == "X":
            self.label.setText("X Wins")
        elif pb2 == "O" and pb6 == "O" and pb10 == "O":
            self.label.setText("O Wins")
        elif pb4 == "X" and pb6 == "X" and pb8 == "X":
            self.label.setText("X Wins")
        elif pb4 == "O" and pb6 == "O" and pb8 == "O":
            self.label.setText("O Wins")
        elif pb3 == "X" and pb6 == "X" and pb9 == "X":
            self.label.setText("X Wins")
        elif pb3 == "O" and pb6 == "O" and pb9 == "O":
            self.label.setText("O Wins")
        elif pb5 == "X" and pb6 == "X" and pb7 == "X":
            self.label.setText("X Wins")
        elif pb5 == "O" and pb6 == "O" and pb7 == "O":
            self.label.setText("O Wins")
    def turn7(self):
        global turns
        global pb2
        global pb3
        global pb4
        global pb5
        global pb6
        global pb7
        global pb8
        global pb9
        global pb10
        if turns == "X":
            self.pushButton_7.setText(turns)
            self.pushButton_7.setDisabled(True)
            pb7 = "X"
            turns = "O"
            self.label.setText("O - Turn")
        elif turns == "O":
            self.pushButton_7.setText(turns)
            self.pushButton_7.setDisabled(True)
            pb7 = "O"
            turns = "X"
            self.label.setText("X - Turn")
        if pb2 == "X" and pb3 == ("X") and pb4 == ("X"):
            self.label.setText("X wins")
        elif pb2 == "O" and pb3 == ("O") and pb4 == ("O"):
            self.label.setText("O wins")
        elif pb2 == "X" and pb5 == "X" and pb8 == "X":
            self.label.setText("X Wins")
        elif pb2 == "O" and pb5 == "O" and pb8 == "O":
            self.label.setText("O Wins")
        elif pb8 == "X" and pb9 == "X" and pb10 == "X":
            self.label.setText("X Wins")
        elif pb8 == "O" and pb9 == "O" and pb10 == "O":
            self.label.setText("O Wins")
        elif pb10 == "X" and pb7 == "X" and pb4 == "X":
            self.label.setText("X Wins")
        elif pb10 == "O" and pb7 == "O" and pb4 == "O":
            self.label.setText("O Wins")
        elif pb2 == "X" and pb6 == "X" and pb10 == "X":
            self.label.setText("X Wins")
        elif pb2 == "O" and pb6 == "O" and pb10 == "O":
            self.label.setText("O Wins")
        elif pb4 == "X" and pb6 == "X" and pb8 == "X":
            self.label.setText("X Wins")
        elif pb4 == "O" and pb6 == "O" and pb8 == "O":
            self.label.setText("O Wins")
        elif pb3 == "X" and pb6 == "X" and pb9 == "X":
            self.label.setText("X Wins")
        elif pb3 == "O" and pb6 == "O" and pb9 == "O":
            self.label.setText("O Wins")
        elif pb5 == "X" and pb6 == "X" and pb7 == "X":
            self.label.setText("X Wins")
        elif pb5 == "O" and pb6 == "O" and pb7 == "O":
            self.label.setText("O Wins")
    def turn8(self):
        global turns
        global pb2
        global pb3
        global pb4
        global pb5
        global pb6
        global pb7
        global pb8
        global pb9
        global pb10
        if turns == "X":
            self.pushButton_8.setText(turns)
            self.pushButton_8.setDisabled(True)
            pb8 = "X"
            turns = "O"
            self.label.setText("O - Turn")
        elif turns == "O":
            self.pushButton_8.setText(turns)
            self.pushButton_8.setDisabled(True)
            pb8 = "O"
            turns = "X"
            self.label.setText("X - Turn")
        if pb2 == "X" and pb3 == ("X") and pb4 == ("X"):
            self.label.setText("X wins")
        elif pb2 == "O" and pb3 == ("O") and pb4 == ("O"):
            self.label.setText("O wins")
        elif pb2 == "X" and pb5 == "X" and pb8 == "X":
            self.label.setText("X Wins")
        elif pb2 == "O" and pb5 == "O" and pb8 == "O":
            self.label.setText("O Wins")
        elif pb8 == "X" and pb9 == "X" and pb10 == "X":
            self.label.setText("X Wins")
        elif pb8 == "O" and pb9 == "O" and pb10 == "O":
            self.label.setText("O Wins")
        elif pb10 == "X" and pb7 == "X" and pb4 == "X":
            self.label.setText("X Wins")
        elif pb10 == "O" and pb7 == "O" and pb4 == "O":
            self.label.setText("O Wins")
        elif pb2 == "X" and pb6 == "X" and pb10 == "X":
            self.label.setText("X Wins")
        elif pb2 == "O" and pb6 == "O" and pb10 == "O":
            self.label.setText("O Wins")
        elif pb4 == "X" and pb6 == "X" and pb8 == "X":
            self.label.setText("X Wins")
        elif pb4 == "O" and pb6 == "O" and pb8 == "O":
            self.label.setText("O Wins")
        elif pb3 == "X" and pb6 == "X" and pb9 == "X":
            self.label.setText("X Wins")
        elif pb3 == "O" and pb6 == "O" and pb9 == "O":
            self.label.setText("O Wins")
        elif pb5 == "X" and pb6 == "X" and pb7 == "X":
            self.label.setText("X Wins")
        elif pb5 == "O" and pb6 == "O" and pb7 == "O":
            self.label.setText("O Wins")
    def turn9(self):
        global turns
        global pb2
        global pb3
        global pb4
        global pb5
        global pb6
        global pb7
        global pb8
        global pb9
        global pb10
        if turns == "X":
            self.pushButton_9.setText(turns)
            self.pushButton_9.setDisabled(True)
            pb9 = "X"
            turns = "O"
            self.label.setText("O - Turn")
        elif turns == "O":
            self.pushButton_9.setText(turns)
            self.pushButton_9.setDisabled(True)
            pb9 = "O"
            turns = "X"
            self.label.setText("X - Turn")
        if pb2 == "X" and pb3 == ("X") and pb4 == ("X"):
            self.label.setText("X wins")
        elif pb2 == "O" and pb3 == ("O") and pb4 == ("O"):
            self.label.setText("O wins")
        elif pb2 == "X" and pb5 == "X" and pb8 == "X":
            self.label.setText("X Wins")
        elif pb2 == "O" and pb5 == "O" and pb8 == "O":
            self.label.setText("O Wins")
        elif pb8 == "X" and pb9 == "X" and pb10 == "X":
            self.label.setText("X Wins")
        elif pb8 == "O" and pb9 == "O" and pb10 == "O":
            self.label.setText("O Wins")
        elif pb10 == "X" and pb7 == "X" and pb4 == "X":
            self.label.setText("X Wins")
        elif pb10 == "O" and pb7 == "O" and pb4 == "O":
            self.label.setText("O Wins")
        elif pb2 == "X" and pb6 == "X" and pb10 == "X":
            self.label.setText("X Wins")
        elif pb2 == "O" and pb6 == "O" and pb10 == "O":
            self.label.setText("O Wins")
        elif pb4 == "X" and pb6 == "X" and pb8 == "X":
            self.label.setText("X Wins")
        elif pb4 == "O" and pb6 == "O" and pb8 == "O":
            self.label.setText("O Wins")
        elif pb3 == "X" and pb6 == "X" and pb9 == "X":
            self.label.setText("X Wins")
        elif pb3 == "O" and pb6 == "O" and pb9 == "O":
            self.label.setText("O Wins")
        elif pb5 == "X" and pb6 == "X" and pb7 == "X":
            self.label.setText("X Wins")
        elif pb5 == "O" and pb6 == "O" and pb7 == "O":
            self.label.setText("O Wins")
    def turn10(self):
        global turns
        global pb2
        global pb3
        global pb4
        global pb5
        global pb6
        global pb7
        global pb8
        global pb9
        global pb10
        if turns == "X":
            self.pushButton_10.setText(turns)
            self.pushButton_10.setDisabled(True)
            pb10 = "X"
            turns = "O"
            self.label.setText("O - Turn")
        elif turns == "O":
            self.pushButton_10.setText(turns)
            self.pushButton_10.setDisabled(True)
            pb10 = "O"
            turns = "X"
            self.label.setText("X - Turn")
        if pb2 == "X" and pb3 == ("X") and pb4 == ("X"):
            self.label.setText("X wins")
        elif pb2 == "O" and pb3 == ("O") and pb4 == ("O"):
            self.label.setText("O wins")
        elif pb2 == "X" and pb5 == "X" and pb8 == "X":
            self.label.setText("X Wins")
        elif pb2 == "O" and pb5 == "O" and pb8 == "O":
            self.label.setText("O Wins")
        elif pb8 == "X" and pb9 == "X" and pb10 == "X":
            self.label.setText("X Wins")
        elif pb8 == "O" and pb9 == "O" and pb10 == "O":
            self.label.setText("O Wins")
        elif pb10 == "X" and pb7 == "X" and pb4 == "X":
            self.label.setText("X Wins")
        elif pb10 == "O" and pb7 == "O" and pb4 == "O":
            self.label.setText("O Wins")
        elif pb2 == "X" and pb6 == "X" and pb10 == "X":
            self.label.setText("X Wins")
        elif pb2 == "O" and pb6 == "O" and pb10 == "O":
            self.label.setText("O Wins")
        elif pb4 == "X" and pb6 == "X" and pb8 == "X":
            self.label.setText("X Wins")
        elif pb4 == "O" and pb6 == "O" and pb8 == "O":
            self.label.setText("O Wins")
        elif pb3 == "X" and pb6 == "X" and pb9 == "X":
            self.label.setText("X Wins")
        elif pb3 == "O" and pb6 == "O" and pb9 == "O":
            self.label.setText("O Wins")
        elif pb5 == "X" and pb6 == "X" and pb7 == "X":
            self.label.setText("X Wins")
        elif pb5 == "O" and pb6 == "O" and pb7 == "O":
            self.label.setText("O Wins")
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
