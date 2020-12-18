from PyQt5 import QtCore, QtGui, QtWidgets
from players import Players
from PyQt5.QtWidgets import QMessageBox

"""This is login Gui"""
"""You can add player for your game in this module"""


class Login(QtWidgets.QMainWindow, QtWidgets.QDialog):
    players = []
    selected_color = []
    #par_1=ludo-game #par=dialog for closing the window
    def __init__(self, par, par_1):
        super(Login, self).__init__()
        self.par = par
        self.par_1 = par_1

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(561, 310)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_user = QtWidgets.QLabel(self.centralwidget)
        self.label_user.setGeometry(QtCore.QRect(40, 60, 89, 23))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label_user.setFont(font)
        self.label_user.setObjectName("label_user")
        self.label_password = QtWidgets.QLabel(self.centralwidget)
        self.label_password.setGeometry(QtCore.QRect(40, 110, 88, 23))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.label_color = QtWidgets.QLabel(self.centralwidget)
        self.label_color.setGeometry(QtCore.QRect(80, 150, 43, 23))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label_color.setFont(font)
        self.label_color.setObjectName("label_color")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 57, 301, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 106, 301, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(150, 155, 211, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 190, 121, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 561, 25))
        self.menubar.setObjectName("menubar")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.isvalid_player)

    def isvalid_player(self):
        """
        for checking if the user is valid or not by read info from file of user
        """
        if self.comboBox.currentText() in Login.selected_color:
            self.comboBox.removeItem(self.comboBox.currentIndex())
            self.has_taken()
        elif len(Login.players) <= 3:
            user_ = self.lineEdit.text()
            pass_ = self.lineEdit_2.text()
            color_ = self.comboBox.currentText()
            with open('users') as f:
                users = {}
                for i in f.readlines():
                    i = i.strip()
                    username, passw = i.split(',')
                    users[username] = passw

                if user_ in users and users[user_] == pass_:
                    Login.players.append(Players(f'{user_}', f'{color_}'))
                    x = self.comboBox.currentIndex()
                    self.comboBox.removeItem(x)
                    Login.selected_color.append(color_)
                    self.add()
                    self.par.close()
                else:
                    self.error_notexist()
            if len(Login.players) == 4:
                self.par_1.ui.add.setEnabled(False)

        else:
            pass
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')

    # check if that color the user selected is taken by another user or not
    def has_taken(self):
        msg = QMessageBox()
        msgBox = msg.critical(self, 'Error', 'This color is taken by another user')
        if msgBox == QMessageBox.Ok:
            msg.close()

    # max add player error dialog
    def max_error(self):
        msg = QMessageBox()
        msgBox = msg.critical(self, 'Error', 'You added 4 players')
        if msgBox == QMessageBox.Ok:
            msg.close()

    # this is not exist dialog
    def error_notexist(self):
        msg = QMessageBox()
        msgBox = msg.critical(self, 'Error', 'This user dosent exist')
        if msgBox == QMessageBox.Ok:
            msg.close()

    # DIALOG FOR adding player
    def add(self):
        msg = QMessageBox()
        msgBox = msg.information(self, 'Add player', 'The user adds succefully')
        if msgBox == QMessageBox.Ok:
            msg.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.label_user.setText(_translate("MainWindow", "Username"))
        self.label_password.setText(_translate("MainWindow", "Password"))
        self.label_color.setText(_translate("MainWindow", "color"))
        self.comboBox.setItemText(0, _translate("MainWindow", "red"))
        self.comboBox.setItemText(1, _translate("MainWindow", "green"))
        self.comboBox.setItemText(2, _translate("MainWindow", "blue"))
        self.comboBox.setItemText(3, _translate("MainWindow", "yellow"))
        self.pushButton.setText(_translate("MainWindow", "login"))
