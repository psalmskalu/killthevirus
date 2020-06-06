import pygame

class Bullet: 
        
    def __init__(self):
        self.bullet_image = pygame.image.load('assets/miscellaneous.png')
        self.bullet_X = 0
        self.bullet_Y = 400
        self.bullet_X_change = 1
        self.bullet_Y_change = 2
        self.bullet_state = 'ready'

    def set_state(self, state):
        self.bullet_state = state

    def move(self):
        if self.bullet_Y <= 0:
            self.bullet_Y = 400
            self.set_state('ready')
