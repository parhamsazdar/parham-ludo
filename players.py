
from piece import Piece


class Players:
    def __init__(self, name, color, number):
        self.name = name
        self.color = color
        self.number = number
        self.confrim = False
        self.number_on_board = 0
        self.home_number = 0
        self.pos = {}
        self.setup_piece()
        self.setup_start_direction()
        self.setup_home_direction()
        self.finally_move = self.start_move - 1

    def setup_piece(self):
        if self.color == 'blue':
            for i in Piece.Blue:
                self.pos[i] = None
        elif self.color == 'red':
            for i in Piece.Red:
                self.pos[i] = None

        elif self.color == 'green':
            for i in Piece.Green:
                self.pos[i] = None

        elif self.color == 'yellow':
            for i in Piece.Yellow:
                self.pos[i] = None

    def setup_start_direction(self):
        if self.color == 'blue':
            self.start_move = 1
        elif self.color == 'red':
            self.start_move = 7
        elif self.color == 'green ':
            self.start_move = 13
        elif self.color == 'yellow':
            self.start_move = 19

    def setup_home_direction(self):
        if self.color == 'blue':
            self.home = (610, 530)
        elif self.color == 'red':
            self.home = (400, 360)
        elif self.color == 'green ':
            self.home = (600, 170)
        elif self.color == 'yellow':
            self.home = (810, 370)

