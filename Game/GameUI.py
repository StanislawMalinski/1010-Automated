from Game.Board import Board
from Game.Tiles import get_block


class GameUI:
    def __init__(self):
        self.board = None
        self.score = 0
        self.blocks = []
        self.running = False

    def isdone(self):
        if not self.running:
            return True
        return len(self.possible_moves()) == 0

    def new_game(self, board=None, blocks=None):
        self.running = True
        if board is None:
            self.board = Board()
        else:
            self.board = board
        self.score = 0
        if blocks is None:
            self.blocks = [get_block(), get_block(), get_block()]
        else:
            self.blocks = blocks

    def put_block(self, x, y, block):
        if block is not None:
            bl = self.blocks[block]
            self.score += len(bl)
            self.board.put_block(x, y, bl)
            self.blocks[block] = None

        done = True
        for block in self.blocks:
            if block is not None:
                done = False
                break
        if done:
            self.blocks = [get_block(), get_block(), get_block()]
        self.isdone()

    def possible_moves(self):
        moves = []
        for ind, block in enumerate(self.blocks):
            if block is None:
                continue
            mov_for_block = self.board.possible_moves(block)
            if len(mov_for_block) > 0:
                moves.append((ind, mov_for_block))
        self.running = len(moves) != 0
        return moves

    def show_board(self):
        print(self.board)
        for block in self.blocks:
            print(block)

    def show_points(self):
        print(self.score)

    def get_board(self):
        return self.board

    def get_blocks(self):
        return self.blocks

    def copy(self):
        nui = GameUI()
        nui.new_game(self.board.copy(), self.blocks.copy())
        return nui

    def save_pos(self):
        self.mem = (self.board.copy(), self.blocks.copy())

    def reset_to_save(self):
        self.board = self.mem[0].copy()
        self.blocks = self.mem[1].copy()
