import sys
from PyQt5 import QtWidgets
from ludo import Ui_MainWindow
from Gameclass import Game
from functools import partial
from login_gui import Login
from piece import Piece
from reset import reset
from winers_ import Winers

"""This is a main class that contain a buttom func and all ludo game 
Visual effects"""


# این بازی به این صورت طراحی شده مه تمام مهره ها هم دکمه اند هم از کلاس piece  هستند
# و بعد از بالا اومدن ui مهره ها ساخته میشن
# بازیکن ها توی  ماژول login تشکیل میشن و با توجه به رنگ انتخابی بازیکن ها مهره
# ها به بازیکن ها با توابع setup. توی کلاس player  اختصاص داده می شوند


class Ludo:

    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        self.Login = None
        self.lbl = [self.ui.lbl_player_1, self.ui.lbl_player_2, self.ui.lbl_player_3, self.ui.lbl_player_4]
        self.lbl_home_number = [self.ui.lbl_blue_home, self.ui.lbl_red_home, self.ui.lbl_green_home,
                                self.ui.lbl_blue_home, self.ui.lbl_yellow_home]
        self.ui.pushButton_tas.setEnabled(False)

        self.click_func()
        MainWindow.show()
        self.add_player()
        self.app.exec_()

    # new_game_messeage_dialog
    def new_game(self):
        msg = QtWidgets.QMessageBox()
        msgBox = msg.question(self.ui, 'New Game', 'Are you sure to setup new game?',
                              QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if msgBox == QtWidgets.QMessageBox.Yes:
            self.reset()
            msg.close()
        else:
            msg.close()

    # Reset_Game_func
    def reset(self):
        reset(Game, Piece, Login, self)

    # Hide_unselected_buttons
    def diable_piece(self):
        for i in Piece.total_piece:
            if i.color not in Game.players_color:
                i.setHidden(True)

    # controll_number_player_then_start_the_game
    def start_game(self):
        if len(Login.players) < 2:
            self.error_min_player()
        else:
            game = Game(self, Login.players)
            self.ui.add.setEnabled(False)
            self.set_name_player()
            self.diable_piece()

    # the dialog for show the messeage of min error
    def error_min_player(self):
        msg = QtWidgets.QMessageBox()
        msgBox = msg.critical(self.ui, 'Error', 'You must add atleast 2 users')
        if msgBox == QtWidgets.QMessageBox.Ok:
            msg.close()

    # connect to login dialog for adding player
    def add_player(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Login(dialog, self)
        dialog.ui.setupUi(dialog)
        dialog.show()

    # connect to the winers dialog for showing winers ranks
    def winers(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Winers(self, dialog)
        dialog.ui.setupUi(dialog)
        dialog.ui.lbl = dialog.ui.lbl[:len(Game.players)]
        for i in range(len(dialog.ui.lbl)):
            dialog.ui.lbl[i].setText(f'{i + 1}.{Game.winers[i].name}')
            dialog.ui.lbl[i].setStyleSheet(f'color : {Game.winers[i].color}')
        dialog.show()

    # connect the buttoms to related func
    def click_func(self):
        self.ui.green_4.clicked.connect(partial(self.ui.green_4.move_piece, self.ui.green_4))
        self.ui.green_3.clicked.connect(partial(self.ui.green_3.move_piece, self.ui.green_3))
        self.ui.green_2.clicked.connect(partial(self.ui.green_2.move_piece, self.ui.green_2))
        self.ui.green_1.clicked.connect(partial(self.ui.green_1.move_piece, self.ui.green_1))
        self.ui.yellow_4.clicked.connect(partial(self.ui.yellow_4.move_piece, self.ui.yellow_4))
        self.ui.yellow_3.clicked.connect(partial(self.ui.yellow_3.move_piece, self.ui.yellow_3))
        self.ui.red_4.clicked.connect(partial(self.ui.red_4.move_piece, self.ui.red_4))
        self.ui.red_3.clicked.connect(partial(self.ui.red_3.move_piece, self.ui.red_3))
        self.ui.blue_4.clicked.connect(partial(self.ui.blue_4.move_piece, self.ui.blue_4))
        self.ui.blue_3.clicked.connect(partial(self.ui.blue_3.move_piece, self.ui.blue_3))
        self.ui.blue_1.clicked.connect(partial(self.ui.blue_1.move_piece, self.ui.blue_1))
        self.ui.red_1.clicked.connect(partial(self.ui.red_1.move_piece, self.ui.red_1))
        self.ui.red_2.clicked.connect(partial(self.ui.red_2.move_piece, self.ui.red_2))
        self.ui.blue_2.clicked.connect(partial(self.ui.blue_2.move_piece, self.ui.blue_2))
        self.ui.yellow_1.clicked.connect(partial(self.ui.yellow_1.move_piece, self.ui.yellow_1))
        self.ui.yellow_2.clicked.connect(partial(self.ui.yellow_2.move_piece, self.ui.yellow_2))
        self.ui.add.triggered.connect(self.add_player)
        self.ui.newgame.triggered.connect(self.new_game)
        self.ui.s.triggered.connect(self.start_game)
        self.ui.pushButton_tas.clicked.connect(Game.roll)

    # for setting name of player on ludo gui
    def set_name_player(self):
        self.lbl = self.lbl[:len(Login.players)]
        for i in range(len(self.lbl)):
            self.lbl[i].setText(f'{i + 1}.{Game.players[i].name}')
            self.lbl[i].setStyleSheet(f'color : {Game.players[i].color}')


if __name__ == '__main__':
    Ludo()
