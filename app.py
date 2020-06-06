import pygame
import math
from random import randint
from player import Player
from virus import Virus
from bullet import Bullet


class Game:
    
    
    score = 0
    RUNNING = True
    
    def __init__(self):
        
        #initialize the pygame
        pygame.init()

       #create your screen
        self.screen = pygame.display.set_mode((400, 400))

       #Background
        self.background = pygame.image.load('assets/background.jpg')


       #add title and icon
        pygame.display.set_caption("Space Invaders")
        self.icon = pygame.image.load('assets/transportation.png')

        pygame.display.set_icon(self.icon)

        self.init_elements()

        

    def run_game(self, player, virus, bullet):
        while self.RUNNING:
             # set screen background with RGB
            self.screen.fill((0, 0, 0))

            #Background
            self.screen.blit(self.background, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.RUNNING = False

                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_LEFT:
                       player.player_X_change = -3

                    if event.key == pygame.K_RIGHT:
                        player.player_X_change = 3

                    if event.key == pygame.K_SPACE:
                         if bullet.bullet_state is 'ready':
                             bullet.bullet_X = player.player_X
                             player.fire_bullet(self.screen, bullet, player.player_X, player.player_Y)

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        player.player_X_change = 0

            
    
            player.move()
    
            for i in range(virus.number_of_viruses):
                
                #Move virus
                virus.move(i)
                
                #Collision
                collision = self.isCollision(virus.virus_X[i], virus.virus_Y[i], bullet.bullet_X, bullet.bullet_Y)
                if collision:
                    bullet.bullet_Y = 300
                    bullet.set_state('ready')
                    self.score += 1
                    virus.virus_X[i] = randint(0, 360)
                    virus.virus_Y[i] = randint(30, 100)

                virus.paint_virus(self.screen, virus.virus_X[i], virus.virus_Y[i], i)

            #Move bullet
            bullet.move()

            if bullet.bullet_state is 'fire':
               player.fire_bullet(self.screen, bullet, player.player_X, player.player_Y)
               bullet.bullet_Y -= bullet.bullet_Y_change


    

            player.paint_player(self.screen, player.player_X, player.player_Y)
    
            pygame.display.update()
    
    def init_elements(self):
        player = Player()
        virus = Virus()
        bullet = Bullet()

        self.run_game(player, virus, bullet)

    def isCollision(self, virus_X, virus_Y, bullet_X, bullet_Y):
        distance = math.sqrt((math.pow(virus_X - bullet_X,2)) + ( math.pow(virus_Y - bullet_Y,2)))
        if distance < 27:
            return True
            return False


if __name__=="__main__":
    game = Game()