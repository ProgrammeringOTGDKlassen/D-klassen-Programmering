import pygame


def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))


class Autist:
    def __init__(self, screen, screen_w, screen_h):
        self.screen = screen
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.width = 75
        self.height = 75
        self.x = self.width
        self.y = self.screen_h - self.height
        self.ground_lv = self.screen_h - self.height - 115
        self.walking = True
        self.walk_count = 0

        self.vy = 0
        self.grav = 1.75

        self.next_frame = pygame.time.Clock()
        self.frame = 0
        self.load_images()

    def load_images(self):
        self.autist_image = pygame.image.load("./naruto_run.png")
        self.autist_image = pygame.transform.scale(
            self.autist_image, (self.width, self.height)
        )
        self.autist_rect = self.autist_image.get_rect(x=self.x, y=self.y)
        self.running_sprites = [
            pygame.image.load("./sprites/run/tile000.png"),
            pygame.image.load("./sprites/run/tile001.png"),
            pygame.image.load("./sprites/run/tile002.png"),
            pygame.image.load("./sprites/run/tile003.png"),
            pygame.image.load("./sprites/run/tile004.png"),
        ]
        for image in self.running_sprites:
            image = pygame.transform.scale(image, ((self.width, self.height)))

    def show(self):
        # self.screen.blit(self.autist_image, self.autist_rect)
        framerate_determinator = 7
        if self.walk_count >= (len(self.running_sprites) * framerate_determinator):
            self.walk_count = 0
        if self.walking:
            self.screen.blit(
                self.running_sprites[self.walk_count // framerate_determinator],
                self.running_sprites[
                    self.walk_count // framerate_determinator
                ].get_rect(x=self.x, y=self.y),
            )
        if not self.walking:
            self.screen.blit(
                self.running_sprites[0],
                self.running_sprites[0].get_rect(x=self.x, y=self.y),
            )
        self.walk_count += 1

    def jump(self):
        if self.y == self.ground_lv:
            self.vy = -35

    def move(self):
        self.y += self.vy
        self.vy += self.grav
        self.y = constrain(self.y, 0, self.ground_lv)
        self.autist_rect = self.autist_image.get_rect(x=self.x, y=self.y)
        if self.y == self.ground_lv:
            self.walking = True
        else:
            self.walking = False


class Obstacle:
    def __init__(self, screen, screen_w, screen_h, ground_lv):
        self.screen = screen
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.width = 30
        self.height = 100
        self.x = self.screen_w
        self.ground_lv = ground_lv
        self.y = self.ground_lv

        self.load_images()

    def load_images(self):
        self.obstacle_image = pygame.image.load("./obstacle.png")
        self.obstacle_image = pygame.transform.scale(
            self.obstacle_image, (self.width, self.height)
        )
        self.obstacle_rect = self.obstacle_image.get_rect(x=self.x, y=self.y)

    def show(self):
        self.screen.blit(self.obstacle_image, self.obstacle_rect)

    def move(self):
        self.x -= 10
        self.obstacle_rect = self.obstacle_image.get_rect(x=self.x, y=self.y)


class Game:
    def __init__(self, screen, screen_w, screen_h, time):
        self.screen = screen
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.autist = Autist(self.screen, self.screen_w, self.screen_h)
        self.ground_lv = self.autist.ground_lv
        self.obstacle = Obstacle(
            self.screen, self.screen_w, self.screen_h, self.ground_lv
        )
        self.time = time
        self.score = 0

        self.load_images()
        self.draw_background()

    def draw_background(self):
        # pygame.draw.rect(
        #     self.screen, (0, 0, 0), pygame.Rect(0, 0, self.screen_w, self.screen_h)
        # )
        self.bg_rel_x = self.bg_posx % self.bg.get_rect().width
        self.screen.blit(
            self.bg, (self.bg_rel_x - self.bg.get_rect().width, self.bg_posy)
        )
        if self.bg_rel_x < self.screen_w:
            self.screen.blit(self.bg, (self.bg_rel_x, self.bg_posy))
        self.bg_posx -= 10

    def collision_check(self, rect1, rect2):
        collision = False
        if rect1.colliderect(rect2):
            collision = True
        return collision

    def get_time(self, time):
        self.time = time

    def calculate_score(self):
        self.score = self.time / 1000

    def display_score(self):
        font = pygame.font.SysFont("comicsans", 40, bold=True)
        score = "%.1f" % self.score
        score = score.replace(".", "")
        score = f"{int(score):05d}"
        label = font.render(f"SCORE: {score}", 1, (255, 255, 255))

        self.screen.blit(
            label,
            (
                self.screen_w / 2 - (label.get_width() / 2),
                self.screen_h / 6 - (label.get_height() / 2),
            ),
        )

    def load_images(self):
        self.bg = pygame.image.load("./bg2.jpg").convert()
        self.bg = pygame.transform.scale(self.bg, (self.screen_w, self.screen_h))
        self.bg_posx = 0
        self.bg_posy = 0

