import pygame
from game import Game, Obstacle, Autist
import random

screen_w = 1000
screen_h = 600
# Setup pygame
pygame.init()
screen = pygame.display.set_mode((screen_w, screen_h))  # , pygame.FULLSCREEN)
my_font = pygame.font.SysFont("monospace", 12)
clock = pygame.time.Clock()

# Initialize game variables
done = False
time = pygame.time.get_ticks()
game = Game(screen, screen_w, screen_h, time)
obstacles = list()


# MUSIC
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
pygame.mixer.music.load("./naruto_run.ogg")


def draw_game(done):
    time = pygame.time.get_ticks()
    game.get_time(time)
    game.draw_background()
    game.calculate_score()
    game.display_score()

    if random.random() < 0.008:
        obstacles.append(Obstacle(screen, screen_w, screen_h, game.ground_lv))

    for obstacle in obstacles:
        obstacle.move()
        obstacle.show()
        if game.collision_check(game.autist.autist_rect, obstacle.obstacle_rect):
            print("game over")
            done = True

    game.autist.move()
    game.autist.show()
    return done


pygame.mixer.music.play(-1)
# Main game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
            event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
        ):
            done = True
        if (
            event.type == pygame.KEYDOWN
            and event.key == pygame.K_SPACE
            or event.type == pygame.KEYDOWN
            and event.key == pygame.K_UP
        ):
            game.autist.jump()

    done = draw_game(done)

    # pygame kommandoer til at vise grafikken og opdatere 60 gange i sekundet.
    pygame.display.flip()
    clock.tick(60)
