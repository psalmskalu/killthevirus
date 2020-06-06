from random import randint
import pygame

class Virus:

    virus_image = []
    virus_X = []
    virus_Y = []
    virus_X_change = []
    virus_Y_change = []
    number_of_viruses = 10

    def __init__(self):        
        for i in range(self.number_of_viruses):
            self.virus_image.append(pygame.image.load('assets/virus.png'))
            self.virus_X.append(randint(0, 560))
            self.virus_Y.append(randint(30, 100))
            self.virus_X_change.append(1)
            self.virus_Y_change.append(5)

    def paint_virus(self, screen, x, y, i):
        screen.blit(self.virus_image[i], (x, y))

    def move(self, i):
        self.virus_X[i] += self.virus_X_change[i]

        if self.virus_X[i] <= 0:
            self.virus_X_change[i] = 1
            self.virus_Y[i]  += self.virus_Y_change[i]
        elif self.virus_X[i] > 560:
            self.virus_X[i] = -1
            self.virus_Y[i] += self.virus_Y_change[i]


