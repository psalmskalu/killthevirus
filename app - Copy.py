import pygame
import math
from random import randint

#initialize the pygame
pygame.init()

#create your screen
screen = pygame.display.set_mode((400, 400))

#Background
background = pygame.image.load('assets/background.jpg')


#add title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('assets/transportation.png')

pygame.display.set_icon(icon)

score = 0

#player
player_image = pygame.image.load('assets/transportation.png')
player_X = 160
player_Y = 350
player_X_change = 0

# Enemy
enemy_image = []
enemy_X = []
enemy_Y = []
enemy_X_change = []
enemy_Y_change = []
number_of_enemies = 6

for i in range(number_of_enemies):
    enemy_image.append(pygame.image.load('assets/virus.png'))
    enemy_X.append(randint(0, 360))
    enemy_Y.append(randint(30, 100))
    enemy_X_change.append(1)
    enemy_Y_change.append(5)

'''
Bullet states
---------

1. Ready - you can't see the bullet on the screen
2. Fire - the bullet is currently moving
'''

# Bullet
bullet_image = pygame.image.load('assets/miscellaneous.png')
bullet_X = 0
bullet_Y = 200
bullet_X_change = 1
bullet_Y_change = 2
bullet_state = 'ready'

#Score
score_value = 0

def player(x, y):
    screen.blit(player_image, (x, y))

def enemy(x, y, i):
    screen.blit(enemy_image[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bullet_image, (x + 10, y + 10))

def isCollision(enemy_X, enemy_Y, bullet_X, bullet_Y):
    distance = math.sqrt((math.pow(enemy_X - bullet_X,2)) + ( math.pow(enemy_Y - bullet_Y,2)))
    if distance < 27:
        return True
    return False

'''
  Game Loop logic
'''
running = True
while running:

    # set screen background with RGB
    screen.fill((0, 0, 0))

    #Background
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_X_change = -3

            if event.key == pygame.K_RIGHT:
                player_X_change = 3

            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    bullet_X = player_X
                    fire_bullet(bullet_X, bullet_Y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_X_change = 0

            
    
    #Player movement
    player_X += player_X_change

    if player_X <= 0:
        player_X = 0
    elif player_X > 336:
        player_X = 336

    # Enemy movement
    for i in range(number_of_enemies):
        enemy_X[i] += enemy_X_change[i]

        if enemy_X[i] <= 0:
            enemy_X_change[i] = 1
            enemy_Y[i]  += enemy_Y_change[i]
        elif enemy_X[i] > 336:
            enemy_X[i] = -1
            enemy_Y[i] += enemy_Y_change[i]

        #Collision
        collision = isCollision(enemy_X[i], enemy_Y[i], bullet_X, bullet_Y)
        if collision:
            bullet_Y = 300
            bullet_state = 'ready'
            score += 1
            enemy_X[i] = randint(0, 360)
            enemy_Y[i] = randint(30, 100)

        enemy(enemy_X[i], enemy_Y[i], i)

    #bullet movement
    if bullet_Y <= 0:
        bullet_Y = 300
        bullet_state = 'ready'

    if bullet_state is 'fire':
        fire_bullet(bullet_X, bullet_Y)
        bullet_Y -= bullet_Y_change


    

    player(player_X, player_Y)
    
    pygame.display.update()
        
