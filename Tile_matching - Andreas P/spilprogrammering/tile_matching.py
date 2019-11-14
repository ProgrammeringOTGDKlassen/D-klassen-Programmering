import pygame
from game import Game

# Setup pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))#, pygame.FULLSCREEN)
myfont = pygame.font.SysFont("monospace", 12)
clock = pygame.time.Clock()

# Initialize game variables
done = False
game = Game()
current_tile = (3,3)

# tile vars
tile_colors = [(0,0,0), (255,0,0), (0,255,0), (0,0,255), (255,255,0), (0,255,255)]
tile_offset = [280,530]
tile_size = [50,50]

restart_dim = (85, 30)
restart_pos = (120, 100)
restart_txt = (restart_pos[0] + 10, restart_pos[1] + 10)
reset_score_dim = (100, 30)
reset_score_pos = (120, 150)
reset_score_txt = (reset_score_pos[0] + 10, reset_score_pos[1] + 10)


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
    screen.blit(myfont.render("Du har {} point".format(game.points), 0, (255,255,255)), (50, 50))
    
    pos = pygame.mouse.get_pos()

    if restart_pos[0] < pos[0] < restart_pos[0] + restart_dim[0] and restart_pos[1] < pos[1] < restart_pos[1] + restart_dim[1]:
        pygame.draw.rect(screen, (255, 220, 115), pygame.Rect(restart_pos[0], restart_pos[1], restart_dim[0], restart_dim[1]))
    else:
        pygame.draw.rect(screen, (255, 207, 64), pygame.Rect(restart_pos[0], restart_pos[1], restart_dim[0], restart_dim[1]))
    screen.blit(myfont.render("RESTART", 0, (0, 0, 0)), (restart_txt[0], restart_txt[1]))

    if reset_score_pos[0] < pos[0] < reset_score_pos[0] + reset_score_dim[0] and reset_score_pos[1] < pos[1] < reset_score_pos[1] + reset_score_dim[1]:
        pygame.draw.rect(screen, (255, 220, 115), pygame.Rect(reset_score_pos[0], reset_score_pos[1], reset_score_dim[0], reset_score_dim[1]))
    else:
        pygame.draw.rect(screen, (255, 207, 64), pygame.Rect(reset_score_pos[0], reset_score_pos[1], reset_score_dim[0], reset_score_dim[1]))
    screen.blit(myfont.render("Reset score", 0, (0, 0, 0)), (reset_score_txt[0], reset_score_txt[1]))


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
            if restart_pos[0] < pos[0] < restart_pos[0] + restart_dim[0] and restart_pos[1] < pos[1] < restart_pos[1] + restart_dim[1]:
                game = Game()
            
            if reset_score_pos[0] < pos[0] < reset_score_pos[0] + reset_score_dim[0] and reset_score_pos[1] < pos[1] < reset_score_pos[1] + reset_score_dim[1]:
                game.points = 0

            if 0 <= x_cell < len(game.grid) and 0 <= y_cell < len(game.grid[0]):
                game.user_press = True
                if current_tile is None:
                    current_tile = (x_cell, y_cell)
                else:
                    game.swap_tiles(x_cell, y_cell, current_tile[0], current_tile[1])
                    current_tile = None
                    #Når der er byttet brikker, kan vi kontrollere om der er lavet et match
                    game.detect_matches()

    draw_game()

    #pygame kommandoer til at vise grafikken og opdatere 60 gange i sekundet.
    pygame.display.flip()
    clock.tick(60)
