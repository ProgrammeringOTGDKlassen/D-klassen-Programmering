import pygame
from pygame import mixer
from game import Game

# Setup pygame
width = 800
height = 505
pygame.init()
screen = pygame.display.set_mode((width, height))#, pygame.FULLSCREEN)

#Skrifttyper
myfont = pygame.font.SysFont("monospace", 18, bold = True)
myfont2 = pygame.font.SysFont("monospace", 50, bold = True)
myfont3 = pygame.font.SysFont("monospace", 24, bold = True)
myfont4 = pygame.font.SysFont("monospace", 13, bold = True)

clock = pygame.time.Clock()

music = ['musik_1.mp3', 'musik_2.mp3', 'musik_3.mp3', 'musik_4.mp3']
index = 0

# Initialize game variables
done = False
game = Game()
current_tile = (3,3)
k = 1

# tile vars
tile_colors = [(0,0,0), (1,31,75), (3,57,108), (0,91,150), (100,151,177), (179,205,224)]
tile_offset = [300,505]
tile_size = [50,50]

class Playing():

    def __init__(self):
        self.width = width
        self.height = height
        self.current_tile = current_tile

    def draw_game(self):
        #Når k = 1, så vises min menu
        if k == 1:
            pos = pygame.mouse.get_pos()
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, 800, 940))
            if 5 < pos[0] < 5 + 790 and 300 < pos[1] < 300 + 50:
                pygame.draw.rect(screen, (30, 30, 130), pygame.Rect(5, 300, 790, 50))
            else:
                pygame.draw.rect(screen, (30, 30, 180), pygame.Rect(5, 300, 790, 50))

            screen.blit(myfont2.render("START", 0, (255, 255, 255)), (320, 300))

        #Når k = 2, så vises spille siden
        elif k == 2:
            pygame.draw.rect(screen, (0, 20, 70), pygame.Rect(0, 0, 800, 940))
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(295, 0, 505, 505))
            
            pos = pygame.mouse.get_pos()

            if 5 < pos[0] < 5 + 80 and 5 < pos[1] < 5 + 50:
                pygame.draw.rect(screen, (30, 30, 130), pygame.Rect(5, 5, 80, 50))

            else:
                pygame.draw.rect(screen, (30, 30, 180), pygame.Rect(5, 5, 80, 50))
            
            screen.blit(myfont3.render("MENU", 0, (255, 255, 255)), (15, 15))

            if 5 < pos[0] < 5 + 75 and 140 < pos[1] < 140 + 30:
                pygame.draw.rect(screen, (30, 30, 130), pygame.Rect(5, 140, 75, 30))

            else:
                pygame.draw.rect(screen, (30, 30, 180), pygame.Rect(5, 140, 75, 30))

            screen.blit(myfont4.render("Next", 0, (255, 255, 255)), (10, 145))

            if 5 < pos[0] < 5 + 75 and 180 < pos[1] < 180 + 30:
                pygame.draw.rect(screen, (30, 30, 130), pygame.Rect(5, 180, 75, 30))

            else:
                pygame.draw.rect(screen, (30, 30, 180), pygame.Rect(5, 180, 75, 30))

            screen.blit(myfont4.render("Past", 0, (255, 255, 255)), (10, 185))

            if self.current_tile is not None:
                t = abs((pygame.time.get_ticks() % 512) - 256) % 256
                c = (t,t,t)
                pygame.draw.rect(screen, c, pygame.Rect(tile_offset[0] + self.current_tile[0]*tile_size[0] - 3, tile_offset[1] - (
                    self.current_tile[1]+1)*tile_size[1] - 3, tile_size[0], tile_size[1]))
            for y in range(0,len(game.grid)):
                for x in range(0,len(game.grid[y])):
                    if game.anim[x][y] > 0:
                        game.anim[x][y] -= 1

                    if game.grid[x][y].special:
                        pygame.draw.rect(screen, tile_colors[game.grid[x][y].color], pygame.Rect(tile_offset[0] + x * tile_size[0], tile_offset[1] - (y + 1) * tile_size[1] - game.anim[x][y], tile_size[0] - 5, tile_size[1] - 5))
                    else: 
                        pygame.draw.rect(screen, tile_colors[game.grid[x][y].color], pygame.Rect(tile_offset[0] + x * tile_size[0],tile_offset[1] - (y + 1) * tile_size[1] - game.anim[x][y], tile_size[0] - 5, tile_size[1] - 5))

            screen.blit(myfont.render("You have {} points".format(game.points), 0, (255, 255, 255)), (5, 300))
            screen.blit(myfont.render("Highscore is {} points".format(game.highscore), 0, (255, 255, 255)), (5, 350))  
            screen.blit(myfont.render("Change song", 0, (255, 255, 255)), (5, 110))
        

    def pixels_to_cell(self,x,y):
        x1 = int((x - tile_offset[0])/tile_size[0])
        y1 = int((-y + tile_offset[1])/tile_size[1])
        return x1,y1


    #Main game loop
    def main(self):
        global index, k

        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    done = True
                
                if k == 1:

                    if event.type == pygame.KEYDOWN:
                        pygame.mixer.music.load(music[index])
                        pygame.mixer.music.play()
                        k = 2

                    #self.window.fill((0, 0, 0))

                    pos = pygame.mouse.get_pos()

                    if 5 < pos[0] < 5 + 790 and 300 < pos[1] < 300 + 50:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            pygame.mixer.music.load(music[index])
                            pygame.mixer.music.play()
                            k = 2

                elif k == 2:
                    #Håndtering af input fra mus
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        x_cell, y_cell = self.pixels_to_cell(pos[0], pos[1])

                        #Håndtering af processen, hvis man kligger på menu knappen
                        if 5 < pos[0] < 5 + 80 and 5 < pos[1] < 5 + 50:
                            pygame.mixer.music.stop()
                            k = 1

                        #Næste musik
                        if 5 < pos[0] < 5 + 75 and 140 < pos[1] < 140 + 30:
                            if index == 3:
                                index = index
                            else:
                                index += 1
                            pygame.mixer.music.stop()
                            pygame.mixer.music.load(music[index])
                            pygame.mixer.music.play()


                        #Tilbage musik
                        if 5 < pos[0] < 5 + 75 and 180 < pos[1] < 180 + 30:
                            if index == 0:
                                index = index
                            else:
                                index -= 1
                            pygame.mixer.music.stop()
                            pygame.mixer.music.load(music[index])
                            pygame.mixer.music.play()

                        if 0 <= x_cell < len(game.grid) and 0 <= y_cell < len(game.grid[0]):
                            if self.current_tile is None:
                                self.current_tile = (x_cell, y_cell)
                            else:
                                game.swap_tiles(
                                    x_cell, y_cell, self.current_tile[0], self.current_tile[1])
                                self.current_tile = None
                                #Når der er byttet brikker, kan vi kontrollere om der er lavet et match
                                game.detect_matches()

            self.draw_game()
            #pygame kommandoer til at vise grafikken og opdatere 60 gange i sekundet.
            pygame.display.flip()
            clock.tick(60)

    def play(self):
        #self.window = pygame.display.set_mode((self.width, self.height))
        self.main()  # start game
        
if __name__ == "__main__":
    playing = Playing()
    playing.play()

