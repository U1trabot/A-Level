#Number Wording Quiz (GUI Version)
#Adam Baker

from PyQt5 import QtCore, QtGui, QtWidgets
import random, tools, os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow): #Sets The GUI Up And Sets How It Looks
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(531, 269)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 541, 271))
        self.tabWidget.setObjectName("tabWidget")
        self.Tests = QtWidgets.QWidget()
        self.Tests.setObjectName("Tests")
        self.ScoreNumber = QtWidgets.QLabel(self.Tests)
        self.ScoreNumber.setGeometry(QtCore.QRect(440, 20, 65, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(20)
        self.ScoreNumber.setFont(font)
        self.ScoreNumber.setObjectName("ScoreNumber")
        self.ScoreText = QtWidgets.QLabel(self.Tests)
        self.ScoreText.setGeometry(QtCore.QRect(350, 20, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(20)
        self.ScoreText.setFont(font)
        self.ScoreText.setObjectName("ScoreText")
        self.lineEdit = QtWidgets.QLineEdit(self.Tests)
        self.lineEdit.setGeometry(QtCore.QRect(40, 130, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.returnPressed.connect(self.answer) #Makes Enter Key Submit Answers
        self.questionLabel = QtWidgets.QLabel(self.Tests)
        self.questionLabel.setGeometry(QtCore.QRect(30, 0, 281, 121))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(16)
        self.questionLabel.setFont(font)
        self.questionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.questionLabel.setObjectName("questionLabel")
        self.questionLabel.setWordWrap(True) #Allows Text To Down When It Reaches The Edge Of It's Box
        self.pushButton = QtWidgets.QPushButton(self.Tests)
        self.pushButton.setGeometry(QtCore.QRect(350, 130, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor)) #Makes Button Change Cursor On Hover
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setAutoDefault(True)
        self.pushButton_3 = QtWidgets.QPushButton(self.Tests)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 130, 281, 41))
        self.pushButton_3.setAutoDefault(True)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(236, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 105, 105))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 52, 52))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 105, 105))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 52, 52))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 105, 105))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 52, 52))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.pushButton_3.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setAutoFillBackground(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.tabWidget.addTab(self.Tests, "")
        self.Login = QtWidgets.QWidget()
        self.Login.setObjectName("Login")
        self.pushButton_2 = QtWidgets.QPushButton(self.Login)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 120, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor)) #Makes Button Change Cursor On Hover
        self.lineEdit_2 = QtWidgets.QLineEdit(self.Login)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 120, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.returnPressed.connect(self.loginSubmit) #Makes Enter Submit Login
        self.label = QtWidgets.QLabel(self.Login)
        self.label.setGeometry(QtCore.QRect(40, 40, 421, 71))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("text.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.Login, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton_2.clicked.connect(self.loginSubmit) #Makes the buttons call functions
        self.pushButton_3.clicked.connect(self.loginForce)
        self.pushButton.clicked.connect(self.answer)
        self.pushButton.setEnabled(False)
    def retranslateUi(self, MainWindow): #Makes The Text Translatable, Sets The Defaut Text
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Number Test"))
        self.ScoreNumber.setText(_translate("MainWindow", "0"))
        self.ScoreText.setText(_translate("MainWindow", "Score:"))
        self.questionLabel.setText(_translate("MainWindow", ""))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.pushButton_3.setText(_translate("MainWindow", "Please Login"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tests), _translate("MainWindow", "Tests"))
        self.pushButton_2.setText(_translate("MainWindow", "Submit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Login), _translate("MainWindow", "Login"))
    def loginSubmit(self): #Handles The Login And Starts The Program
        global username
        global wins
        global correct
        global incorrect
        global words
        global repeat
        wins = 0
        repeat = 0
        username = self.lineEdit_2.text()
        self.lineEdit_2.clear()
        self.pushButton_3.hide()
        self.pushButton.setEnabled(True) #Allows The User To Submit Answers Now That They Are Logged In
        try:
            os.mkdir(username)
        except:
            pass
        file = open(username+'/'+"ca.pak" ,"a") #Creates ca.pak file if it doesn't already exist
        file.close()

        correct = list() #Grabs all data from ca.pak and puts it in list variable
        file = open(username+'/'+"ca.pak", "r")
        line = file.readline()
        correct = line.split(',')
        file.close()
        correct.remove('')
        try:
            incorrect = list() #Grabs all data from ia.pak and puts it in list variable
            file = open(username+'/'+"ia.pak", "r")
            line = file.readline()
            incorrect = line.split(',')
            incorrect.remove('')
        except:
            pass
        file.close()
        self.questGen()
    def questGen(self):
        global username
        global wins
        global digits
        global correct
        global incorrect
        global words
        if len(incorrect) == (0): #Checks if there are any questions that where answered incorrectly
            digits = random.randint(0,9999) #picks a random number smaller than 10,000 and larger than -1
        elif len(incorrect) > (0):
            digits = int(random.choice(incorrect)) #Will get the user a question they got wrong before until they get it right
            incorrect.remove(str(digits)) #Removes given question from the file/list
            os.remove(username+'/'+'ia.pak')
            file = open(username+'/'+"ia.pak","a")
            for item in incorrect:
                    file.write(item+',')
            file.close
        for item in correct: #Checks if number has been correct before
            if int(item) == digits:
                self.questGen() #Gets a new number
            else:
                break #Continues the question generation
        words = self.convert(digits) #Converts Number to Words
        self.questionLabel.setText(words)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.setTabEnabled(1,False)
    def loginForce(self):
            self.tabWidget.setCurrentIndex(1)
    def convert(self,number):
        tenNeeded = False #Varible used to find out if teen/eleven type numbers should be used
        strNumber = str(number) #converts number to string
        length = len(strNumber) #finds out how many digits in the number
        output = list() #creates empty list to be filled with the words
        if length == (4): #If the number is 4 digits long, it will start at the thousands and go down
            if strNumber[0] == ("1"): #Will check every digit for a number then put relevant word in the output list
                output.append("one thousand")
            elif strNumber[0] == ("2"):
                output.append("two thousand")
            elif strNumber[0] == ("3"):
                output.append("three thousand")
            elif strNumber[0] == ("4"):
                output.append("four thousand")
            elif strNumber[0] == ("5"):
                output.append("five thousand")
            elif strNumber[0] == ("6"):
                output.append("six thousand")
            elif strNumber[0] == ("7"):
                output.append("seven thousand")
            elif strNumber[0] == ("8"):
                output.append("eight thousand")
            elif strNumber[0] == ("9"):
                output.append("nine thousand")
            if strNumber[1] != ('0'):
                output.append(",") #If more numbers are to come, a comma is added
            if strNumber[1] == ("1"):
                output.append("one hundred")
            elif strNumber[1] == ("2"):
                output.append("two hundred")
            elif strNumber[1] == ("3"):
                output.append("three hundred")
            elif strNumber[1] == ("4"):
                output.append("four hundred")
            elif strNumber[1] == ("5"):
                output.append("five hundred")
            elif strNumber[1] == ("6"):
                output.append("six hundred")
            elif strNumber[1] == ("7"):
                output.append("seven hundred")
            elif strNumber[1] == ("8"):
                output.append("eight hundred")
            elif strNumber[1] == ("9"):
                output.append("nine hundred")
            if strNumber[2] != ('0') or strNumber[3] != ('0'): #If more numbers are to come, an 'and' is added
                output.append("and")
            if strNumber[2] == ("1"):
                tenNeeded = True #Tells the system a ten will be needed
            elif strNumber[2] == ("2"):
                output.append("twenty")
            elif strNumber[2] == ("3"):
                output.append("thirty")
            elif strNumber[2] == ("4"):
                output.append("fourty")
            elif strNumber[2] == ("5"):
                output.append("fifty")
            elif strNumber[2] == ("6"):
                output.append("sixty")
            elif strNumber[2] == ("7"):
                output.append("seventy")
            elif strNumber[2] == ("8"):
                output.append("eighty")
            elif strNumber[2] == ("9"):
                output.append("ninety")
            if strNumber[3] == ("1"):
                if tenNeeded: #Changes to eleven if a ten is needed
                    output.append("eleven")
                else:
                    output.append("one")
            elif strNumber[3] == ("2"):
                if tenNeeded: #Changes to twelve if a ten is needed ect.
                    output.append("twelve")
                else:
                    output.append("two")
            elif strNumber[3] == ("3"):
                if tenNeeded:
                    output.append("thirteen")
                else:
                    output.append("three")
            elif strNumber[3] == ("4"):
                if tenNeeded:
                    output.append("fourteen")
                else:
                    output.append("four")
            elif strNumber[3] == ("5"):
                if tenNeeded:
                    output.append("fifteen")
                else:
                    output.append("five")
            elif strNumber[3] == ("6"):
                if tenNeeded:
                    output.append("sixteen")
                else:
                    output.append("six")
            elif strNumber[3] == ("7"):
                if tenNeeded:
                    output.append("seventeen")
                else:
                    output.append("seven")
            elif strNumber[3] == ("8"):
                if tenNeeded:
                    output.append("eighteen")
                else:
                    output.append("eight")
            elif strNumber[3] == ("9"):
                if tenNeeded:
                    output.append("nineteen")
                else:
                    output.append("nine")
            elif strNumber[3] == ("0"):
                if tenNeeded:
                    output.append("ten") #Adds a ten if a ten is needed
        elif length == (3): #If the number is 3 digits long, it will start at the hundreds and go down
            if strNumber[0] == ("1"): #Will check every digit for a number then put relevant word in the output list
                output.append("one hundred")
            elif strNumber[0] == ("2"):
                output.append("two hundred")
            elif strNumber[0] == ("3"):
                output.append("three hundred")
            elif strNumber[0] == ("4"):
                output.append("four hundred")
            elif strNumber[0] == ("5"):
                output.append("five hundred")
            elif strNumber[0] == ("6"):
                output.append("six hundred")
            elif strNumber[0] == ("7"):
                output.append("seven hundred")
            elif strNumber[0] == ("8"):
                output.append("eight hundred")
            elif strNumber[0] == ("9"):
                output.append("nine hundred")
            if strNumber[1] != ('0') or strNumber[2] != ('0'): #If more numbers are to come, an 'and' is added
                output.append("and")
            if strNumber[1] == ("1"):
                tenNeeded = True
            elif strNumber[1] == ("2"):
                output.append("twenty")
            elif strNumber[1] == ("3"):
                output.append("thirty")
            elif strNumber[1] == ("4"):
                output.append("fourty")
            elif strNumber[1] == ("5"):
                output.append("fifty")
            elif strNumber[1] == ("6"):
                output.append("sixty")
            elif strNumber[1] == ("7"):
                output.append("seventy")
            elif strNumber[1] == ("8"):
                output.append("eighty")
            elif strNumber[1] == ("9"):
                output.append("ninety")
            if strNumber[2] == ("1"):
                if tenNeeded:
                    output.append("eleven")
                else:
                    output.append("one")
            elif strNumber[2] == ("2"):
                if tenNeeded:
                    output.append("twelve")
                else:
                    output.append("two")
            elif strNumber[2] == ("3"):
                if tenNeeded:
                    output.append("thirteen")
                else:
                    output.append("three")
            elif strNumber[2] == ("4"):
                if tenNeeded:
                    output.append("fourteen")
                else:
                    output.append("four")
            elif strNumber[2] == ("5"):
                if tenNeeded:
                    output.append("fifteen")
                else:
                    output.append("five")
            elif strNumber[2] == ("6"):
                if tenNeeded:
                    output.append("sixteen")
                else:
                    output.append("six")
            elif strNumber[2] == ("7"):
                if tenNeeded:
                    output.append("seventeen")
                else:
                    output.append("seven")
            elif strNumber[2] == ("8"):
                if tenNeeded:
                    output.append("eighteen")
                else:
                    output.append("eight")
            elif strNumber[2] == ("9"):
                if tenNeeded:
                    output.append("nineteen")
                else:
                    output.append("nine")
            elif strNumber[2] == ("0"):
                if tenNeeded:
                    output.append("ten")
        elif length == (2): #If the number is 2 digits long, it will start at the tens and go down
            if strNumber[0] == ("1"): #Will check every digit for a number then put relevant word in the output list
                tenNeeded = True
            elif strNumber[0] == ("2"):
                output.append("twenty")
            elif strNumber[0] == ("3"):
                output.append("thirty")
            elif strNumber[0] == ("4"):
                output.append("fourty")
            elif strNumber[0] == ("5"):
                output.append("fifty")
            elif strNumber[0] == ("6"):
                output.append("sixty")
            elif strNumber[0] == ("7"):
                output.append("seventy")
            elif strNumber[0] == ("8"):
                output.append("eighty")
            elif strNumber[0] == ("9"):
                output.append("ninety")
            if strNumber[1] == ("1"):
                if tenNeeded:
                    output.append("eleven")
                else:
                    output.append("one")
            elif strNumber[1] == ("2"):
                if tenNeeded:
                    output.append("twelve")
                else:
                    output.append("two")
            elif strNumber[1] == ("3"):
                if tenNeeded:
                    output.append("thirteen")
                else:
                    output.append("three")
            elif strNumber[1] == ("4"):
                if tenNeeded:
                    output.append("fourteen")
                else:
                    output.append("four")
            elif strNumber[1] == ("5"):
                if tenNeeded:
                    output.append("fifteen")
                else:
                    output.append("five")
            elif strNumber[1] == ("6"):
                if tenNeeded:
                    output.append("sixteen")
                else:
                    output.append("six")
            elif strNumber[1] == ("7"):
                if tenNeeded:
                    output.append("seventeen")
                else:
                    output.append("seven")
            elif strNumber[1] == ("8"):
                if tenNeeded:
                    output.append("eighteen")
                else:
                    output.append("eight")
            elif strNumber[1] == ("9"):
                if tenNeeded:
                    output.append("nineteen")
                else:
                    output.append("nine")
            elif strNumber[1] == ("0"):
                if tenNeeded:
                    output.append("ten")
        elif length == (1): #If the number is 1 digit long, it will start at the digits and go down
            if strNumber[0] == ("1"): #Will check every digit for a number then put relevant word in the output list
                if tenNeeded:
                    output.append("eleven")
                else:
                    output.append("one")
            elif strNumber[0] == ("2"):
                if tenNeeded:
                    output.append("twelve")
                else:
                    output.append("two")
            elif strNumber[0] == ("3"):
                if tenNeeded:
                    output.append("thirteen")
                else:
                    output.append("three")
            elif strNumber[0] == ("4"):
                if tenNeeded:
                    output.append("fourteen")
                else:
                    output.append("four")
            elif strNumber[0] == ("5"):
                if tenNeeded:
                    output.append("fifteen")
                else:
                    output.append("five")
            elif strNumber[0] == ("6"):
                if tenNeeded:
                    output.append("sixteen")
                else:
                    output.append("six")
            elif strNumber[0] == ("7"):
                if tenNeeded:
                    output.append("seventeen")
                else:
                    output.append("seven")
            elif strNumber[0] == ("8"):
                if tenNeeded:
                    output.append("eighteen")
                else:
                    output.append("eight")
            elif strNumber[0] == ("9"):
                if tenNeeded:
                    output.append("nineteen")
                else:
                    output.append("nine")
            elif strNumber[0] == ("0"):
                if tenNeeded:
                    output.append("ten")
                else:
                    output.append("zero") #Adds a zero if 0 is the only digit
        words = ""
        run = 0
        for item in output: #System to add spaces if needed
            if run == 0:
                words = item
            elif run > 0:
                words = (words+' '+item)
            run = run + 1
        return words #Returns the number as words
    def answer(self):
        global username
        global wins
        global correct
        global incorrect
        global words
        global digits
        global repeat
        try:
            input = int(self.lineEdit.text())
        except:
            input = 0
        self.lineEdit.clear()
        if input == digits:
            palette = QtGui.QPalette()
            brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
            brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
            self.lineEdit.setPalette(palette)
            wins = wins + 1 #adds a score to the variable
            self.ScoreNumber.setText(str(wins))
            file = open(username+'/'+"ca.pak", "a") #Saves Question To ca.pak as it was answered correctly
            file.write(str(digits)+',')
            file.close()
        elif input != digits:
            palette = QtGui.QPalette()
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
            brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
            self.lineEdit.setPalette(palette)
            file = open(username+'/'+"ia.pak", "a") #Saves Question To ia.pak as it was answered incorrectly
            file.write(str(digits)+',')
            file.close()
        repeat = repeat + 1
        if repeat < 10:
            self.questGen()
        else: #System For Ending The Test
            self.questionLabel.setText('10 Questions Completed')
            self.pushButton_3.setText('Test Completed')
            self.pushButton.setEnabled(False)
            self.pushButton_3.show()
            file = open(username+'/'+"scores.pak","a")
            file.write(str(wins)+'\n')
            file.close()
            file = open(username+'/'+"StudentScores.txt","a")
            file.write(str(wins)+'\n')
            file.close()
            file = open(username+'/'+"tests.pak","a")
            file.close()
            file = open(username+'/'+"tests.pak","r")
            score = 0
            for line in file:
                score = int(line)
            score = score +1
            if score == (3): #System For Getting The Average After 3 Tests
                self.questionLabel.setText("You have completed 3 tests, here is your average score!")
                file = open(username+'/'+"scores.pak","r")
                total = 0
                for line in file:
                    total = total + int(line)
                mean = total/3
                self.ScoreNumber.setText(str(mean))
                score = 0
                file.close()
                os.remove(username+'/'+"tests.pak")
                os.remove(username+'/'+"scores.pak")
            file = open(username+'/'+"tests.pak","w+")
            file.write(str(score))
            file.close()

if __name__ == "__main__": #System for opening the GUI
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
