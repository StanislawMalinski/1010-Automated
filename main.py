from pstats import SortKey

from AI.GameTree import game_tree
from Game.GUI import Display
from Game.GameUI import GameUI
import cProfile, pstats, io

def profile_func(func):
    pr = cProfile.Profile()
    pr.enable()

    func()

    pr.disable()
    s = io.StringIO()
    sortby = SortKey.CUMULATIVE
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print(s.getvalue())


SIZE = 7
if __name__ == '__main__':
    ui = GameUI()
    ui.new_game()
    board = ui.get_board()
    d = Display(board)

    dic = game_tree(ui)

    while True:
        d.update_window()



