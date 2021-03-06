from random import randint
from datetime import datetime

"""This module contains the most import class which name is Game class"""
"""Game class contains all the rules that related to the ludo game"""

li = [[490, 620], [490, 540], [490, 450], [400, 450],
      [310, 450], [310, 360], [310, 280],
      [400, 280], [490, 280],
      [490, 180],
      [490, 90], [590, 90], [700, 90], [700, 180], [700, 270],
      [810, 270], [900, 270],
      [900, 360], [900, 450], [810, 450],
      [720, 450], [720, 540], [720, 620], [610, 620]]


class Game:
    board = [0] + [{'coord': i, 'piece': None} for i in li]
    tas = None
    tas_count = 0
    turn = None
    players = None
    players_color = []
    winers = []

    def __init__(self, Ludo, players):
        Game.Ludo = Ludo
        Game.players = players
        for i in Game.players:
            Game.players_color.append(i.color)
        Game.setHidden()
        Game.Ludo.ui.pushButton_tas.setEnabled(True)

    # visible the players piece on main gui
    @staticmethod
    def setHidden():
        for i in Game.players:
            for j in i.pos:
                j.setHidden(False)

    # This func handle the turn of the game
    @staticmethod
    def next_turn():
        Game.turn = Game.players_color[0]
        Game.check_number_home()
        Game.players_color.append(Game.players_color.pop(0))

    # this func choose who is the main player of the game
    @staticmethod
    def choose_player():
        for i in range(len(Game.players)):
            if Game.players[i].color == Game.turn:
                return i

    # check number of piece on home and fill the the winers list
    # if game finesh prepare the winers gui and file of winers
    @staticmethod
    def check_number_home():
        for i in Game.players:
            if i.home_number == len(Game.players[Game.choose_player()].pos):
                Game.winers.append(i)
                Game.players_color.remove(i)
        if len(Game.winers) == len(Game.players):
            with open('winers_ranks.txt', 'a') as f:
                winers = str(datetime.now()) + ' '
                for i in Game.winers:
                    winers += (i.name + ' ')
                f.write(winers)
            Game.Ludo.winers()

    # roll the dice
    @staticmethod
    def roll():
        if Game.turn is None:
            Game.next_turn()
        Game.Ludo.ui.lbl_turns.setText('Turn:' + f'{Game.players[Game.choose_player()].name}')
        Game.Ludo.ui.lbl_turns.setStyleSheet(f'color:white;background-color:{Game.turn}')
        Game.Ludo.ui.label_guid.setText(f'{Game.players[Game.choose_player()].name}' + ' roll a dice')
        Game.Ludo.ui.label_guid.setStyleSheet(f'color:{Game.turn}')
        if Game.check_number_onboard() is False and Game.tas_count <= 3:
            Game.tas_count += 1
            Game.tas = randint(1, 6)
            Game.Ludo.ui.lbl_tas.setText(str(Game.tas))
            Game.Ludo.ui.lbl_tas.setStyleSheet(f'color:{Game.turn}')
            if Game.tas == 6:
                Game.tas_count = 0
                Game.Ludo.ui.pushButton_tas.setEnabled(False)
                Game.Ludo.ui.label_guid.setText(f'{Game.players[Game.choose_player()].name}' + ' bring piece')
                Game.Ludo.ui.label_guid.setStyleSheet(f'color:{Game.turn}')
            elif Game.tas_count == 3:
                Game.next_turn()
                Game.tas_count = 0
        else:
            Game.tas = randint(1, 6)
            Game.tas_count = 0
            Game.Ludo.ui.pushButton_tas.setEnabled(False)
            Game.set_color()

    # set the lable_home of main gui
    @staticmethod
    def set_home_number():
        if Game.players[Game.choose_player()].home_number > 0:
            if Game.players[Game.choose_player()].color == 'red':
                Game.Ludo.ui.lbl_red_home.setText(str(Game.players[Game.choose_player()].home_number))
            if Game.players[Game.choose_player()].color == 'blue':
                Game.Ludo.ui.lbl_blue_home.setText(str(Game.players[Game.choose_player()].home_number))
            if Game.players[Game.choose_player()].color == 'green':
                Game.Ludo.ui.lbl_green_home.setText(str(Game.players[Game.choose_player()].home_number))
            if Game.players[Game.choose_player()].color == 'yellow':
                Game.Ludo.ui.lbl_yellow_home.setText(str(Game.players[Game.choose_player()].home_number))

    # for seting lbl of guid color in main gui
    @staticmethod
    def set_color():
        if Game.tas != 6:
            Game.Ludo.ui.label_guid.setText(f'{Game.players[Game.choose_player()].name}' + ' select your piece')
            Game.Ludo.ui.label_guid.setStyleSheet(f'color:{Game.turn}')
        else:
            Game.Ludo.ui.label_guid.setText(f'{Game.players[Game.choose_player()].name}' + ' you gotta price')
            Game.Ludo.ui.label_guid.setStyleSheet(f'color:{Game.turn}')
        Game.Ludo.ui.lbl_tas.setText(str(Game.tas))
        Game.Ludo.ui.lbl_tas.setStyleSheet(f'color:{Game.turn}')

    @staticmethod
    def check_number_onboard():
        if Game.players[Game.choose_player()].number_on_board > 0:
            return True
        else:
            return False

    """The funcs below are about the condition that players experiece"""

    # موقعیتی که نوبت بازیکن هست و تاس ۶ میاد یا بازیکن مهره نداره یا اینکه بازیکن مهره داره و
    # به عنوان جایزه می تونه مهره بیاره تو زمین و توی نقطه شروع هیچ مهره ای وجود نداره از جنس خودش
    @staticmethod
    def condination_1(piece):
        if Game.turn == piece.color:
            if (Game.tas == 6 and Game.check_number_onboard() is False) or (
                    Game.tas == 6 and Game.check_number_onboard() is True and
                    piece.on_board is False and
                    Game.board[Game.players[Game.choose_player()].start_move]['piece'] not in Game.players[
                        Game.choose_player()].pos):
                return True

    # موقعیتی که بازیکن نوبتشه و حداقل یه مهره رو تو زمین داره
    @staticmethod
    def condition_2(piece):
        if Game.turn == piece.color:
            if piece.on_board and Game.check_number_onboard():
                return True

    # موقعیتی که بازیکن قبل خانه فاینال یا همان home  خود قرار دارد و
    # موقعیت الان جمعش با عدد تاس کمتر از خونه فاینال خودش میشه و خونه جلوییش که می خواد بره
    # مهره ای از جنس خودش نباشه
    @staticmethod
    def condition_2_1(piece):
        if Game.players[Game.choose_player()].pos[piece] + Game.tas >= Game.players[
            Game.choose_player()].finally_move and Game.players[Game.choose_player()].pos[
            piece] + Game.tas <= 24 and piece.emergency and \
                Game.board[Game.players[Game.choose_player()].pos[piece] + Game.tas]['piece'] not in \
                Game.players[Game.choose_player()].pos:
            return True

    # زمانی که مهره خونه ۲۴ رو رد می کنه و جمع عدد تاسش با پوزیشن مهره از ۲۴ بیشتر میشه
    # که از پوزیشن حال حاضر مهره ۲۴ تا کم میشه
    # چون تعداد مهره های زمین ۲۴ تاست این مرحله
    # برای مهره قرمز و زرد و سبز می افته چون ابی که نباید ۲۴ رو رد کنه
    @staticmethod
    def condition_2_2(piece):
        if Game.players[Game.choose_player()].pos[piece] + Game.tas > 24 and Game.players[Game.choose_player()].pos[
            piece] + Game.tas - 24 < Game.players[Game.choose_player()].finally_move and \
                Game.board[Game.players[Game.choose_player()].pos[piece] + Game.tas - 24]['piece'] not in Game.players[
            Game.choose_player()].pos:
            return True

    # این مرحله مهره خانه ۲۴ رو رد کرده اما هنوز به خونه فاینال نرسیده پس باید پوزیشن
    # و تاس جمعشون کمتر از فاینال مهره بشه که اگر بیشتر بشه مهره نباید
    # حرکتی داشته باشه بازم این حالت برای مهره های ابی اتفاق نمی افتد چون قرار نیست خانه ۲۴ رد بشه
    @staticmethod
    def condition_2_3(piece):

        if Game.players[Game.choose_player()].pos[piece] + Game.tas < Game.players[Game.choose_player()].start_move and \
                Game.board[Game.players[Game.choose_player()].pos[piece] + Game.tas][
                    'piece'] not in Game.players[Game.choose_player()].pos and piece.on_board:
            return True

    # این مرحله برای اینه که اگر مهره جمع پوزیشن و تاس بیشتر از ۲۴ شد اما یا بیشتر از خونه فاینال خودش شد
    # اما این حرکت باعث رفتن مهره به خونه میشه مهره رو به سمت خونه اش هدایت کنه
    @staticmethod
    def condition_2_home(piece):

        if Game.players[Game.choose_player()].pos[piece] + Game.tas == Game.players[Game.choose_player()].home[2]:
            return True

    # این مرحله برای اینه هست که اگر مهره چاره ای نداشته باشه
    # برای حرکت با کلیک بر روی مهره حداقل نوبت بر
    # ه رو نفره بعدی در صورتی که فقط یه مهره تو زمین داشته باشه
    @staticmethod
    def condition_last(piece):
        if Game.players[Game.choose_player()].color == 'blue':
            z = 25
        else:
            z = Game.players[Game.choose_player()].start_move
        if Game.players[Game.choose_player()].pos[piece] + Game.tas >= z and \
                piece and Game.players[Game.choose_player()].number_on_board == 1:
            return True
