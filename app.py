import pygame
import math
from random import randint
from player import Player
from virus import Virus
from bullet import Bullet
from score import Score
from pygame import mixer


class Game:
           
    RUNNING = True
    
    def __init__(self):
        
        #initialize the pygame
        pygame.init()

       #create your screen
        self.screen = pygame.display.set_mode((600, 470))

       #Background
        self.background = pygame.image.load('assets/background.jpg')

        #Background sound
        mixer.music.load('assets/audio/spacemusic.wav')
        mixer.music.play(-1)

        #Game over text
        self.font = pygame.font.Font('assets/fonts/flux.otf', 64)


       #add title and icon
        pygame.display.set_caption("Kill the Virus")
        self.icon = pygame.image.load('assets/transportation.png')

        pygame.display.set_icon(self.icon)

        self.init_elements()
 

    def run_game(self, player, virus, bullet, score):
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
                         if bullet.bullet_state == 'ready':
                             bullet.bullet_X = player.player_X
                             player.fire_bullet(self.screen, bullet)

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        player.player_X_change = 0
            
            #Move player
            player.move()
    
            for i in range(virus.number_of_viruses):
                
                if virus.virus_Y[i] > 300:
                    for j in range(virus.number_of_viruses):
                        virus.virus_Y[j] = 2000

                    self.game_over()
                    mixer.music.stop()
                    break

                #Move virus
                virus.move(i)
                
                #Handle collision
                collision = self.isCollision(virus.virus_X[i], virus.virus_Y[i], bullet.bullet_X, bullet.bullet_Y)
                if collision:
                    virus.dying_sound.play()
                    bullet.bullet_Y = 400
                    bullet.set_state('ready')
                    score.set_value(score.get_value() + 1)

                    virus.virus_X[i] = randint(0, 600)
                    virus.virus_Y[i] = randint(30, 200)

                virus.paint_virus(self.screen, virus.virus_X[i], virus.virus_Y[i], i)

            #Move bullet
            bullet.move()

            if bullet.bullet_state == 'fire':
               player.fire_bullet(self.screen, bullet)
               bullet.bullet_Y -= bullet.bullet_Y_change


            #display score
            score.show_score(self.screen)

            player.paint_player(self.screen, player.player_X, player.player_Y)
    
            pygame.display.update()
    
    def init_elements(self):
        player = Player()
        virus = Virus()
        bullet = Bullet()
        score = Score()

        self.run_game(player, virus, bullet, score)

    def isCollision(self, virus_X, virus_Y, bullet_X, bullet_Y):
        distance = math.sqrt((math.pow(virus_X - bullet_X,2)) + ( math.pow(virus_Y - bullet_Y,2)))
        if bullet_X == 250:
            return False

        if distance < 27:
            return True
        return False

    def game_over(self):
        over_text = self.font.render('GAME OVER ', True, (255, 255, 255))
        self.screen.blit(over_text, (150, 150))



if __name__=="__main__":
    game = Game()