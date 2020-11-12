from random import randint


# from players import Players

# parham = Players('parham', 'blue', 1)


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
    main_player = None

    def __init__(self, *args):
        Game.players = args
        for i in args:
            Game.players_color.append(i.color)
        Game.turn = Game.players_color[0]

    @staticmethod
    def next_turn():
        Game.check_tedad_home()
        z = Game.players_color[0]
        Game.players_color.remove(Game.players_color[0])
        Game.turn = Game.players_color[0]
        Game.players_color.append(z)
        Game.choose_player()

    @staticmethod
    def choose_player():
        for i in Game.players:
            if i.color == Game.turn:
                Game.main_player = i

    @staticmethod
    def check_tedad_home():
        for i in Game.players:
            if i.home_number == 4:
                Game.players_color.remove(i)

    @staticmethod
    def roll():
        Game.check_tedad_zamin()
        if Game.main_player.confirm is False and Game.tas_count <= 3:
            Game.tas_count += 1
            Game.tas = randint(1, 6)
            if Game.tas == 6:
                Game.tas_count = 0
                # self.ui.pushButton_tas.setEnabled(False)
            elif Game.tas_count == 3:
                Game.next_turn()
                Game.tas_count = 0
        else:
            Game.tas = randint(1, 6)
            # self.ui.lbl_tas.setText(str(self.tas))
            # self.ui.pushButton_tas.setEnabled(False)
            Game.tas_count = 0

    @staticmethod
    def check_tedad_zamin():
        Game.choose_player()
        if Game.main_player.number_on_board > 0:
            Game.main_player.confirm = True
        else:
            Game.main_player.confirm = False

    @staticmethod
    def condination_1(piece):
        if (Game.tas == 6 and Game.main_player.confrim is False) or (
                Game.tas == 6 and Game.main_player.confrim is True and
                piece.on_board is False and
                Game.board[Game.main_player.start_move]['piece'] not in Game.main_player.pos):
            return True

    @staticmethod
    def condition_2(piece):
        if piece.on_board and Game.main_player.confrim:
            return True

    @staticmethod
    def condition_2_1(piece):
        if Game.main_player.pos[piece] + Game.tas >= Game.main_player.finally_move and Game.main_player.pos[
            piece] + Game.tas <= 24 and piece.emergency and \
                Game.board[Game.main_player.pos[piece] + Game.tas]['piece'] not in Game.main_player.pos:
            return True

    @staticmethod
    def condition_2_2(piece):
        if Game.main_player.pos[piece] + Game.tas > 24 and Game.main_player.pos[
            piece] + Game.tas - 24 < Game.main_player.finally_move and \
                Game.board[Game.main_player.pos[piece] + Game.tas - 24]['piece'] not in Game.main_player.pos:
            return True

    @staticmethod
    def condition_2_3(piece):
        if Game.main_player.pos[piece] + Game.tas < Game.main_player.start_move and \
                Game.board[Game.main_player.pos[piece] + Game.tas][
                    'piece'] not in Game.main_player.pos and piece.on_board:
            return True

    @staticmethod
    def condition_2_home(piece):
        if Game.main_player.pos[piece] + Game.tas == Game.main_player.home:
            return True

    @staticmethod
    def condition_last(piece):
        if Game.main_player.pos[piece] + Game.tas >= 7 and \
                piece and Game.main_player.number == 1:
            return True
