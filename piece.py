from Gameclass import Game
from PyQt5.QtWidgets import QPushButton


class Piece(QPushButton):
    Red = []
    Green = []
    Blue = []
    Yellow = []

    def __init__(self, color, piece_store, *__args):
        super().__init__(*__args)
        self.color = color
        self.on_board = False
        self.emergency = True
        self.piece_store = piece_store
        self.add_color_list()

    def add_color_list(self):
        if self.color == 'blue':
            Piece.Blue.append(self)
        elif self.color == 'red':
            Piece.Red.append(self)
        elif self.color == 'green':
            Piece.Green.append(self)
        elif self.color == 'yellow':
            Piece.Yellow.append(self)

    def move_piece(self, piece):
        if Game.condination_1(piece):
            Game.Ludo.ui.pushButton_tas.setEnabled(True)
            Game.players[Game.choose_player()].pos[piece] = Game.players[Game.choose_player()].start_move
            piece.removing(piece, Game.players[Game.choose_player()])
            piece.move(Game.board[Game.players[Game.choose_player()].pos[piece]]['coord'][0],
                       Game.board[Game.players[Game.choose_player()].pos[piece]]['coord'][1])
            piece.record(piece, Game.players[Game.choose_player()])
            piece.initial_operation(piece, Game.players[Game.choose_player()])
            Game.tas = 0
        # part2
        elif Game.condition_2(piece):
            Game.Ludo.ui.pushButton_tas.setEnabled(True)
            if Game.condition_2_1(piece):
                piece.clearing(piece)
                Game.players[Game.choose_player()].pos[piece] += Game.tas
                piece.move(Game.board[Game.players[Game.choose_player()].pos[piece]]['coord'][0],
                           Game.board[Game.players[Game.choose_player()].pos[piece]]['coord'][1])
                piece.removing(piece, Game.players[Game.choose_player()])
                piece.record(piece, Game.players[Game.choose_player()])
                piece.check_award()
                Game.tas = 0

            elif Game.condition_2_2(piece):
                piece.emergency = False
                piece.clearing(piece)
                Game.players[Game.choose_player()].pos[piece] += (Game.tas - 24)
                piece.move(Game.board[Game.players[Game.choose_player()].pos[piece]]['coord'][0],
                           Game.board[Game.players[Game.choose_player()].pos[piece]]['coord'][1])
                piece.removing(piece, Game.players[Game.choose_player()])
                piece.record(piece, Game.players[Game.choose_player()])
                piece.check_award()
                Game.tas = 0

            # part2_3
            elif Game.condition_2_3(piece):
                piece.emergency = False
                piece.clearing(piece)
                Game.players[Game.choose_player()].pos[piece] += Game.tas
                piece.removing(piece, Game.players[Game.choose_player()])
                piece.move(Game.board[Game.players[Game.choose_player()].pos[piece]]['coord'][0],
                           Game.board[Game.players[Game.choose_player()].pos[piece]]['coord'][1])
                piece.record(piece, Game.players[Game.choose_player()])
                piece.check_award()
                Game.tas = 0
            # part2_4
            elif Game.condition_2_home(piece):
                piece.move(Game.players[Game.choose_player()].home[0], Game.players[Game.choose_player()].home[1])
                piece.clearing(piece)
                piece.final_operation(piece, Game.players[Game.choose_player()])
                piece.check_award()
                Game.tas = 0
            # part2_5
            elif Game.condition_last(piece):
                print('im in 2_last')
                piece.check_award()
                Game.tas = 0
        else:
            print(Game.turn)
            print(piece.color)

    def clearing(self, piece):
        Game.board[Game.players[Game.choose_player()].pos[piece]]['piece'] = None

    def removing(self, piece, player):
        if Game.board[player.pos[piece]]['piece'] not in player.pos and Game.board[player.pos[piece]][
            'piece'] is not None:
            x = Game.board[player.pos[piece]]['piece']
            x.move(x.piece_store[0], x.piece_store[1])
            self.who_is(x).number_on_board -= 1
            x.on_board = False
            x.emergency = True
            Game.board[player.pos[piece]]['piece'] = None
            del self.who_is(x).pos[x]

    def who_is(self, piece):
        for i in Game.players:
            if piece.color == i.color:
                return i

    def record(self, piece, player):
        Game.board[player.pos[piece]]['piece'] = piece

    def initial_operation(self, piece, player):

        piece.on_board = True
        player.number_on_board += 1

    def final_operation(self, piece, player):
        self.clearing(piece)
        player.home_number += 1
        player.number_on_board -= 1
        Game.Ludo.ui.piece.setEnabled(False)

    def check_award(self):
        if Game.tas != 6:
            Game.next_turn()
