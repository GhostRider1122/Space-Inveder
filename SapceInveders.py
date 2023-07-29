import pygame
import random
import math as m
from pygame import mixer

# initialize the pygame
pygame.init()

# create the screen
width = 800
height = 600
screen = pygame.display.set_mode((width, height))

# Caption and icon
pygame.display.set_caption("My First Game")
icon = pygame.image.load('assets/icons/game_icon.png')
pygame.display.set_icon(icon)

# Background
bg_img = pygame.image.load('assets/icons/background.jpg')
bg_img = pygame.transform.scale(bg_img, (width, height))

# Music and sound effects
mixer.music.load('assets/sounds/bgm.mp3')
mixer.music.play(-1)

# SpaceShip
playerImg = pygame.image.load('assets/icons/spaceship.png')
playerX = 360
playerY = 500
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemy = 6

for i in range(num_of_enemy):
    enemyImg.append(pygame.image.load('assets/icons/enemy.png'))
    enemyX.append(random.randint(0, width - 65))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.3)
    enemyY_change.append(40)

# bullet
# Ready - You can't see the bullet on the screen
# Fire -  Bullet is currently moving
bulletImg = pygame.image.load('assets/icons/bullet.png')
bulletX = 0
bulletY = 500
bulletX_change = 0
bulletY_change = 1
bullet_state = "ready"


# player function to draw the spaceship on the screen surface
def player(x, y):
    screen.blit(playerImg, (x, y))


# enemy function to draw the enemy on the screen surface
def enemy(x, y, index):
    screen.blit(enemyImg[index], (x, y))


# bullet function to fire the bullet
def bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y - 16))


# collision detection function
def isCollision(x1, y1, x2, y2):
    dist = m.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
    if dist <= 27:
        return True
    return False


# score
score = 0

font = pygame.font.Font(None, 36)


def display_score():
    score_text = font.render("Score: " + str(score), True, (0, 255, 0))
    screen.blit(score_text, (10, 10))


over_font = pygame.font.Font(None, 128)


def game_over():
    game_over_text = over_font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(game_over_text, (150, 250))


j = 0
# Game Loop
loop = True
while loop:

    # Change the background colour
    screen.fill((0, 0, 0))
    screen.blit(bg_img, (0, j))
    screen.blit(bg_img, (0, j - height))

    if j == height:
        screen.blit(bg_img, (0, j - height))
        j = 0
    j += .5

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                loop = False

        # if a key is pressed check if pressed key is left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerX_change = -0.4
            if event.key == pygame.K_d:
                playerX_change = 0.4

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if bullet_state == "ready":
                bullet_sound = mixer.Sound('assets/sounds/shoot.wav')
                mixer.Sound.play(bullet_sound)

                bulletX = playerX
                bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0

    playerX += playerX_change

    # conditions so that spaceship does not leave the screen boundary
    # as the spaceship img is 64 pixels so 64 is subtracted from the width of screen
    if playerX <= 0:
        playerX = 0
    if playerX >= width - 64:
        playerX = width - 64

    # change the direction of enemy if it hits the boundary
    for i in range(num_of_enemy):

        # Game over
        if enemyY[i] > 480:
            for j in range(num_of_enemy):
                enemyY[j] = 2000
            playerX, playerY = 2000, 2000
            game_over()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        if enemyX[i] >= width - 64:
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]

        # collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 500
            bullet_state = "ready"
            score += 1
            enemyX[i] = random.randint(0, width - 65)
            enemyY[i] = random.randint(50, 150)

            explosion_sound = mixer.Sound('assets/sounds/invaderkilled.wav')
            mixer.Sound.play(explosion_sound)

        enemy(enemyX[i], enemyY[i], i)

    # bullet movement
    if bullet_state == "fire":
        bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    if bulletY <= 0:
        bulletY = 500
        bullet_state = "ready"

    player(playerX, playerY)
    display_score()

    pygame.display.update()

pygame.quit()
