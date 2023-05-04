import random

blocks = [[[0, 0]],# malutka kostka,
            [[0, 0], [0, 1], [1, 0], [1, 1]], # mała kostka
            [[0, 0], [2, 2], [0, 2], [2, 0], [0, 1], [1, 0], [1, 1], [1, 2], [2, 1]],  # duża kostka
            [[0, 0], [2, 2], [0, 2], [0, 1], [1, 2]],  # duży kąt
            [[0, 0], [0, 1], [1, 1]], # mały kąt
            [[0, 0], [0, 1]],  # linia2
            [[0, 0], [0, 2], [0, 1]],   # linia3
            [[0, 0], [0, 3], [0, 1], [0, 2]],  # linia4
            [[0, 0], [0, 4], [0, 1], [0, 2], [0, 3]]]# linia5

def rotate(block, rotation :int):
    rotation = rotation % 4
    if rotation == 0 or len(block) <= 1:
        return block
    for i in range(1, len(block)):
        x, y = block[i]
        if rotation == 1:
            block[i] = [y, -x]
        elif rotation == 2:
            block[i] = [-x,-y]
        elif rotation == 3:
            block[i] = [-y, x]
    return block

def get_block(id=None, rot=True):
    if id is None:
        id = random.randint(0, len(blocks))
    id = id % len(blocks)
    bl = blocks[id].copy()
    if rot:
        r = random.randint(0, 4)
        return rotate(bl, r)
    return bl
