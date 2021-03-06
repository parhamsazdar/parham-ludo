from PyQt5 import QtCore, QtGui, QtWidgets
import sys

"""This module is contain winners Gui and all related func"""


class Winers(QtWidgets.QMainWindow, QtWidgets.QDialog):

    # par=ludo-game #par_1=dialog for closing the window
    def __init__(self, par, par_1):
        super().__init__()
        self.par = par
        self.par_1 = par_1

    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(363, 494)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(100, 260, 153, 36))
        font = QtGui.QFont()
        font.setFamily("Ravie")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 210, 152, 36))
        font = QtGui.QFont()
        font.setFamily("Ravie")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 310, 157, 36))
        font = QtGui.QFont()
        font.setFamily("Ravie")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 50, 211, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 80, 131, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(100, 160, 145, 36))
        font = QtGui.QFont()
        font.setFamily("Ravie")
        font.setPointSize(16)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(61, 381, 93, 28))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(179, 381, 93, 28))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.lbl = [self.label_1, self.label_3, self.label_5, self.label_4]


        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        self.pushButton.clicked.connect(self.reset)
        self.pushButton_2.clicked.connect(self.end)

    def reset(self):
        self.new_game_add()
        self.par.reset()
        self.par_1.close()

    def new_game_add(self):
        msg = QtWidgets.QMessageBox()
        msgBox = msg.information(self, 'New Game', 'setup NeW Game')
        if msgBox == QtWidgets.QMessageBox.Ok:
            msg.close()

    def end(self):
        sys.exit()

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Winers"))
        self.label_5.setText(_translate("mainWindow", ""))
        self.label_3.setText(_translate("mainWindow", ""))
        self.label_4.setText(_translate("mainWindow", ""))
        self.label.setText(_translate("mainWindow", "Game Finished!"))
        self.label_2.setText(_translate("mainWindow", "ranking:"))
        self.label_1.setText(_translate("mainWindow", ""))
        self.pushButton.setText(_translate("mainWindow", "New Game"))
        self.pushButton_2.setText(_translate("mainWindow", "Finish"))
