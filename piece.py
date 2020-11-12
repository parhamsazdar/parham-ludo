from Gameclass import Game
from PyQt5.QtWidgets import QPushButton

class Piece(QPushButton):
    Red = []
    Green = []
    Blue = []
    Yellow = []

    def __init__(self, color, piece_store,*__args):
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

    def move(self,piece,player=Game.main_player):
        # part1
        if Game.condination_1(piece):
            player.pos[piece] = player.start_move
            self.removing( piece,player)
            piece.move(Game.board[player.pos[piece]]['coord'][0], Game.board[player.pos[piece]]['coord'][0])
            self.record(piece,player)
            self.initial_operation( piece,player)
            self.check_award()


        # part2
        elif Game.condition_2(piece):
            # part2_1
            if Game.condition_2_1(piece):
                self.clearing( piece)
                player.pos[piece] += Game.tas
                piece.move(Game.board[player.pos[piece]]['coord'][0], Game.board[player.pos[piece]]['coord'][0])
                self.removing( piece,player)
                self.record(piece,player)
                self.check_award()

            # part2_2
            elif Game.condition_2_2( piece):
                piece.emergency = False
                self.clearing( piece)
                player.pos[piece] += (Game.tas - 24)
                piece.move(Game.board[player.pos[piece]]['coord'][0], Game.board[player.pos[piece]]['coord'][0])
                self.removing(piece, player)
                self.record(piece,player)
                self.check_award()

            # part2_3
            elif Game.condition_2_3(piece):
                piece.emergency = False
                player.pos[piece] = Game.tas
                self.removing(piece, player)
                piece.move(Game.board[player.pos[piece]]['coord'][0], Game.board[player.pos[piece]]['coord'][0])
                self.record(piece,player)
                self.check_award()

            # part2_4
            elif Game.condition_2_home(piece):
                piece.move(player.home[0], player.home[0][1])
                self.clearing(piece)
                self.check_award()
                self.final_operation(piece,player)
            # part2_5
            elif Game.condition_last(piece):
                self.check_award()

    def clearing(self, piece):
        Game.board['piece'] = piece

    def removing(self, piece, player):
        if Game.board[player.pos[piece]]['piece'] not in player.pos and Game.board[player.pos[piece]][
            'piece'] is not None:
            x = Game.board[player.pos[piece]]['piece']
            x.move(x.piecestore[0], x.piecestore[1])
            self.who_is(x).number_on_board -= 1
            piece.on_board = False
            piece.emergency = True
            Game.board[player.pos[piece]]['piece'] = None
            del self.who_is(x).pos[x]

    def who_is(self, piece):
        for i in Game.players:
            if piece.color == i.color:
                return i

    def record(self, piece,player):
        Game.board[player.pos[piece]]['piece'] = piece


    def initial_operation(self, piece,player):
        piece.on_board = True
        player.number_on_board+=1

    def final_operation(self, piece,player):
        self.clearing(piece)
        player.home_number += 1
        player.number_on_board-= 1

    def check_award(self):
        if Game.tas != 6:
            Game.next_turn()
        Game.tas = None
