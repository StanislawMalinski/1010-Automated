import torch

SIZE = 9

SIZE_X = SIZE
SIZE_Y = SIZE


class Board:
    def __init__(self, board=None):
        if board is not None:
            self._board = board
        else:
            r = [0] * SIZE_X
            self._board = []
            for i in range(SIZE_Y):
                self._board.append(r.copy())
        self.s_y = len(self._board)
        self.s_x = len(self._board[0])

    def __str__(self):
        s = ""
        rows = len(self._board)
        for y in range(rows - 1, -1, -1):
            s += "|"
            for x in self._board[y]:
                s += str(x) + "|"
            s += "\n"
        return s

    def check_block(self, xc, yc, block):
        for x, y in block:
            nx = x + xc
            ny = y + yc
            if nx >= self.s_x or nx < 0 or ny >= self.s_y or ny < 0:
                return False

            if self._board[ny][nx] == 1:
                return False
        return True

    def put_block(self, xc, yc, block):
        xl = []
        yl = []
        for x, y in block:
            nx = x + xc
            ny = y + yc
            self._board[ny][nx] = 1
            if not nx in xl:
                xl.append(nx)
            if not ny in yl:
                yl.append(ny)
        self._eliminate_lines(xl, 0)
        self._eliminate_lines(yl, 1)

    def possible_moves(self, block):
        moves = []
        for x in range(self.s_x):
            for y in range(self.s_y):
                if self.check_block(x, y, block):
                    moves.append((x, y))
        return moves

    def _eliminate_lines(self, lines, dim):
        for line in lines:
            if dim == 0:
                elem = True
                for y in range(self.s_y):
                    if self._board[y][line] == 0:
                        elem = False
                        break
                if elem:
                    for y in range(self.s_y):
                        self._board[y][line] = 0
            if dim == 1:
                elem = True
                for x in range(self.s_x):
                    if self._board[line][x] == 0:
                        elem = False
                        break
                if elem:
                    for x in range(self.s_x):
                        self._board[line][x] = 0

    def get_board(self):
        return self._board

    def copy(self):
        new = []
        for r in self._board:
            new.append(r.copy())
        b = Board(new)
        return b

    def to_Tensor(self):
        t = torch.Tensor(self._board)
        if torch.cuda.is_available():
            t.to(torch.device('cuda:0'))
        return t
