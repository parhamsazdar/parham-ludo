from random import randint
from datetime import datetime


class Game:
    board = [0, {'coord': (490, 620), 'piece': None}, {'coord': (490, 540), 'piece': None},
             {'coord': (490, 450), 'piece': None},
             {'coord': (400, 450), 'piece': None}, {'coord': (310, 450), 'piece': None},
             {'coord': (310, 360), 'piece': None},
             {'coord': (310, 280), 'piece': None}, {'coord': (400, 280), 'piece': None},
             {'coord': (490, 280), 'piece': None},
             {'coord': (490, 180), 'piece': None}, {'coord': (490, 90), 'piece': None},
             {'coord': (590, 90), 'piece': None},
             {'coord': (700, 90), 'piece': None}, {'coord': (700, 180), 'piece': None},
             {'coord': (700, 270), 'piece': None},
             {'coord': (810, 270), 'piece': None}, {'coord': (900, 270), 'piece': None},
             {'coord': (900, 360), 'piece': None},
             {'coord': (900, 450), 'piece': None}, {'coord': (810, 450), 'piece': None},
             {'coord': (720, 450), 'piece': None},
             {'coord': (720, 540), 'piece': None}, {'coord': (720, 620), 'piece': None},
             {'coord': (610, 620), 'piece': None}]
    tas = None
    tas_count = 0
    turn = None
    players = None
    players_color = []
    winers = []

    def __init__(self, Ludo, players):

        Game.Ludo = Ludo
        Game.players = players
        print(Game.players)
        for i in Game.players:
            Game.players_color.append(i.color)
        Game.setHidden()
        Game.Ludo.ui.pushButton_tas.setEnabled(True)
        print(Game.players_color)

    @staticmethod
    def setHidden():
        for i in Game.players:
            for j in i.pos:
                j.setHidden(False)

    @staticmethod
    def next_turn():

        Game.turn = Game.players_color[0]
        Game.check_number_home()
        Game.players_color.append(Game.players_color.pop(0))

    @staticmethod
    def choose_player():
        for i in range(len(Game.players)):
            if Game.players[i].color == Game.turn:
                return i

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

    @staticmethod
    def condination_1(piece):
        if Game.turn == piece.color:
            if (Game.tas == 6 and Game.check_number_onboard() is False) or (
                    Game.tas == 6 and Game.check_number_onboard() is True and
                    piece.on_board is False and
                    Game.board[Game.players[Game.choose_player()].start_move]['piece'] not in Game.players[
                        Game.choose_player()].pos):
                return True

    @staticmethod
    def condition_2(piece):
        if Game.turn == piece.color:
            if piece.on_board and Game.check_number_onboard():
                return True

    @staticmethod
    def condition_2_1(piece):
        if Game.players[Game.choose_player()].pos[piece] + Game.tas >= Game.players[
            Game.choose_player()].finally_move and Game.players[Game.choose_player()].pos[
            piece] + Game.tas <= 24 and piece.emergency and \
                Game.board[Game.players[Game.choose_player()].pos[piece] + Game.tas]['piece'] not in \
                Game.players[Game.choose_player()].pos:
            return True

    @staticmethod
    def condition_2_2(piece):
        if Game.players[Game.choose_player()].pos[piece] + Game.tas > 24 and Game.players[Game.choose_player()].pos[
            piece] + Game.tas - 24 < Game.players[Game.choose_player()].finally_move and \
                Game.board[Game.players[Game.choose_player()].pos[piece] + Game.tas - 24]['piece'] not in Game.players[
            Game.choose_player()].pos:
            return True

    @staticmethod
    def condition_2_3(piece):

        if Game.players[Game.choose_player()].pos[piece] + Game.tas < Game.players[Game.choose_player()].start_move and \
                Game.board[Game.players[Game.choose_player()].pos[piece] + Game.tas][
                    'piece'] not in Game.players[Game.choose_player()].pos and piece.on_board:
            return True

    @staticmethod
    def condition_2_home(piece):

        if Game.players[Game.choose_player()].pos[piece] + Game.tas == Game.players[Game.choose_player()].home[2]:
            return True

    @staticmethod
    def condition_last(piece):
        if Game.players[Game.choose_player()].color == 'blue':
            z = 25
        else:
            z = Game.players[Game.choose_player()].start_move
        if Game.players[Game.choose_player()].pos[piece] + Game.tas >= z and \
                piece and Game.players[Game.choose_player()].number_on_board == 1:
            return True
