from Game.GameUI import GameUI

def game_tree(ui :GameUI):
    positions = {}
    nui = ui.copy()
    nui.save_pos()
    moves = nui.possible_moves()

    for move in moves:
        ind, cords = move
        for cord in cords:
            nui.put_block(cord[0], cord[1], ind)
            positions[nui.get_board()] = (ind, cord)
            nui.reset_to_save()

    return positions
