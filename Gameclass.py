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
    players=None
    # d_rep = {}
    players_color = []
    main_player=None
    def __init__(self, *args):
        Game.players = args
        for i in args:
            Game.players_color.append(i.color)
        Game.turns = Game.players_color[0]

    def next_turn(self):
        self.check_tedad_home()
        z = Game.players_color[0]
        Game.players_color.remove(Game.players_color[0])
        Game.turns = Game.players_color[0]
        Game.players_color.append(z)

    def choose_player(self):
        for i in Game.players:
            if i.color == self.turn:
                Game.main_player = i

    def check_tedad_home(self):
        for i in Game.players_color:
            if Game.total[i][2] == 4:
                Game.players_color.remove(i)

    def roll(self):
        self.check_tedad_zamin()
        if Game.total[Game.turn][0] is False and Game.tas_count <= 3:
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

    def check_tedad_zamin(self):
        if Game.total[Game.turn][1] > 0:
            Game.total[Game.turn][0] = True
        else:
            Game.total[Game.turn][0] = False

    def condination_1(self, piece):
        self.main_player = parham
        if (Game.tas == 6 and self.main_player.confrim is False) or (
                Game.tas == 6 and self.main_player.confrim is True and
                piece.on_board is False and
                Game.board[self.main_player.start_move]['piece'] not in self.main_player.pos):
            return True

    def condition_2(self, piece):
        if piece.on_board and self.main_player.confrim:
            return True

    def condition_2_1(self, piece):
        if self.main_player.pos[piece] + Game.tas >= self.main_player.finally_move and self.main_player.pos[
            piece] + Game.tas <= 24 and piece.emergency and \
                Game.board[self.main_player.pos[piece] + Game.tas]['piece'] not in self.main_player.pos:
            return True

    def condition_2_2(self, piece):
        if self.main_player.pos[piece] + Game.tas > 24 and self.main_player.pos[
            piece] + Game.tas - 24 < self.main_player.finally_move and \
                Game.board[self.main_player.pos[piece] + Game.tas - 24]['piece'] not in self.main_player.pos:
            return True

    def condition_2_3(self, piece):
        if self.main_player.pos[piece] + Game.tas < self.main_player.start_move and \
                Game.board[self.main_player.pos[piece] + Game.tas][
                    'piece'] not in self.main_player.pos and piece.on_board:
            return True

    def condition_2_home(self, piece):
        if self.main_player.pos[piece] + Game.tas == self.main_player.home:
            return True

    def condition_last(self,piece):
        if self.main_player.pos[piece] + Game.tas >= 7 and \
                piece and self.main_player.number == 1:
            return True
