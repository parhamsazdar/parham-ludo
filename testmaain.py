import sys
from PyQt5 import QtWidgets
from ludo import Ui_MainWindow
from Gameclass import Game
from functools import partial
from login_gui import Login


class Ludo:

    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        self.lbl=[self.ui.lbl_player_1,self.ui.lbl_player_2,self.ui.lbl_player_3,self.ui.lbl_player_4]
        self.ui.pushButton_tas.setEnabled(False)
        self.ui.s.triggered.connect(self.start_game)
        self.click_func()
        self.Login=None
        MainWindow.show()
        self.ui.add.triggered.connect(self.add_player)
        self.ui.blue_1.setHidden(False)
        app.exec_()

    def start_game(self):
        if len(Login.players) < 2:
            self.error_min_player()
        else:
            game = Game(self, Login.players)
            self.ui.add.setEnabled(False)
            self.set_name_player()

    def error_min_player(self):
        msg = QtWidgets.QMessageBox()
        msgBox = msg.critical(self.ui, 'Error', 'You must add atleast 2 users')
        if msgBox == QtWidgets.QMessageBox.Ok:
            msg.close()

    def add_player(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Login()
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()


    def click_func(self):
        self.ui.blue_1.clicked.connect(partial(self.ui.blue_1.move_piece, self.ui.blue_1))
        self.ui.red_1.clicked.connect(partial(self.ui.red_1.move_piece, self.ui.red_1))
        self.ui.red_2.clicked.connect(partial(self.ui.red_2.move_piece, self.ui.red_2))
        self.ui.blue_2.clicked.connect(partial(self.ui.blue_2.move_piece, self.ui.blue_2))
        self.ui.yellow_1.clicked.connect(partial(self.ui.yellow_1.move_piece, self.ui.yellow_1))
        self.ui.yellow_2.clicked.connect(partial(self.ui.yellow_2.move_piece, self.ui.yellow_2))
        self.ui.pushButton_tas.clicked.connect(Game.roll)

    def set_name_player(self):
        self.lbl=self.lbl[:len(Login.players)]
        for i in range(len(self.lbl)):
            self.lbl[i].setText(Game.players[i].name)
            self.lbl[i].setStyleSheet(f'color : {Game.players[i].color}')



a = Ludo()
