import pygame
import sys
import sysconfig
import random
import math
from pygame import mixer
# intiliazin the  pygame
pygame.init()
# creating a  screen in python
screen = pygame.display.set_mode((750, 450))

# adding background
background = pygame.image.load('./spaceinvader/3.jpg')
background = pygame.transform.scale(background, (750, 450))
# adding background sound 
mixer.music.load('./spaceinvader/background.wav')
mixer.music.play(-1)

# creating title and icon
pygame.display.set_caption("Space Invadors")
icon = pygame.image.load('./spaceinvader/1.jpg')
icon = pygame.transform.scale(icon, (30, 30))
pygame.display.set_icon(icon)

#score font download in dafont website best website
score_val=0
font = pygame.font.Font("./spaceinvader/font.ttf",25)
textX=15
textY=20

def show_score(x,y):
    score=font.render("Score:"+str(score_val),True,(255,255,255))
    screen.blit(score,(x,y))

# game over 
over_text=pygame.font.Font("./spaceinvader/font.ttf",120)
game_textX=35
game_textY=155
def game_over_text(x,y):
    game_over=over_text.render("GAME OVER",True,(255,255,255))
    screen.blit(game_over,(x,y))
# Adding player
playerimg = pygame.image.load('./spaceinvader/battleship.png')
playerimg = pygame.transform.scale(playerimg, (65, 65))
playerX = 345
playerY = 350
playerchange_X = 0
playerchange_Y = 0

# adding enemy
enemyimglist= []
enemyX = []
enemyY = []
enemychange_X = []
enemychange_Y = []
no_of_enemies = 6
for i in range(no_of_enemies):
    enemyimg = pygame.image.load('./spaceinvader/4.png')
    enemyimg = pygame.transform.scale(enemyimg, (65, 65))
    enemyimglist.append(enemyimg)
    enemyX.append(random.randint(0, 685))
    enemyY.append(random.randint(50, 150))
    enemychange_X.append(0.3)
    enemychange_Y.append(35)

# adding bullet
# read-means not seen in loop or display
# fire-means seen according to fire function
bulletimg = pygame.image.load('./spaceinvader/bullets.png')
bulletimg = pygame.transform.scale(bulletimg, (20, 20))
bulletX = 0
bulletY = 350
bulletchage_x = 0
bulletchange_y = 1
bullet_state = "ready"

# collision


def iscollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX,2)+math.pow(enemyY-bulletY,2))
    if distance < 40:
        return True
    else:
        return False

# bullet method


def bullet_fire(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x+21, y+17))
# adding methods in game
# player methods


def player(x, y):
    screen.blit(playerimg, (x, y))  # used to draw image take two parameter


def enemy(x, y,i):
    screen.blit(enemyimglist[i], (x, y))


# game loop
running = True
while running:
    # doing event related coding
    # filling screen and updating it
    screen.fill((128, 128, 128))  # tuple is given in format in rgb type
    # movement mechanics of game in loop
    # playerX+=0.1
    # playerY-=0.1
    # adding background
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # creating a keystroke in event loop
        if event.type == pygame.KEYDOWN:
            # print("A keystroke is pressed")
            if event.key == pygame.K_LEFT:
                playerchange_X = -0.7
                # print("left arrow is pressed")
            if event.key == pygame.K_RIGHT:
                playerchange_X = 0.7
                # print("Right arrow is pressed")
            if event.key == pygame.K_UP:
                playerchange_Y = -0.2
                # print("up arrow is pressed")
            if event.key == pygame.K_DOWN:
                playerchange_Y = 0.2
                # print("Down arrow is pressed")
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound=mixer.Sound('./spaceinvader/laser.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    bullet_fire(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerchange_X = 0

    playerX += playerchange_X
    # playerY +=playerchange_Y
    # taking bordering
    if playerX <= 0:
        playerX = 0
    elif playerX >= 685:
        playerX = 685
    # playerY +=playerchange
    player(playerX, playerY)
    # enemy movement
    for i in range(no_of_enemies):
        enemyX[i] += enemychange_X[i]
        if enemyY[i]>= 280:
            for i in range(no_of_enemies):
                enemyY[i]=2000
            game_over_text(game_textX,game_textY)
            break
        if enemyX[i] <= 0:
            enemychange_X[i] = 0.4
            enemyY[i] += enemychange_Y[i]
        elif enemyX[i] >= 685:
            enemychange_X[i] = -0.4
            enemyY[i] += enemychange_Y[i]
        # collision calls
        collision = iscollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bullet_expolsion=mixer.Sound('./spaceinvader/explosion.wav')
            bullet_expolsion.play()
            bulletY = 350
            bullet_state = "ready"
            score_val += 1
            enemyX[i] = random.randint(0, 685)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i],i)
        
    # adding multiple bullet
    if bulletY <= 0:
        bulletY = 350
        bullet_state = "ready"
    # bullet movement
    if bullet_state is "fire":
        bullet_fire(bulletX, bulletY)
        bulletY -= bulletchange_y
    
    show_score(textX,textY)
    pygame.display.update()
