import pygame


class Player:
    
    def __init__(self):
        self.player_image = pygame.image.load('assets/transportation.png')
        self.player_X = 160
        self.player_Y = 350
        self.player_X_change = 0

    def get_image(self):
        return self.player_image

    def paint_player(self, screen, x, y):
        screen.blit(self.player_image, (x, y))

    def fire_bullet(self, screen, bullet, x, y):
        bullet.set_state('fire')              
        screen.blit(bullet.bullet_image, (x + 10, y + 10))

    def move(self):
        
        self.player_X += self.player_X_change

        if self.player_X <= 0:
            self.player_X = 0
        elif self.player_X > 336:
            self.player_X = 336

