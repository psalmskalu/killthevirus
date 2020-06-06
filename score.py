import pygame


class Score:

    def __init__(self):
        self.value = 0
        self.X = 10
        self.Y = 10
        self.font = pygame.font.Font('assets/fonts/flux.otf', 32)

    def show_score(self, screen):
        score = self.font.render('Score : ' + str(self.value), True, (255, 255, 255))
        screen.blit(score, (self.X, self.Y))

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value
