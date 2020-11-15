import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ludo import Ui_MainWindow
from random import randint
from piece import Piece
from collections import OrderedDict

li = [0, [490, 620, [0, None]], [490, 540, [0, None]], [490, 450, [0, None]], [400, 450, [0, None]],
      [310, 450, [0, None]], [310, 360, [0, None]], [310, 280, [0, None]],
      [400, 280, [0, None]], [490, 280, [0, None]],
      [490, 180, [0, None]],
      [490, 90, [0, None]], [590, 90, [0, None]], [700, 90, [0, None]], [700, 180, [0, None]], [700, 270, [0, None]],
      [810, 270, [0, None]], [900, 270, [0, None]],
      [900, 360, [0, None]], [900, 450, [0, None]], [810, 450, [0, None]],
      [720, 450, [0, None]], [720, 540, [0, None]], [720, 620, [0, None]], [610, 620, [0, None]]]
li_home = [[610, 530], [400, 360]]

# blue = Piece('blue')
class A(QtWidgets.QPushButton):
    pass


class Ludo:
    nobat = 'blue'
    tas = None
    blue = False
    blue_pos = {}
    tas_count = 0
    red = False
    red_pos = {}

    tedad_red = 0
    tedad_blue = 0
    tedad_red_home = 0
    tedad_blue_home = 0

    def __init__(self):

        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        self.blue_pos = {self.ui.blue_1: 0, self.ui.blue_2: 0, self.ui.blue_3: 0, self.ui.blue_4: 0}
        self.red_pos = {self.ui.red_1: 0, self.ui.red_2: 0, self.ui.red_3: 0, self.ui.red_4: 0}
        # a=A(self.ui.blue_1,'blue')

        self.ui.yellow_1
        self.ui.yellow_2
        self.red_blue = {self.ui.red_1: [False, 'red', True],
                         self.ui.red_2: [False, 'red', True],
                         self.ui.red_3: [False, 'red', True],
                         self.ui.red_4: [False, 'red', True],
                         self.ui.blue_1: [False, 'blue', True],
                         self.ui.blue_2: [False, 'blue', True],
                         self.ui.blue_3: [False, 'blue', True],
                         self.ui.blue_4: [False, 'blue', True],
                         'red': [self.red, self.tedad_red, self.tedad_red_home, self.red_pos],
                         'blue': [self.blue, self.tedad_blue, self.tedad_blue_home, self.blue_pos]}
        self.d = OrderedDict({self.ui.blue_1: [410, 620], self.ui.blue_2: [320, 620],
                              self.ui.blue_3: [320, 530], self.ui.blue_4: [410, 530],
                              self.ui.red_1: [310, 200], self.ui.red_2: [310, 100],
                              self.ui.red_3: [400, 100], self.ui.red_4: [400, 200]})

        self.ui.pushButton_tas.clicked.connect(self.roll)
        # self.ui.blue_1.clicked.connect(self.move)
        self.ui.red_1.clicked.connect(self.move_red)
        self.ui.blue_2.clicked.connect(self.move)
        self.ui.red_2.clicked.connect(self.move_red)

        self.ui.blue_1.clicked.connect(self.move)
        print(self.ui.blue_1.tas)
        MainWindow.show()
        sys.exit(app.exec_())

    def roll(self):

        if self.red_blue['red'][1] > 0:
            self.red_blue['red'][0] = True
        else:
            self.red_blue['red'][0] = False
        if self.red_blue['blue'][1] > 0:
            self.red_blue['blue'][0] = True
        else:
            self.red_blue['blue'][0] = False
        self.ui.lbl_turns.setText(self.nobat)
        if self.nobat == 'blue' and self.red_blue['blue'][0] is False and self.tas_count <= 3:
            self.tas_count += 1
            self.tas = randint(1, 6)
            self.ui.lbl_tas.setText(str(self.tas))
            if self.tas == 6:
                self.ui.pushButton_tas.setEnabled(False)
                self.tas_count = 0
            elif self.tas_count == 3:
                self.nobat = 'red'
                self.tas_count = 0
        elif self.nobat == 'red' and self.red_blue['red'][0] is False and self.tas_count <= 3:
            self.tas_count += 1
            self.tas = randint(1, 6)
            self.ui.lbl_tas.setText(str(self.tas))
            if self.tas == 6:
                self.ui.pushButton_tas.setEnabled(False)
                self.tas_count = 0
            elif self.tas_count == 3:
                self.nobat = 'blue'
                self.tas_count = 0
        else:
            self.tas = randint(1, 6)
            self.ui.lbl_tas.setText(str(self.tas))
            self.ui.pushButton_tas.setEnabled(False)
            self.tas_count = 0

    def move_red(self):
        sender = self.ui.sender()

        # bara 6 avardan
        if self.nobat == 'red' and self.tas is not None:
            self.ui.pushButton_tas.setEnabled(True)
            if (self.tas == 6 and self.red_blue['red'][0] is False) or (self.tas == 6 and self.red_blue['red'][
                0] is True and self.red_blue[
                                                                            sender][0] is False and li[7][2][
                                                                            1] != 'red'):
                self.red_blue['red'][3][sender] = 7

                # """tke code zadan mohre"""
                if li[self.red_blue['red'][3][sender]][2][0] != 0 and li[self.red_blue['red'][3][sender]][2][
                    1] != 'red':
                    self.ui.x = li[self.red_pos[sender]][2][0]
                    self.ui.y = li[self.red_pos[sender]][2][1]
                    self.ui.x.move(self.d[self.ui.x][0], self.d[self.ui.x][1])
                    self.red_blue[self.ui.y][1] -= 1
                    self.red_blue[self.ui.x][0] = False
                    self.red_blue[self.ui.x][2] = True
                    li[self.red_blue[self.ui.y][3][self.ui.x]][2][1] = None
                    li[self.red_blue[self.ui.y][3][self.ui.x]][2][0] = 0

                    del self.red_blue[self.ui.y][3][self.ui.x]

                sender.move(li[7][0], li[7][1])
                li[7][2][0] = sender
                li[7][2][1] = 'red'

                self.tas = None
                print(li)

                self.red_blue[sender][0] = True

                self.red_blue['red'][1] += 1




            elif self.red_blue[sender][0]:

                # bara harekatr adi
                if self.red_blue['red'][0]:
                    # bara inke jo lotar az mamool nare
                    if self.red_blue['red'][3][sender] + self.tas >= 7 and self.red_blue['red'][3][
                        sender] + self.tas <= 24 and self.red_blue[sender][2] and \
                            li[self.red_blue['red'][3][sender] + self.tas][2][
                                1] != 'red':
                        # print('one')
                        # print(self.red_pos[0])

                        li[self.red_blue['red'][3][sender]][2][1] = None
                        li[self.red_blue['red'][3][sender]][2][0] = 0
                        self.red_blue['red'][3][sender] += self.tas

                        sender.move(li[self.red_blue['red'][3][sender]][0], li[self.red_blue['red'][3][sender]][1])
                        """tke code zadan mohre"""
                        if li[self.red_blue['red'][3][sender]][2][0] != 0 and li[self.red_blue['red'][3][sender]][2][
                            1] != 'red':
                            self.ui.x = li[self.red_pos[sender]][2][0]
                            self.ui.y = li[self.red_pos[sender]][2][1]
                            self.ui.x.move(self.d[self.ui.x][0], self.d[self.ui.x][1])
                            self.red_blue[self.ui.y][1] -= 1
                            self.red_blue[self.ui.x][0] = False
                            self.red_blue[self.ui.x][2] = True
                            li[self.red_blue[self.ui.y][3][self.ui.x]][2][1] = None
                            li[self.red_blue[self.ui.y][3][self.ui.x]][2][0] = 0
                            del self.red_blue[self.ui.y][3][self.ui.x]

                        li[self.red_blue['red'][3][sender]][2][0] = sender
                        li[self.red_blue['red'][3][sender]][2][1] = 'red'
                        if self.tas != 6:
                            self.nobat = 'blue'
                        self.tas = None
                        print(li)
                    elif self.red_blue['red'][3][sender] + self.tas > 24 and self.red_blue['red'][3][
                        sender] + self.tas - 24 < 7 and \
                            li[self.red_blue['red'][3][sender] + self.tas - 24][2][1] != 'red':
                        # print('two')

                        self.red_blue[sender][2] = False
                        li[self.red_blue['red'][3][sender]][2][0] = 0
                        li[self.red_blue['red'][3][sender]][2][1] = None
                        self.red_blue['red'][3][sender] += (self.tas - 24)

                        """tke code zadan mohre"""
                        if li[self.red_blue['red'][3][sender]][2][0] != 0 and li[self.red_blue['red'][3][sender]][2][
                            1] != 'red':
                            self.ui.x = li[self.red_pos[sender]][2][0]
                            self.ui.y = li[self.red_pos[sender]][2][1]
                            self.ui.x.move(self.d[self.ui.x][0], self.d[self.ui.x][1])
                            self.red_blue[self.ui.y][1] -= 1
                            self.red_blue[self.ui.x][0] = False
                            self.red_blue[self.ui.x][2] = True
                            li[self.red_blue[self.ui.y][3][self.ui.x]][2][1] = None
                            li[self.red_blue[self.ui.y][3][self.ui.x]][2][0] = 0
                            del self.red_blue[self.ui.y][3][self.ui.x]

                        sender.move(li[self.red_blue['red'][3][sender]][0], li[self.red_blue['red'][3][sender]][1])
                        li[self.red_blue['red'][3][sender]][2][0] = sender
                        li[self.red_blue['red'][3][sender]][2][1] = 'red'
                        if self.tas != 6:
                            self.nobat = 'blue'
                        self.tas = None
                        print(li)
                    elif self.red_blue['red'][3][sender] + self.tas < 7 and \
                            li[self.red_blue['red'][3][sender] + self.tas][2][1] != 'red' and self.red_blue[sender][0]:

                        li[self.red_blue['red'][3][sender]][2][0] = 0
                        li[self.red_blue['red'][3][sender]][2][1] = None
                        self.red_blue['red'][3][sender] += self.tas

                        self.red_blue[sender][2] = False
                        """tke code zadan mohre"""
                        if li[self.red_blue['red'][3][sender]][2][0] != 0 and li[self.red_blue['red'][3][sender]][2][
                            1] != 'red':
                            self.ui.x = li[self.red_pos[sender]][2][0]
                            self.ui.y = li[self.red_pos[sender]][2][1]
                            self.ui.x.move(self.d[self.ui.x][0], self.d[self.ui.x][1])
                            self.red_blue[self.ui.y][1] -= 1
                            self.red_blue[self.ui.x][0] = False
                            self.red_blue[self.ui.x][2] = True
                            li[self.red_blue[self.ui.y][3][self.ui.x]][2][1] = None
                            li[self.red_blue[self.ui.y][3][self.ui.x]][2][0] = 0
                            del self.red_blue[self.ui.y][3][self.ui.x]

                        sender.move(li[self.red_blue['red'][3][sender]][0], li[self.red_blue['red'][3][sender]][1])
                        li[self.red_blue['red'][3][sender]][2][0] = sender
                        li[self.red_blue['red'][3][sender]][2][1] = 'red'
                        if self.tas != 6:
                            self.nobat = 'blue'
                        self.tas = None
                        print(li)
                    elif self.red_blue['red'][3][sender] + self.tas == 7 and self.nobat == 'red':

                        sender.move(li_home[1][0], li_home[1][1])
                        li[self.red_blue['red'][3][sender]][2][0] = 0
                        li[self.red_blue['red'][3][sender]][2][1] = None
                        if self.tas != 6:
                            self.nobat = 'blue'
                        self.red_blue['red'][2] += 1

                        self.red_blue['red'][1] -= 1
                        self.tas = None
                        print('red', 'hhhhhhh', li)

                    elif self.red_blue['red'][3][sender] + self.tas >= 7 and \
                            self.red_blue[sender][0] and self.red_blue['red'][1]==1:
                        if self.tas != 6:
                            self.nobat = 'blue'
                        self.tas = None
        print()
        print(self.red_blue['red'])
        print()
        print(self.red_blue[sender], '     ', self.nobat)
        print()

    def move(self):
        sender = self.ui.sender()
        if self.nobat == 'blue' and self.tas is not None:
            self.ui.pushButton_tas.setEnabled(True)
            if (self.tas == 6 and self.red_blue['blue'][0] is False) or (self.tas == 6 and self.red_blue['blue'][
                0] is True and self.red_blue[
                                                                             sender][0] is False and li[1][2][
                                                                             1] != 'blue'):
                self.red_blue['blue'][3][sender] = 1
                self.tas = None
                print(li)
                if li[self.red_blue['blue'][3][sender]][2][0] != 0 and li[self.red_blue['blue'][3][sender]][2][
                    1] != 'blue':
                    self.ui.x = li[self.red_blue['blue'][3][sender]][2][0]
                    self.ui.y = li[self.red_blue['blue'][3][sender]][2][1]
                    self.ui.x.move(self.d[self.ui.x][0], self.d[self.ui.x][1])
                    self.red_blue[self.ui.y][1] -= 1
                    self.red_blue[self.ui.x][0] = False
                    self.red_blue[self.ui.x][2] = True
                    li[self.red_blue[self.ui.y][3][self.ui.x]][2][1] = None
                    li[self.red_blue[self.ui.y][3][self.ui.x]][2][0] = 0
                    del self.red_blue[self.ui.y][3][self.ui.x]

                sender.move(li[1][0], li[1][1])
                li[self.red_blue['blue'][3][sender]][2][0] = sender
                li[self.red_blue['blue'][3][sender]][2][1] = 'blue'

                self.red_blue[sender][0] = True
                self.red_blue['blue'][1] += 1
            # """oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo"""
            elif self.red_blue['blue'][0] and self.red_blue[sender][0] is True:
                if self.red_blue['blue'][3][sender] + self.tas <= 24 and \
                        li[self.red_blue['blue'][3][sender] + self.tas][2][1] != 'blue':
                    li[self.red_blue['blue'][3][sender]][2][0] = 0
                    li[self.red_blue['blue'][3][sender]][2][1] = None
                    self.red_blue['blue'][3][sender] += self.tas

                    sender.move(li[self.red_blue['blue'][3][sender]][0], li[self.red_blue['blue'][3][sender]][1])
                    """tike kode zadan mohre ha"""
                    if li[self.red_blue['blue'][3][sender]][2][0] != 0 and li[self.red_blue['blue'][3][sender]][2][
                        1] != 'blue':
                        self.ui.x = li[self.red_blue['blue'][3][sender]][2][0]
                        self.ui.y = li[self.red_blue['blue'][3][sender]][2][1]
                        self.ui.x.move(self.d[self.ui.x][0], self.d[self.ui.x][1])
                        self.red_blue[self.ui.y][1] -= 1
                        self.red_blue[self.ui.x][0] = False
                        self.red_blue[self.ui.x][2] = True
                        li[self.red_blue[self.ui.y][3][self.ui.x]][2][1] = None
                        li[self.red_blue[self.ui.y][3][self.ui.x]][2][0] = 0
                        del self.red_blue[self.ui.y][3][self.ui.x]

                    li[self.red_blue['blue'][3][sender]][2][0] = sender
                    li[self.red_blue['blue'][3][sender]][2][1] = 'blue'
                    print(li)
                    if self.tas != 6:
                        self.nobat = 'red'
                    self.tas = None
                elif self.red_blue['blue'][3][sender] + self.tas == 25:
                    li[self.red_blue['blue'][3][sender]][2][0] = 0
                    li[self.red_blue['blue'][3][sender]][2][1] = None
                    self.red_blue['blue'][1] -= 1
                    self.red_blue['blue'][2] += 1
                    sender.move(li_home[0][0], li_home[0][1])
                    print(li)
                    sender.setEnabled(False)
                    if self.tas != 6:
                        self.nobat = 'red'
                    self.tas = None
                elif self.red_blue['blue'][3][sender] + self.tas > 24:
                    if self.tas != 6:
                        self.nobat = 'red'
                    self.tas = None


        print()
        print(self.red_blue['blue'])
        print()
        print(self.red_blue[sender], '     ', self.nobat)
        print()


if __name__ == "__main__":
    Ludo()
