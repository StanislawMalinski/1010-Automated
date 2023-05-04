import pygame


class Display:

    def __init__(self, board, max_fps=300):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.backgroundColor = (153, 153, 153)
        self.tileColor = (100, 153, 153)
        self.resourcesColor = (29, 122, 29)
        self.hatcheryColor = (150, 45, 45)
        self.highlightedColor = (81, 210, 252)
        self.selectedColor = (255, 225, 64)
        self.max_fps = max_fps

        self.DEFAULT_WIDTH = 900
        self.DEFAULT_HEIGHT = 600

        self.TILE_SIZE = 60

        self.width = self.DEFAULT_WIDTH
        self.height = self.DEFAULT_HEIGHT

        self.main_surface = pygame.Surface((self.DEFAULT_WIDTH, self.DEFAULT_HEIGHT))

        self.window_scale = 1

        self.tileButtons = []

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Fuck 1010!")

        self.Board = board

    def update_window(self, score=None):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        self.main_surface.fill(self.backgroundColor)
        self.draw_board()
        self.screen.blit(self.main_surface, (0, 0))
        self.clock.tick(self.max_fps)

        if score is not None:
            green = (0, 255, 0)
            blue = (0, 0, 128)
            font = pygame.font.Font('freesansbold.ttf', 32)
            text = font.render(str(score), True, green, blue)
            textRect = text.get_rect()
            textRect.center = (700, 30)
            self.screen.blit(text, textRect)


        pygame.display.update()


    def set_board(self, b):
        self.Board = b

    def draw_board(self):
        board_cord = self.Board.get_board()
        off = 5
        Y_off = len(board_cord) * (self.TILE_SIZE + off)
        for y, row in enumerate(board_cord):
            for x, col in enumerate(row):
                vertices = [[x * (self.TILE_SIZE + off), Y_off - y * (self.TILE_SIZE + off)],
                            [(x + 1) * (self.TILE_SIZE + off) - off, Y_off - y * (self.TILE_SIZE + off)],
                            [(x + 1) * (self.TILE_SIZE + off) - off, Y_off - (y + 1) * (self.TILE_SIZE + off) + off],
                            [x * (self.TILE_SIZE + off), Y_off - (y + 1) * (self.TILE_SIZE + off) + off]]

                if col == 0:
                    pygame.draw.polygon(self.main_surface, self.tileColor, vertices)
                if col == 1:
                    pygame.draw.polygon(self.main_surface, self.resourcesColor, vertices)
