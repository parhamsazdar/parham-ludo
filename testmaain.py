import sys
from PyQt5 import QtWidgets
from ludo import Ui_MainWindow
from players import Players
from Gameclass import Game
from functools import partial


class Ludo:
    player_1 = None

    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        self.setupplayers()
        game = Game(self, Ludo.player_1, Ludo.player_3, Ludo.player_2)
        self.click_func()
        self.set_name_player()
        MainWindow.show()
        app.exec_()

    def click_func(self):
        self.ui.blue_1.clicked.connect(partial(self.ui.blue_1.move_piece, self.ui.blue_1))
        self.ui.red_1.clicked.connect(partial(self.ui.red_1.move_piece, self.ui.red_1))
        self.ui.red_2.clicked.connect(partial(self.ui.red_2.move_piece, self.ui.red_2))
        self.ui.blue_2.clicked.connect(partial(self.ui.blue_2.move_piece, self.ui.blue_2))
        self.ui.yellow_1.clicked.connect(partial(self.ui.yellow_1.move_piece, self.ui.yellow_1))
        self.ui.yellow_2.clicked.connect(partial(self.ui.yellow_2.move_piece, self.ui.yellow_2))
        self.ui.pushButton_tas.clicked.connect(Game.roll)

    def set_name_player(self):
        self.ui.lbl_player_1.setText(Game.players[0].name)
        self.ui.lbl_player_1.setStyleSheet(f'color : {Game.players[0].color}')
        self.ui.lbl_player_2.setText(Game.players[1].name)
        self.ui.lbl_player_2.setStyleSheet(f'color : {Game.players[1].color}')
        self.ui.lbl_player_3.setText(Game.players[2].name)
        self.ui.lbl_player_3.setStyleSheet(f'color : {Game.players[2].color}')
        self.ui.lbl_player_4.setText('')

    def setupplayers(self):
        Ludo.player_1 = Players('parham', 'red', 1)
        Ludo.player_2 = Players('hasan', 'blue', 2)
        Ludo.player_3 = Players('omid', 'yellow', 3)


a = Ludo()
