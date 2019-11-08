import pygame, random, os

ABS_FILEPATH = os.path.dirname(os.path.abspath(__file__))

"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""

pygame.font.init()

# MUSIC
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
pygame.mixer.music.load(fr"{ABS_FILEPATH}\music\tetris_back_music.ogg")

# GLOBALS VARS
s_width = 800
s_height = 700
play_height = 600
play_width = play_height // 2

top_left_x = s_width * 0.20
top_left_y = s_height - play_height


# SHAPE FORMATS
S = [
    [".....", ".....", "..00.", ".00..", "....."],
    [".....", "..0..", "..00.", "...0.", "....."],
]

Z = [
    [".....", ".....", ".00..", "..00.", "....."],
    [".....", "..0..", ".00..", ".0...", "....."],
]

I = [
    ["..0..", "..0..", "..0..", "..0..", "....."],
    [".....", "0000.", ".....", ".....", "....."],
]

O = [[".....", ".....", ".00..", ".00..", "....."]]

J = [
    [".....", ".0...", ".000.", ".....", "....."],
    [".....", "..00.", "..0..", "..0..", "....."],
    [".....", ".....", ".000.", "...0.", "....."],
    [".....", "..0..", "..0..", ".00..", "....."],
]

L = [
    [".....", "...0.", ".000.", ".....", "....."],
    [".....", "..0..", "..0..", "..00.", "....."],
    [".....", ".....", ".000.", ".0...", "....."],
    [".....", ".00..", "..0..", "..0..", "....."],
]

T = [
    [".....", "..0..", ".000.", ".....", "....."],
    [".....", "..0..", "..00.", "..0..", "....."],
    [".....", ".....", ".000.", "..0..", "....."],
    [".....", "..0..", ".00..", "..0..", "....."],
]

shapes = [S, Z, I, O, J, L, T]
shape_colors = [
    (0, 255, 0),
    (255, 0, 0),
    (0, 255, 255),
    (255, 255, 0),
    (255, 165, 0),
    (0, 0, 255),
    (150, 0, 150),
]
# index 0 - 6 represent shape

shadow_colors = [
    (0, 150, 0),
    (150, 0, 0),
    (0, 150, 150),
    (150, 150, 0),
    (150, 80, 0),
    (0, 0, 150),
    (70, 0, 70),
]


class Piece(object):
    rows = 20  # y
    columns = 10  # x

    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0  # number from 0-3


class Game(object):
    def create_grid(self, locked_positions={}):
        self.grid = [[(0, 0, 0) for x in range(10)] for x in range(20)]

        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if (j, i) in locked_positions:
                    c = locked_positions[(j, i)]
                    self.grid[i][j] = c

        return self.grid

    def main(self):
        global grid

        pygame.mixer.music.play(-1)

        locked_positions = {}  # (x,y):(255,0,0)
        grid = self.create_grid(locked_positions)

        change_piece = False
        run = True
        self.current_piece = self.get_shape()
        self.shadow = self.get_shape()
        self.update_shadow()
        next_piece = self.get_shape()
        clock = pygame.time.Clock()
        fall_time = 0

        while run:
            fall_speed = 0.27

            grid = self.create_grid(locked_positions)
            fall_time += clock.get_rawtime()
            clock.tick()

            # PIECE FALLING CODE
            if fall_time / 1000 >= fall_speed:
                fall_time = 0
                self.current_piece.y += 1
                if (
                    not (self.valid_space(self.current_piece, grid))
                    and self.current_piece.y > 0
                ):
                    self.current_piece.y -= 1
                    change_piece = True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.display.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.current_piece.x -= 1
                        if not self.valid_space(self.current_piece, grid):
                            self.current_piece.x += 1
                        self.update_shadow()

                    elif event.key == pygame.K_RIGHT:
                        self.current_piece.x += 1
                        if not self.valid_space(self.current_piece, grid):
                            self.current_piece.x -= 1
                        self.update_shadow()
                    elif event.key == pygame.K_UP:
                        # rotate shape
                        self.current_piece.rotation = (
                            self.current_piece.rotation
                            + 1 % len(self.current_piece.shape)
                        )
                        if not self.valid_space(self.current_piece, grid):
                            self.current_piece.rotation = (
                                self.current_piece.rotation
                                - 1 % len(self.current_piece.shape)
                            )
                        # self.shadow.rotation = self.current_piece.rotation
                        self.update_shadow()

                    if event.key == pygame.K_DOWN:
                        # move shape down
                        self.current_piece.y += 1
                        if not self.valid_space(self.current_piece, grid):
                            self.current_piece.y -= 1
                        self.update_shadow()

                    if event.key == pygame.K_SPACE:
                        while self.valid_space(self.current_piece, grid):
                            self.current_piece.y += 1
                        self.current_piece.y -= 1
                        self.update_shadow()
                        # TODO fix this:
                        # print(self.convert_shape_format(self.current_piece))

            shape_pos = self.convert_shape_format(self.current_piece)

            # add piece to the grid for drawing
            for i in range(len(shape_pos)):
                x, y = shape_pos[i]
                if y > -1:
                    grid[y][x] = self.current_piece.color

            self.draw__shadow()

            # IF PIECE HIT GROUND
            if change_piece:
                for pos in shape_pos:
                    p = (pos[0], pos[1])
                    locked_positions[p] = self.current_piece.color
                self.current_piece = next_piece
                self.update_shadow()
                next_piece = self.get_shape()
                change_piece = False

                # call four times to check for multiple clear rows
                self.clear_rows(grid, locked_positions)

            self.draw_window(self.win)
            self.draw_next_shape(next_piece, self.win)
            pygame.display.update()

            # Check if user lost
            if self.check_lost(locked_positions):
                run = False

        self.game_over()
        pygame.display.update()
        pygame.time.delay(2000)

    def game_over(self):
        self.draw_text_middle("You Lost", 40, (255, 255, 255), self.win)
        pygame.mixer.music.pause()

    def draw_text_middle(self, text, size, color, surface):
        font = pygame.font.SysFont("comicsans", size, bold=True)
        label = font.render(text, 1, color)

        surface.blit(
            label,
            (
                s_width / 2 - (label.get_width() / 2),
                s_height / 2 - label.get_height() / 2,
            ),
        )

    def convert_shape_format(self, shape):
        positions = []
        format = shape.shape[shape.rotation % len(shape.shape)]

        for i, line in enumerate(format):
            row = list(line)
            for j, column in enumerate(row):
                if column == "0":
                    positions.append((shape.x + j, shape.y + i))

        for i, pos in enumerate(positions):
            positions[i] = (pos[0] - 2, pos[1] - 4)

        return positions

    def check_lost(self, positions):
        for pos in positions:
            x, y = pos
            if y < 1:
                return True
        return False

    def valid_space(self, shape, grid):
        accepted_positions = [
            [(j, i) for j in range(10) if grid[i][j] == (0, 0, 0)] for i in range(20)
        ]
        accepted_positions = [j for sub in accepted_positions for j in sub]
        formatted = self.convert_shape_format(shape)

        for pos in formatted:
            if pos not in accepted_positions:
                if pos[1] > -1:
                    return False

        return True

    def draw_window(self, surface):
        surface.fill((0, 0, 0))
        # Tetris Title
        font = pygame.font.SysFont("comicsans", 60)
        label = font.render("TETRIS", 1, (255, 255, 255))

        surface.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2), 30))

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                pygame.draw.rect(
                    surface,
                    grid[i][j],
                    (top_left_x + j * 30, top_left_y + i * 30, 30, 30),
                    0,
                )

        # draw grid and border
        self.draw_grid(surface, 20, 10)
        pygame.draw.rect(
            surface, (107, 252, 3), (top_left_x, top_left_y, play_width, play_height), 5
        )
        # pygame.display.update()

    def get_shape(self):
        global shapes, shape_colors

        return Piece(5, 0, random.choice(shapes))

    def draw__shadow(self):
        self.shadow.x = self.current_piece.x
        while self.valid_space(self.shadow, grid):
            self.shadow.y += 1
        self.shadow.y -= 1
        shape_pos = self.convert_shape_format(self.shadow)

        # add piece to the grid for drawing
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = self.shadow.color

    def update_shadow(self):
        self.shadow.shape = self.current_piece.shape
        self.set_shadow_color()
        self.shadow.rotation = self.current_piece.rotation

    def set_shadow_color(self):
        for i in range(len(shape_colors)):
            if shape_colors[i] == self.current_piece.color:
                self.shadow.color = shadow_colors[i]

    def draw_grid(self, surface, row, col):
        sx = top_left_x
        sy = top_left_y
        for i in range(row):
            pygame.draw.line(
                surface,
                (128, 128, 128),
                (sx, sy + i * 30),
                (sx + play_width, sy + i * 30),
            )  # horizontal lines
            for j in range(col):
                pygame.draw.line(
                    surface,
                    (128, 128, 128),
                    (sx + j * 30, sy),
                    (sx + j * 30, sy + play_height),
                )  # vertical lines

    def clear_rows(self, grid, locked):
        # need to see if row is clear to shift every other row above down one

        inc = 0
        for i in range(len(grid) - 1, -1, -1):
            row = grid[i]
            if (0, 0, 0) not in row:
                inc += 1
                # add positions to remove from locked
                ind = i
                for j in range(len(row)):
                    try:
                        del locked[(j, i)]
                    except:
                        continue
        if inc > 0:
            for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
                x, y = key
                if y < ind:
                    newKey = (x, y + inc)
                    locked[newKey] = locked.pop(key)

    def draw_next_shape(self, shape, surface):
        font = pygame.font.SysFont("comicsans", 30)
        label = font.render("Next Shape", 1, (255, 255, 255))

        sx = top_left_x + play_width + 50
        sy = top_left_y + play_height / 2 - 100
        format = shape.shape[shape.rotation % len(shape.shape)]

        for i, line in enumerate(format):
            row = list(line)
            for j, column in enumerate(row):
                if column == "0":
                    pygame.draw.rect(
                        surface, shape.color, (sx + j * 30, sy + i * 30, 30, 30), 0
                    )

        surface.blit(label, (sx + 10, sy - 30))

    def main_menu(self):
        run = True
        while run:
            self.win.fill((0, 0, 0))
            self.draw_text_middle(
                "Press any key to begin.", 60, (255, 255, 255), self.win
            )
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:
                    self.main()
        pygame.quit()

    def play(self):
        self.win = pygame.display.set_mode((s_width, s_height))
        pygame.display.set_caption("Tetris")

        self.main_menu()  # start game


if __name__ == "__main__":
    game = Game()
    game.play()
