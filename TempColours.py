# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TempColours.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UI(object):
    def setupUi(self, UI):
        UI.setObjectName("UI")
        UI.resize(637, 483)
        self.centralwidget = QtWidgets.QWidget(UI)
        self.centralwidget.setObjectName("centralwidget")
        self.tempSlider = QtWidgets.QSlider(self.centralwidget)
        self.tempSlider.setGeometry(QtCore.QRect(550, 10, 41, 411))
        self.tempSlider.setOrientation(QtCore.Qt.Vertical)
        self.tempSlider.setObjectName("tempSlider")
        self.colourBackground = QtWidgets.QTextEdit(self.centralwidget)
        self.colourBackground.setGeometry(QtCore.QRect(10, 10, 510, 411))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0,0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.colourBackground.setPalette(palette)
        self.colourBackground.setObjectName("colourBackground")
        UI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(UI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 637, 26))
        self.menubar.setObjectName("menubar")
        UI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(UI)
        self.statusbar.setObjectName("statusbar")
        UI.setStatusBar(self.statusbar)
        self.tempSlider.valueChanged[int].connect(self.colourChange)

        self.retranslateUi(UI)
        QtCore.QMetaObject.connectSlotsByName(UI)

    def retranslateUi(self, UI):
        _translate = QtCore.QCoreApplication.translate
        UI.setWindowTitle(_translate("UI", "MainWindow"))
    def colourChange(self, value):
        temp = (value/2)
        red = -(((temp-50)**2.0)/2.45098039)+255.0
        green = -(((temp-25.0)**2.0)/2.45098039)+255.0
        blue = -(((temp)**2.0)/2.45098039)+255.0
        red *= (red>0)
        green *= (green>0)
        blue *= (blue>0)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(int(red), int(green), int(blue)))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        self.colourBackground.setPalette(palette)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UI = QtWidgets.QMainWindow()
    ui = Ui_UI()
    ui.setupUi(UI)
    UI.show()
    sys.exit(app.exec_())
