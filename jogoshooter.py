import os, sys
dirpath = os.getcwd()
sys.path.append(dirpath)
if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)

import pygame
#import math
import random
from ship import player
from monsters import enemies
from shot import Shot
from save import SaveLoadSystem
#from buttons import Button

pygame.init()
print('Path to module:', pygame.__file__)
print(locals()['pygame'])

display = pygame.display.set_mode([840, 480])
pygame.display.set_caption("Shooter Game")
objectGroup = pygame.sprite.Group()


# sons
shotlaser = pygame.mixer.Sound("data/Laser Shot.wav")
# limitar fps
clock = pygame.time.Clock()
#botoes
start = pygame.image.load("data/button1.png").convert_alpha()
exit = pygame.image.load("data/button2.png").convert_alpha()

#sistema de save da pontuação
save = SaveLoadSystem(".save", "save_data")
#sistema de save da pontuação
totalscore = save.load_game_data(["totalscore"], [0])

click = False

def main_menu():

    background_menu = pygame.sprite.Sprite(objectGroup)
    background_menu.image = pygame.image.load("data/background_menu.png")
    background_menu.image = pygame.transform.scale(background_menu.image, [840, 480])
    background_menu.rect = background_menu.image.get_rect()

    objectGroup.update()
    objectGroup.draw(display)

    start_b = start.get_rect()
    exit_b = exit.get_rect()
    start_b.center = (210, 370)
    exit_b.center = (630, 370)
    # start_b = start.Rect(110, 370, 200, 70)
    # exit_b = exit.Rect(530, 370, 200, 70)
    display.blit(start, start_b)
    display.blit(exit, exit_b)

    # musica
    pygame.mixer.music.load("data/Nosferatu3.mp3")
    pygame.mixer.music.play(-1)

    # sistema de save da pontuação
    save = SaveLoadSystem(".save", "save_data")
    # sistema de save da pontuação
    totalscore = save.load_game_data(["totalscore"], [0])

    # pontuação total
    font = pygame.font.Font("freesansbold.ttf", 32)
    text2 = font.render("COINS: " + str(totalscore), True, (0, 0, 0))
    textRect2 = text2.get_rect()
    textRect2.center = (700, 20)

    gameloop = True
    while gameloop:
        clock.tick(60)
        mx, my = pygame.mouse.get_pos()

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save.save_game_data([totalscore], ["totalscore"])
                gameloop = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    if click == True:
                        print("mouse pressionado")
        if start_b.collidepoint((mx, my)):
            if click:
                game()
        if exit_b.collidepoint((mx, my)):
            if click:
                gameloop = False

        text2 = font.render("COINS: " + str(totalscore), True, (0, 0, 0))
        display.blit(text2, textRect2)
        pygame.display.update()


def game():
    background = pygame.sprite.Sprite(objectGroup)
    background.image = pygame.image.load("data/background.png")
    background.image = pygame.transform.scale(background.image, [840, 480])
    background.rect = background.image.get_rect()
    ship = player(objectGroup)
    shotGroup = pygame.sprite.Group()

    #pygame.mouse.set_visible(False)

    # musica
    pygame.mixer.music.load("data/Nosferatu1.mp3")
    pygame.mixer.music.load("data/Nosferatu2.mp3")
    pygame.mixer.music.play(-1)

    #pontuação
    score = 0
    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render("SCORE: " + str(score), True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (80, 20)

    # sistema de save da pontuação
    save = SaveLoadSystem(".save", "save_data")
    # sistema de save da pontuação
    totalscore = save.load_game_data(["totalscore"], [0])

    # pontuação total
    text2 = font.render("COINS: " + str(totalscore), True, (0, 0, 0))
    textRect2 = text2.get_rect()
    textRect2.center = (700, 20)

    timer = 20
    enemyGroup = pygame.sprite.Group()
    gameloop = True
    while gameloop:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save.save_game_data([totalscore], ["totalscore"])
                gameloop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    shotlaser.play()
                    newShot = Shot(objectGroup, shotGroup)
                    newShot.rect.center = ship.rect.center
        objectGroup.update()

        # imagem carregada
        objectGroup.draw(display)
        timer += 1
        if timer > 30:
            timer = 0
            if random.random() < 0.2:
                newEnemy = enemies(objectGroup, enemyGroup)
        colisions = pygame.sprite.spritecollide(ship, enemyGroup, False, pygame.sprite.collide_mask)

        if colisions:
            print("Game Over")
            gameloop = False

        hit = pygame.sprite.groupcollide(shotGroup, enemyGroup, True, True, pygame.sprite.collide_mask)
        if hit:
            point = 20
            score += point
            text = font.render("Score: " + str(score), True, (0, 0, 0))
            totalscore += (point//10)
            text2 = font.render("COINS: " + str(totalscore), True, (0, 0, 0))
            print(totalscore)
        # pontuação
        display.blit(text, textRect)
        display.blit(text2, textRect2)
        pygame.display.update()
    main_menu()
main_menu()
