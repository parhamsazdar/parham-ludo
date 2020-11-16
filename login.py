import sys
from login_gui import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox
from players import Players


class Login:
    players = []

    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        self.ui.pushButton.clicked.connect(self.isvalid_player)
        MainWindow.show()
        sys.exit(app.exec_())

    def isvalid_player(self):
        if len(Login.players) <= 3:
            user_ = self.ui.lineEdit.text()
            pass_ = self.ui.lineEdit_2.text()
            color_ = self.ui.comboBox.currentText()
            with open('users') as f:
                li = []
                for i in f.readlines():
                    i = i.strip()
                    i = i.split(',')
                    li.extend(i)

                if (user_ and pass_ in li) and li.index(pass_) - li.index(user_) == 1:
                    Login.players.append(Players(f'{user_}', f'{color_}'))
                    x = self.ui.comboBox.currentIndex()
                    self.ui.comboBox.removeItem(x)
                    self.add()
                else:
                    self.error_notexist()
        else:
            self.max_error()

    def max_error(self):
        msg = QMessageBox()
        msgBox = msg.critical(self.ui, 'Error', 'You added 4 players')
        if msgBox == QMessageBox.Ok:
            msg.close()

    def error_notexist(self):
        msg = QMessageBox()
        msgBox = msg.critical(self.ui, 'Error', 'This user dosent exist')
        if msgBox == QMessageBox.Ok:
            msg.close()

    def add(self):
        msg = QMessageBox()
        msgBox = msg.information(self.ui, 'Add player', 'The user adds succefully')
        if msgBox == QMessageBox.Ok:
            msg.close()


if __name__ == '__main__':
    Login()
