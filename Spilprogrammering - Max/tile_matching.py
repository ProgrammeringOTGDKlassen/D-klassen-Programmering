import pygame
from game import Game

# Setup pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))#, pygame.FULLSCREEN)
point_font = pygame.font.SysFont("monospace", 20, True)
restart_font = pygame.font.SysFont("monospace", 20, True)
clock = pygame.time.Clock()

# Initialize game variables
done = False
game = Game()
current_tile = (3,3)

# tile vars
tile_colors = [(0,0,0), (255,0,0), (0,255,0), (0,0,255), (255,255,0), (0,255,255)]
tile_offset = [280,530]
tile_size = [50,50]

pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)


def draw_game():
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(0,0,800,600))
    if current_tile is not None:
        t = abs((pygame.time.get_ticks() % 512) - 256) % 256
        c = (t,t,t)
        pygame.draw.rect(screen, c, pygame.Rect(tile_offset[0] + current_tile[0]*tile_size[0] - 3, tile_offset[1] - (current_tile[1]+1)*tile_size[1] - 3, tile_size[0], tile_size[1]))
    for y in range(0,len(game.grid)):
        for x in range(0,len(game.grid[y])):
            if game.anim[x][y] > 0:
                game.anim[x][y] -= 1
                if game.anim[x][y] == 0:
                    game.detect_matches()
            pygame.draw.rect(screen, tile_colors[game.grid[x][y]], pygame.Rect(tile_offset[0] + x*tile_size[0], tile_offset[1] - (y+1)*tile_size[1] - game.anim[x][y], tile_size[0]-5, tile_size[1]-5))
    screen.blit(point_font.render(f'Point: {game.point}', 0, (255,255,255)), (50,50))
    pos = pygame.mouse.get_pos()
    if 52 <= pos[0] <= 152 and 100 <= pos[1] <= 140:
        pygame.draw.rect(screen, (195,0,0), pygame.Rect(52, 100, 100, 40))
    else:
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(52, 100, 100, 40))
    screen.blit(restart_font.render("Restart", 0, (255,255,255)), (60,108))
def pixels_to_cell(x,y):
    x1 = int((x - tile_offset[0])/tile_size[0])
    y1 = int((-y + tile_offset[1])/tile_size[1])
    return x1,y1


#Main game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            done = True

        #Håndtering af input fra mus
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x_cell, y_cell = pixels_to_cell(pos[0],pos[1])

            if 0 <= x_cell < len(game.grid) and 0 <= y_cell < len(game.grid[0]):
                if current_tile is None:
                    current_tile = (x_cell, y_cell)
                else:
                    game.swap_tiles(x_cell, y_cell, current_tile[0], current_tile[1])
                    current_tile = None
                    #Når der er byttet brikker, kan vi kontrollere om der er lavet et match
                    game.detect_matches()
            if 52 <= pos[0] <= 152 and 100 <= pos[1] <= 140:
                game = Game()

    draw_game()
    #pygame kommandoer til at vise grafikken og opdatere 60 gange i sekundet.
    pygame.display.flip()
    clock.tick(60)