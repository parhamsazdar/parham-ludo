"""This func reset all the ludo game """


# class_1=Game class
# class_2=Piece_class
# class_3=Login_class
# class_4=Ludo

def reset(class_1, class_2, class_3, class_4):
    # part_game
    class_1.tas = None
    class_1.tas_count = 0
    class_1.turn = None
    class_1.players = None
    class_1.players_color = []
    class_1.winers = []
    # part_piece
    for i in class_2.total_piece:
        i.move(i.piece_store[0], i.piece_store[1])
        i.setHidden(True)
        i.setEnabled(True)

    # part_login_player
    class_3.players = []
    class_3.selected_color = []
    # part_ludo_ui
    class_4.ui.pushButton_tas.setEnabled(False)
    class_4.ui.add.setEnabled(True)
    class_4.ui.lbl_turns.setText('')
    class_4.ui.lbl_tas.setText('')
    class_4.ui.label_guid.setText('')
    for i in class_4.lbl_home_number:
        i.setText('')
