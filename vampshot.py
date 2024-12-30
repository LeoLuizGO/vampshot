import os, sys
dirpath = os.getcwd()
sys.path.append(dirpath)
if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)

import pygame
import random
from ship import player, player2, player3, player4, Shipsos, Shot3
from monsters import enemies, enemy3, boss
from shot import Shot, Enemyshot
from save import SaveLoadSystem
from life import hearts, heartsoff, heartdrop
from drop import speeddrop, Coindrop, Scoredrop, Shotdrop
from speedbuff import sbuff, Shotbuff


pygame.init()
# print('Path to module:', pygame.__file__)
# print(locals()['pygame'])

display = pygame.display.set_mode([840, 480])
pygame.display.set_caption("VampShot")
objectGroup = pygame.sprite.Group()
shopGroup = pygame.sprite.Group()
icon = pygame.image.load('data/enemy1.png')
pygame.display.set_icon(icon)

# sons
vampirehiss = pygame.mixer.Sound("data/vampirehiss.mp3")
vampire2 = pygame.mixer.Sound("data/vampire2.mp3")
vampire3 = pygame.mixer.Sound("data/vampire3.mp3")
shotlaser = pygame.mixer.Sound("data/Laser Shot.wav")
impacto = pygame.mixer.Sound("data/Explosion_Impact.wav")
helpme = pygame.mixer.Sound("data/helpmesound.mp3")
pygame.mixer.Sound.set_volume(impacto, 0.2)
# limitar fps
clock = pygame.time.Clock()
#botoes
start = pygame.image.load("data/button1.png").convert_alpha()
exit = pygame.image.load("data/button2.png").convert_alpha()
about = pygame.image.load("data/button3.png").convert_alpha()
savebutton = pygame.image.load("data/button4.png").convert_alpha()
menu = pygame.image.load("data/menu.png").convert_alpha()
delete = pygame.image.load("data/button5.png").convert_alpha()
yes = pygame.image.load("data/buttonyes.png").convert_alpha()
no = pygame.image.load("data/buttonno.png").convert_alpha()
shop = pygame.image.load("data/shopbutton.png").convert_alpha()
shopbg = pygame.image.load("data/shopbg.png").convert_alpha()
use = pygame.image.load("data/buttonuse.png").convert_alpha()
resume = pygame.image.load("data/buttonresume.png").convert_alpha()
pause = pygame.image.load("data/pausepause.png").convert_alpha()
retry = pygame.image.load("data/buttonretry.png").convert_alpha()
#buttongen = pygame.image.load("data/buttongen.png").convert_alpha()

#about
aboutdisplay = pygame.image.load("data/about.png").convert_alpha()

#sistema de save da pontuação
save = SaveLoadSystem(".save", "save_data")
#sistema de save da pontuação
totalscore, shopverif, skin = save.load_game_data(["totalscore", "shopverif", "skin"], [0, [0, 0, 0, 0], 1])


click = False


def main_menu():
    pygame.init()
    #print("skin no verfif3: %d", skin)
    background_menu = pygame.sprite.Sprite(objectGroup)
    background_menu.image = pygame.image.load("data/background_menu.png")
    background_menu.image = pygame.transform.scale(background_menu.image, [840, 480])
    background_menu.rect = background_menu.image.get_rect()

    objectGroup.update()
    objectGroup.draw(display)

    start_b = start.get_rect()
    exit_b = exit.get_rect()
    about_b = about.get_rect()
    savebutton_b = savebutton.get_rect()
    shop_b = shop.get_rect()

    start_b.center = (100, 370)
    about_b.center = (310, 370)
    savebutton_b.center = (520, 370)
    exit_b.center = (730, 370)
    #shop_b.size = (40, 40)
    shop_b.center = (775, 55)

    # start_b = start.Rect(110, 370, 200, 70)
    # exit_b = exit.Rect(530, 370, 200, 70)
    display.blit(start, start_b)
    display.blit(exit, exit_b)
    display.blit(about, about_b)
    display.blit(savebutton, savebutton_b)
    display.blit(shop, shop_b)

    # musica
    pygame.mixer.music.load("data/Nosferatu3.mp3")
    pygame.mixer.music.set_volume(0.1) #----------------volume
    pygame.mixer.music.play(-1)

    # sistema de save da pontuação
    save = SaveLoadSystem(".save", "save_data")
    # sistema de save da pontuação
    totalscore = save.load_game_data(["totalscore"], [0])

    # pontuação total
    font = pygame.font.Font("freesansbold.ttf", 32)
    text2 = font.render("COINS: " + str(totalscore), True, (0, 0, 0))
    textRect2 = text2.get_rect()
    textRect2.x = 5
    textRect2.y = 5
    #textRect2.center = (125, 20)


    gameloop = True
    while gameloop:
        clock.tick(60)
        mx, my = pygame.mouse.get_pos()

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #save.save_game_data([totalscore], ["totalscore"])
                pygame.quit()
                gameloop = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    # if click == True:
                        # print("mouse pressionado")
        if start_b.collidepoint((mx, my)):
            if click:
                game()
        if exit_b.collidepoint((mx, my)):
            if click:
                gameloop = False
        if about_b.collidepoint((mx, my)):
            if click:
                aboutd()
        if savebutton_b.collidepoint((mx, my)):
            if click:
                saved()
        if shop_b.collidepoint((mx, my)):
            if click:
                shop_menu()
        text2 = font.render("COINS: " + str(totalscore), True, (0, 0, 0))
        display.blit(text2, textRect2)
        pygame.display.update()
    save.save_game_data([totalscore], ["totalscore"])
    pygame.quit()
    sys.exit()


def game():
    pygame.init()
    background = pygame.sprite.Sprite(objectGroup)
    background.image = pygame.image.load("data/background.png")
    background.image = pygame.transform.scale(background.image, [840, 480])
    background.rect = background.image.get_rect()
    # sistema de save da pontuação
    save = SaveLoadSystem(".save", "save_data")
    # sistema de save da pontuação
    skin = save.load_game_data(["skin"], [1])

    if skin == 1:
        ship = player(objectGroup)
    elif skin == 2:
        ship = player2(objectGroup)
    elif skin == 3:
        ship = player3(objectGroup)
    elif skin == 4:
        ship = player4(objectGroup)
    tripleshot = False


    shotGroup = pygame.sprite.Group()

    #vida
    life = 3
    heartoff = heartsoff(objectGroup)
    heartoff.rect.center = [380, 20]
    heartoff2 = heartsoff(objectGroup)
    heartoff2.rect.center = [420, 20]
    heartoff3 = heartsoff(objectGroup)
    heartoff3.rect.center = [460, 20]

    heart = hearts(objectGroup)
    heart.rect.center = [380, 20]
    heart2 = hearts(objectGroup)
    heart2.rect.center = [420, 20]
    heart3 = hearts(objectGroup)
    heart3.rect.center = [460, 20]


    # musica
    pygame.mixer.music.load("data/Nosferatu1.mp3")
    pygame.mixer.music.load("data/Nosferatu2.mp3")
    pygame.mixer.music.play(-1)

    #pontuação
    score = 0
    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render("SCORE: " + str(score), True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (80, 50)

    # sistema de save da pontuação
    save = SaveLoadSystem(".save", "save_data")
    # sistema de save da pontuação
    totalscore = save.load_game_data(["totalscore"], [0])

    # pontuação total
    text2 = font.render("COINS: " + str(totalscore), True, (0, 0, 0))
    textRect2 = text2.get_rect()
    textRect2.x = 5
    textRect2.y = 5

    timer = 20
    timerspeed = 0
    timershot = 0
    #grupos que serão úteis
    enemyGroup = pygame.sprite.Group()
    dropGroup = pygame.sprite.Group()
    shotenemyGroup = pygame.sprite.Group()
    bossGroup = pygame.sprite.Group()
    healthbar = pygame.sprite.Group()
    buffgroup = pygame.sprite.Group()
    sosGroup = pygame.sprite.Group()
    shotdropGroup = pygame.sprite.Group()
    #resgatar funções na classe boss:
    Boss = boss()
    Boss2 = boss()
    Boss3 = boss()

    gameloop = True
    speed = 5
    speedd = False
    while gameloop:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                pygame.quit()
                gameloop = False
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    shotlaser.play()
                    newShot = Shot(objectGroup, shotGroup)
                    newShot.rect.center = ship.rect.center
                    if tripleshot:
                        newShot2 = Shot(objectGroup, shotGroup)
                        newShot2.rect.centerx = ship.rect.centerx
                        newShot2.rect.y = (ship.rect.centery + 20)
                        newShot3 = Shot(objectGroup, shotGroup)
                        newShot3.rect.centerx = ship.rect.centerx
                        newShot3.rect.y = (ship.rect.centery - 30)
                if event.key == pygame.K_ESCAPE:
                    # print("foi esc clicado")
                    save.save_game_data([totalscore], ["totalscore"])
                    pause_menu()

        if tripleshot:

            for _ in shotdropGroup:
                if len(shotdropGroup) == 1:
                    newtripleshot.kill()
            newtripleshot = Shot3(objectGroup, shotdropGroup)
            newtripleshot.rect.center = ship.rect.center

            #print(len(shotdropGroup))
            #print(shotdropGroup)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            ship.rect.x += speed
            if tripleshot:
                newtripleshot.rect.x += speed
        elif keys[pygame.K_a]:
            ship.rect.x -= speed
            if tripleshot:
                newtripleshot.rect.x -= speed
        elif keys[pygame.K_w]:
            ship.rect.y -= speed
            if tripleshot:
                newtripleshot.rect.y -= speed
        elif keys[pygame.K_s]:
            ship.rect.y += speed
            if tripleshot:
                newtripleshot.rect.y += speed

        objectGroup.update()
        # imagem carregada
        objectGroup.draw(display)

        timershot += 1
        timerspeed += 1
        timer += 1
        if score < 500:
            if timer > 30:
                timer = 0
                if random.random() < 0.3:
                    newEnemy = enemies(objectGroup, enemyGroup)
        elif score >= 500 and score < 2000:                                   #valor que aparece novo inimigo
            if timer > 20:
                timer = 0
                if random.random() < 0.2:
                    newEnemy = enemy3(objectGroup, enemyGroup)
                if random.random() < 0.1:
                    newEnemy = enemies(objectGroup, enemyGroup)
                if random.random() < 0.01:
                    newshipsos = Shipsos(objectGroup, sosGroup)
                    helpme.play()
        elif score >= 2000 and score < 3000 and len(enemyGroup.sprites()) == 0 and len(bossGroup.sprites()) == 0:
            vampirehiss.play()
            lifeboss = 180
            newEnemyboss = boss(objectGroup, bossGroup)
            start_time = pygame.time.get_ticks()
            #vida do boss -----------------------------------------------
            Boss3.hit()
            boshbbinner = Boss2.healthbarinner(objectGroup, healthbar)
            boshbb = Boss.healthbarboss(objectGroup, healthbar)
            objectGroup.update()
            healthbar.update()
        elif score >= 2000 and score < 3000 and len(bossGroup.sprites()) == 1:
            current_time = pygame.time.get_ticks()
            timespan = 5000
            time = False
            if current_time > start_time + timespan:
                time = True
            if timer > 20 and time == True:
                timer = 0
                if random.random() < 0.8:
                    enemyshot = Enemyshot(objectGroup, shotenemyGroup)
                    enemyshot2 = Enemyshot(objectGroup, shotenemyGroup)
                    enemyshot.rect.center = [580, 90]
                    enemyshot2.rect.center = [610, 160]
                #tiros do boss aqui ------------------------------------

            shotenemyGroup.update()
        objectGroup.update()

        colisionboss1 = pygame.sprite.spritecollide(ship, shotenemyGroup, True, pygame.sprite.collide_mask)
        colisionbossship = pygame.sprite.spritecollide(ship, bossGroup, False, pygame.sprite.collide_mask)
        colisionshipsos = pygame.sprite.spritecollide(ship, sosGroup, True, pygame.sprite.collide_mask)
        colisionshotsos = pygame.sprite.groupcollide(shotGroup, sosGroup, True, True, pygame.sprite.collide_mask)
        colisionbossshot = pygame.sprite.groupcollide(shotGroup, bossGroup, True, False, pygame.sprite.collide_mask)
        colisionshotshot = pygame.sprite.groupcollide(shotGroup, shotenemyGroup, True, True, pygame.sprite.collide_mask)


        colisions = pygame.sprite.spritecollide(ship, enemyGroup, True, pygame.sprite.collide_mask)

        if colisionbossshot:
            if lifeboss >= 3:
                lifeboss -= 3
                Boss3.hit()
                healthbar.update()
                objectGroup.update()
                boshbbinnerB = Boss2.healthbarinner(objectGroup, healthbar)

            else:
                score += 1000
                text = font.render("SCORE: " + str(score), True, (0, 0, 0))
                totalscore += 500
                text2 = font.render("COINS: " + str(totalscore), True, (0, 0, 0))
                newEnemyboss.kill()
                save.save_game_data([totalscore], ["totalscore"])
                win_menu()
        #lógica vida do player-------------------------------------------
        if colisionbossship:
            impacto.play()
            if life == 3:
                ship.rect.center = (200, 240)
                life -= 1
                heart3.kill()
            elif life == 2:
                ship.rect.center = (200, 240)
                life -= 1
                heart2.kill()
            elif life == 1:
                ship.rect.center = (200, 240)
                life -= 1
                heart.kill()
                save.save_game_data([totalscore], ["totalscore"])
                gameloop = False
                gameover_menu()
        if colisions or colisionboss1:
            impacto.play()
            if life == 3:
                life -= 1
                heart3.kill()
            elif life == 2:
                life -= 1
                heart2.kill()
            elif life == 1:
                life -= 1
                heart.kill()
                save.save_game_data([totalscore], ["totalscore"])
                gameover_menu()     #tela gameover
                gameloop = False
        if colisionshipsos:
            totalscore += 100
            text2 = font.render("COINS: " + str(totalscore), True, (0, 0, 0))
            score += 100
            text = font.render("SCORE: " + str(score), True, (0, 0, 0))
            if life == 3:
                pass
            elif life == 2:
                life += 1
                heart3 = hearts(objectGroup)
                heart3.rect.center = [460, 20]
            elif life == 1:
                life += 1
                heart2 = hearts(objectGroup)
                heart2.rect.center = [420, 20]
        if colisionshotsos:
            impacto.play()
            if life == 3:
                life -= 1
                heart3.kill()
            elif life == 2:
                life -= 1
                heart2.kill()
            elif life == 1:
                life -= 1
                heart.kill()
                gameloop = False
                save.save_game_data([totalscore], ["totalscore"])
                gameover_menu()
        hit = pygame.sprite.groupcollide(shotGroup, enemyGroup, True, True, pygame.sprite.collide_mask)
        if hit:
            point = 20
            score += point
            text = font.render("SCORE: " + str(score), True, (0, 0, 0))
            totalscore += (point//10)
            text2 = font.render("COINS: " + str(totalscore), True, (0, 0, 0))
            if random.random() < 0.5:
                if random.random() < 0.10:
                    for enemy in hit:
                        heartsdrop = heartdrop(objectGroup, dropGroup)
                        heartsdrop.rect.center = enemy.rect.center
                elif random.random() < 0.10:
                    for enemy in hit:
                        speedsdrop = speeddrop(objectGroup, dropGroup)
                        speedsdrop.rect.center = enemy.rect.center
                elif random.random() < 0.10:
                    for enemy in hit:
                        scoredrop = Scoredrop(objectGroup, dropGroup)
                        scoredrop.rect.center = enemy.rect.center
                elif random.random() < 0.10:
                    for enemy in hit:
                        coindrop = Coindrop(objectGroup, dropGroup)
                        coindrop.rect.center = enemy.rect.center
                elif random.random() < 0.35:
                    for enemy in hit:
                        shotdrop = Shotdrop(objectGroup, dropGroup)
                        shotdrop.rect.center = enemy.rect.center

            # print(totalscore)

        colisiondrop = pygame.sprite.spritecollide(ship, dropGroup, True, pygame.sprite.collide_mask)

        if colisiondrop:
            colisiondropp = str(colisiondrop)
            colisiondrop = list(colisiondrop)
            colisiondrop[0] = str(colisiondrop[0])
            colisiondropp = colisiondrop[0]
            colisiondropp = list(colisiondropp)
            colisiondropp.remove(colisiondropp[0])
            for i in range(0, len(colisiondropp)):
                if " " in colisiondropp[i]:
                    marc = i
                    rescolision = (("".join(colisiondropp[0:marc])))
                    break
            # print(rescolision)
            if rescolision == 'heartdrop':
                if life == 3:
                    pass
                elif life == 2:
                    life += 1
                    heart3 = hearts(objectGroup)
                    heart3.rect.center = [460, 20]
                elif life == 1:
                    life += 1
                    heart2 = hearts(objectGroup)
                    heart2.rect.center = [420, 20]
            elif rescolision == 'speeddrop':
                Speedbuff = sbuff(objectGroup, buffgroup)
                speed = 10
                speedd = True
                #print("aiaiai")
                timerspeed = 0
            elif rescolision == 'Coindrop':
                totalscore += 100
                text2 = font.render("COINS: " + str(totalscore), True, (0, 0, 0))
            elif rescolision == 'Scoredrop':
                score += 100
                text = font.render("SCORE: " + str(score), True, (0, 0, 0))
            elif rescolision == "Shotdrop":
                shotbuff = Shotbuff(objectGroup, buffgroup)
                tripleshot = True
                shott = True
                timershot = 0
        if speedd == True and timerspeed > 900:
            timerspeed = 0
            speedd = False
            speed = 5
        if tripleshot == True and timershot > 900:
            timershot = 0
            newtripleshot.kill()
            tripleshot = False


        # pontuação
        display.blit(text, textRect)
        display.blit(text2, textRect2)
        pygame.display.update()
    save.save_game_data([totalscore], ["totalscore"])
    main_menu()


def aboutd():
    pygame.init()
    background = pygame.sprite.Sprite(objectGroup)
    background.image = pygame.image.load("data/background.png")
    background.image = pygame.transform.scale(background.image, [840, 480])
    background.rect = background.image.get_rect()

    # sistema de save da pontuação
    save = SaveLoadSystem(".save", "save_data")
    totalscore = save.load_game_data(["totalscore"], [0])

    objectGroup.update()
    objectGroup.draw(display)

    # pontuação total
    font = pygame.font.Font("freesansbold.ttf", 32)
    text2 = font.render("COINS: " + str(totalscore), True, (0, 0, 0))
    textRect2 = text2.get_rect()
    textRect2.x = 5
    textRect2.y = 5

    aboutdisplay_d = aboutdisplay.get_rect()
    aboutdisplay_d.center = (420, 240)

    menu_b = menu.get_rect()
    menu_b.center = (740, 400)

    display.blit(text2, textRect2)
    display.blit(aboutdisplay, aboutdisplay_d)
    display.blit(menu, menu_b)
    aboutloop = True
    while aboutloop == True:
        clock.tick(60)
        mx, my = pygame.mouse.get_pos()

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                aboutloop = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    # if click == True:
                        # print("mouse pressionado")
            if menu_b.collidepoint((mx, my)):
                if click:
                    main_menu()
        pygame.display.update()


def saved():
    background = pygame.sprite.Sprite(objectGroup)
    background.image = pygame.image.load("data/background.png")
    background.image = pygame.transform.scale(background.image, [840, 480])
    background.rect = background.image.get_rect()

    # sistema de save da pontuação
    save = SaveLoadSystem(".save", "save_data")
    totalscore = save.load_game_data(["totalscore"], [0])

    objectGroup.update()
    objectGroup.draw(display)

    # pontuação total
    font = pygame.font.Font("freesansbold.ttf", 32)
    text2 = font.render("COINS: " + str(totalscore), True, (0, 0, 0))
    textRect2 = text2.get_rect()
    textRect2.x = 5
    textRect2.y = 5

    menu_b = menu.get_rect()
    menu_b.center = (740, 400)
    deleterect = delete.get_rect()
    deleterect.center = (420, 240)

    display.blit(text2, textRect2)
    display.blit(menu, menu_b)
    display.blit(delete, deleterect)
    saveloop = True
    while saveloop == True:
        clock.tick(60)
        mx, my = pygame.mouse.get_pos()

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                pygame.quit()
                saveloop = False
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    # if click == True:
                        # print("mouse pressionado")
            if menu_b.collidepoint((mx, my)):
                if click:
                    main_menu()
            if deleterect.collidepoint((mx, my)):
                if click:
                    delete_menu()
        pygame.display.update()


def delete_menu():
    background = pygame.sprite.Sprite(objectGroup)
    background.image = pygame.image.load("data/background.png")
    background.image = pygame.transform.scale(background.image, [840, 480])
    background.rect = background.image.get_rect()

    objectGroup.update()
    objectGroup.draw(display)

    # sistema de save da pontuação
    save = SaveLoadSystem(".save", "save_data")
    totalscore, shopverif, skin = save.load_game_data(["totalscore", "shopverif", "skin"], [0, [0, 0, 0, 0], 1])
    # pontuação total
    font = pygame.font.Font("freesansbold.ttf", 32)
    text2 = font.render("COINS: " + str(totalscore), True, (0, 0, 0))
    textRect2 = text2.get_rect()
    textRect2.x = 5
    textRect2.y = 5
    confirmtext = font.render("Are you sure?", True, (0, 0, 0))
    confirmtextrect = confirmtext.get_rect()
    confirmtextrect.center = (400, 180)
    menu_b = menu.get_rect()
    menu_b.center = (740, 400)
    yesrect = yes.get_rect()
    yesrect.center = (240, 320)
    norect = no.get_rect()
    norect.center = (540, 320)

    display.blit(text2, textRect2)
    display.blit(menu, menu_b)
    display.blit(yes, yesrect)
    display.blit(no, norect)
    display.blit(confirmtext, confirmtextrect)
    deleteloop = True
    while deleteloop == True:
        clock.tick(60)
        mx, my = pygame.mouse.get_pos()

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                pygame.quit()
                deleteloop = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if menu_b.collidepoint((mx, my)):
                if click:
                    main_menu()
            if yesrect.collidepoint((mx, my)):
                if click:
                    totalscore = 0
                    shopverif[1] = 0
                    shopverif[2] = 0
                    shopverif[3] = 0
                    skin = 1
                    #print("foi clicado")
                    save.save_game_data([totalscore], ["totalscore"])
                    save.save_game_data([shopverif], ["shopverif"])
                    save.save_game_data([skin], ["skin"])
                    text2 = font.render("COINS: " + str(totalscore), True, (0, 0, 0))
                    display.blit(text2, textRect2)
                    deleteloop = False
                    saved()
            if norect.collidepoint((mx, my)):
                if click:
                    deleteloop = False
                    saved()
        pygame.display.update()


def shop_menu():
    background = pygame.sprite.Sprite(objectGroup)
    background.image = pygame.image.load("data/background.png")
    background.image = pygame.transform.scale(background.image, [840, 480])
    background.rect = background.image.get_rect()
    # sistema de save da pontuação
    save = SaveLoadSystem(".save", "save_data")
    totalscore, shopverif, skin = save.load_game_data(["totalscore", "shopverif", "skin"], [0, [0, 0, 0, 0], 1])

    # pontuação total
    font = pygame.font.Font("freesansbold.ttf", 32)
    text2 = font.render("COINS: " + str(totalscore), True, (0, 0, 0))
    textRect2 = text2.get_rect()
    textRect2.x = 5
    textRect2.y = 5
    buttongen = pygame.sprite.Sprite(shopGroup)
    buttongen.image = pygame.image.load("data/buttongen.png")
    buttongen.image = pygame.transform.scale(buttongen.image, [170, 120])
    buttongen.rect = buttongen.image.get_rect()
    buttongen.rect.center = (210, 150)

    buttongen1 = pygame.sprite.Sprite(shopGroup)
    buttongen1.image = pygame.image.load("data/buttongen.png")
    buttongen1.image = pygame.transform.scale(buttongen1.image, [170, 120])
    buttongen1.rect = buttongen1.image.get_rect()
    buttongen1.rect.center = (210, 300)

    buttongen2 = pygame.sprite.Sprite(shopGroup)
    buttongen2.image = pygame.image.load("data/buttongen.png")
    buttongen2.image = pygame.transform.scale(buttongen1.image, [170, 120])
    buttongen2.rect = buttongen1.image.get_rect()
    buttongen2.rect.center = (500, 150)

    buttongen3 = pygame.sprite.Sprite(shopGroup)
    buttongen3.image = pygame.image.load("data/buttongen.png")
    buttongen3.image = pygame.transform.scale(buttongen1.image, [170, 120])
    buttongen3.rect = buttongen1.image.get_rect()
    buttongen3.rect.center = (500, 300)

    if shopverif[1] == 0:
        buy = pygame.sprite.Sprite(shopGroup)
        buy.image = pygame.image.load("data/buttonbuy.png")
        buy.image = pygame.transform.scale(buy.image, [110, 55])
        buy.rect = buy.image.get_rect()
        buy.rect.center = (350, 320)
    if shopverif[2] == 0:
        buy2 = pygame.sprite.Sprite(shopGroup)
        buy2.image = pygame.image.load("data/buttonbuy.png")
        buy2.image = pygame.transform.scale(buy2.image, [110, 55])
        buy2.rect = buy2.image.get_rect()
        buy2.rect.center = (640, 170)
    if shopverif[3] == 0:
        buy3 = pygame.sprite.Sprite(shopGroup)
        buy3.image = pygame.image.load("data/buttonbuy.png")
        buy3.image = pygame.transform.scale(buy3.image, [110, 55])
        buy3.rect = buy3.image.get_rect()
        buy3.rect.center = (640, 320)

    objectGroup.update()
    objectGroup.draw(display)

    font2 = pygame.font.Font("freesansbold.ttf", 16)
    # preço 1
    textprice = font2.render("500 COINS", True, (0, 0, 0))
    textRectprice = textprice.get_rect()
    textRectprice.centerx = 350
    textRectprice.centery = 270
    #preço 2
    textprice2 = font2.render("1500 COINS", True, (0, 0, 0))
    textRectprice2 = textprice2.get_rect()
    textRectprice2.centerx = 640
    textRectprice2.centery = 120
    #preço 3
    textprice3 = font2.render("10000 COINS", True, (0, 0, 0))
    textRectprice3 = textprice3.get_rect()
    textRectprice3.centerx = 640
    textRectprice3.centery = 270

    ship = player(shopGroup)
    ship.rect.center = (200, 150)

    ship2 = player2(shopGroup)
    ship2.rect.center = (200, 300)

    ship3 = player3(shopGroup)
    ship3.rect.center = (490, 150)

    ship4 = player4(shopGroup)
    ship4.rect.center = (490, 300)

    use_b = use.get_rect()
    use_b.center = (350, 300)
    use_b2 = use.get_rect()
    use_b2.center = (350, 150)
    use_b3 = use.get_rect()
    use_b3.center = (640, 150)
    use_b4 = use.get_rect()
    use_b4.center = (640, 300)
    shopbgdisplay = shopbg.get_rect()
    shopbgdisplay.center = (420, 240)
    menu_b = menu.get_rect()
    menu_b.center = (740, 400)

    display.blit(text2, textRect2)
    display.blit(shopbg, shopbgdisplay)
    display.blit(menu, menu_b)
    display.blit(use, use_b2)
    if shopverif[1] == 0:
        display.blit(textprice, textRectprice)
    elif shopverif[1] == 1:
        display.blit(use, use_b)
    if shopverif[2] == 0:
        display.blit(textprice2, textRectprice2)
    elif shopverif[2] == 1:
        display.blit(use, use_b3)
    if shopverif[3] == 0:
        display.blit(textprice3, textRectprice3)
    elif shopverif[3] == 1:
        display.blit(use, use_b4)

    shopGroup.update()
    shopGroup.draw(display)

    shoploop = True
    while shoploop == True:
        clock.tick(60)
        mx, my = pygame.mouse.get_pos()

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save.save_game_data([totalscore], ["totalscore"])
                save.save_game_data([shopverif], ["shopverif"])
                save.save_game_data([skin], ["skin"])
                pygame.quit()
                shoploop = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if menu_b.collidepoint((mx, my)):
                if click:
                    shoploop = False
                    main_menu()
            if use_b2.collidepoint((mx, my)):
                if click:
                    # print("chegou no use")
                    skin = 1
                    save.save_game_data([skin], ["skin"])
            if shopverif[1] == 0:
                if buy.rect.collidepoint((mx, my)):
                    if click:
                        if totalscore - 500 >= 0:
                            totalscore -= 500
                            shopverif[1] = 1
                            # print("foi clicado")
                            save.save_game_data([totalscore], ["totalscore"])
                            save.save_game_data([shopverif], ["shopverif"])
                            text2 = font.render("COINS: " + str(totalscore), True, (0, 0, 0))
                            objectGroup.draw(display)
                            display.blit(text2, textRect2)
                            display.blit(shopbg, shopbgdisplay)
                            display.blit(menu, menu_b)
                            display.blit(use, use_b2)
                            shopGroup.draw(display)
                            display.blit(text2, textRect2)
                            display.blit(use, use_b)
                            buy.kill()
                            if shopverif[2] == 0:
                                display.blit(textprice2, textRectprice2)
                            elif shopverif[2] == 1:
                                display.blit(use, use_b3)
                            if shopverif[3] == 0:
                                display.blit(textprice3, textRectprice3)
                            elif shopverif[3] == 1:
                                display.blit(use, use_b4)
                        else:
                            pass

            if shopverif[1] == 1:
                objectGroup.draw(display)
                display.blit(text2, textRect2)
                display.blit(shopbg, shopbgdisplay)
                display.blit(menu, menu_b)
                display.blit(use, use_b2)
                shopGroup.draw(display)
                display.blit(text2, textRect2)
                display.blit(use, use_b)
                if shopverif[2] == 0:
                    display.blit(textprice2, textRectprice2)
                elif shopverif[2] == 1:
                    display.blit(use, use_b3)
                if shopverif[3] == 0:
                    display.blit(textprice3, textRectprice3)
                elif shopverif[3] == 1:
                    display.blit(use, use_b4)
                if use_b.collidepoint((mx, my)):
                    if click:
                        # print("chegou aqui")
                        skin = 2
                        save.save_game_data([skin], ["skin"])
            if shopverif[2] == 0:
                if buy2.rect.collidepoint((mx, my)):
                    if click:
                        if totalscore - 1500 >= 0:
                            totalscore -= 1500
                            shopverif[2] = 1
                            # print("foi clicado")
                            save.save_game_data([totalscore], ["totalscore"])
                            save.save_game_data([shopverif], ["shopverif"])
                            text2 = font.render("COINS: " + str(totalscore), True, (0, 0, 0))
                            objectGroup.draw(display)
                            display.blit(text2, textRect2)
                            display.blit(shopbg, shopbgdisplay)
                            display.blit(menu, menu_b)
                            display.blit(use, use_b2)
                            shopGroup.draw(display)
                            display.blit(text2, textRect2)
                            display.blit(use, use_b3)
                            buy2.kill()
                            if shopverif[1] == 0:
                                display.blit(textprice, textRectprice)
                            elif shopverif[1] == 1:
                                display.blit(use, use_b)
                            if shopverif[3] == 0:
                                display.blit(textprice3, textRectprice3)
                            elif shopverif[3] == 1:
                                display.blit(use, use_b4)
                        else:
                            pass

            if shopverif[2] == 1:
                objectGroup.draw(display)
                display.blit(text2, textRect2)
                display.blit(shopbg, shopbgdisplay)
                display.blit(menu, menu_b)
                display.blit(use, use_b2)
                shopGroup.draw(display)
                display.blit(text2, textRect2)
                display.blit(use, use_b3)
                if shopverif[1] == 0:
                    display.blit(textprice2, textRectprice2)
                elif shopverif[1] == 1:
                    display.blit(use, use_b)
                if shopverif[3] == 0:
                    display.blit(textprice3, textRectprice3)
                elif shopverif[3] == 1:
                    display.blit(use, use_b4)
                if use_b3.collidepoint((mx, my)):
                    if click:
                        #print("chegou aqui")
                        skin = 3
                        #print("skin no verfif3: %d", skin)
                        save.save_game_data([skin], ["skin"])
            if shopverif[3] == 0:
                if buy3.rect.collidepoint((mx, my)):
                    if click:
                        if totalscore - 10000 >= 0:
                            totalscore -= 10000
                            shopverif[3] = 1
                            #print("foi clicado")
                            save.save_game_data([totalscore], ["totalscore"])
                            save.save_game_data([shopverif], ["shopverif"])
                            text2 = font.render("COINS: " + str(totalscore), True, (0, 0, 0))
                            objectGroup.draw(display)
                            display.blit(text2, textRect2)
                            display.blit(shopbg, shopbgdisplay)
                            display.blit(menu, menu_b)
                            display.blit(use, use_b2)
                            shopGroup.draw(display)
                            display.blit(text2, textRect2)
                            display.blit(use, use_b4)
                            buy3.kill()
                            if shopverif[1] == 0:
                                display.blit(textprice, textRectprice)
                            elif shopverif[1] == 1:
                                display.blit(use, use_b)
                            if shopverif[2] == 0:
                                display.blit(textprice2, textRectprice2)
                            elif shopverif[2] == 1:
                                display.blit(use, use_b3)
                        else:
                            pass

            if shopverif[3] == 1:
                objectGroup.draw(display)
                display.blit(text2, textRect2)
                display.blit(shopbg, shopbgdisplay)
                display.blit(menu, menu_b)
                display.blit(use, use_b2)
                shopGroup.draw(display)
                display.blit(text2, textRect2)
                display.blit(use, use_b4)
                if shopverif[1] == 0:
                    display.blit(textprice, textRectprice)
                elif shopverif[1] == 1:
                    display.blit(use, use_b)
                if shopverif[2] == 0:
                    display.blit(textprice2, textRectprice2)
                elif shopverif[2] == 1:
                    display.blit(use, use_b3)
                if use_b4 .collidepoint((mx, my)):
                    if click:
                        # print("chegou aqui")
                        skin = 4
                        save.save_game_data([skin], ["skin"])
            pygame.display.update()
    save.save_game_data([totalscore], ["totalscore"])
    save.save_game_data([shopverif], ["shopverif"])
    save.save_game_data([skin], ["skin"])


def gameover_menu():
    background = pygame.sprite.Sprite(objectGroup)
    background.image = pygame.image.load("data/background_gameover.png")
    background.image = pygame.transform.scale(background.image, [840, 480])
    background.rect = background.image.get_rect()
    # sistema de save da pontuação
    save = SaveLoadSystem(".save", "save_data")
    totalscore = save.load_game_data(["totalscore"], [0])

    objectGroup.update()
    objectGroup.draw(display)

    # pontuação total
    font = pygame.font.Font("freesansbold.ttf", 32)
    text2 = font.render("COINS: " + str(totalscore), True, (0, 0, 0))
    textRect2 = text2.get_rect()
    textRect2.x = 5
    textRect2.y = 5
    objectGroup.update()
    objectGroup.draw(display)

    retry_b = retry.get_rect()
    menu_b = menu.get_rect()
    exit_b = exit.get_rect()

    retry_b.center = (130, 300)
    menu_b.center = (410, 300)
    exit_b.center = (690, 300)

    display.blit(retry, retry_b)
    display.blit(menu, menu_b)
    display.blit(exit, exit_b)

    gameoverloop = True

    while gameoverloop == True:
        clock.tick(60)
        mx, my = pygame.mouse.get_pos()

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save.save_game_data([totalscore], ["totalscore"])
                save.save_game_data([shopverif], ["shopverif"])
                save.save_game_data([skin], ["skin"])
                pygame.quit()
                gameoverloop = False

                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if retry_b.collidepoint((mx, my)):
                if click:
                    gameoverloop = False
                    save.save_game_data([totalscore], ["totalscore"])
                    game()

            if menu_b.collidepoint((mx, my)):
                if click:
                    gameoverloop = False
                    save.save_game_data([totalscore], ["totalscore"])
                    main_menu()
            if exit_b.collidepoint((mx, my)):
                if click:
                    save.save_game_data([totalscore], ["totalscore"])
                    pygame.quit()
                    gameoverloop = False
                    sys.exit()
            pygame.display.update()


def pause_menu():
    pygame.init()
    font = pygame.font.Font("freesansbold.ttf", 32)
    text2 = font.render("COINS: " + str(totalscore), True, (0, 0, 0))
    textRect2 = text2.get_rect()
    textRect2.x = 5
    textRect2.y = 5

    pause_b = pause.get_rect()
    resume_b = resume.get_rect()
    menu_b = menu.get_rect()
    exit_b = exit.get_rect()

    pause_b.center = (410, 150)
    resume_b.center = (130, 300)
    menu_b.center = (410, 300)
    exit_b.center = (690, 300)

    display.blit(pause, pause_b)
    display.blit(resume, resume_b)
    display.blit(menu, menu_b)
    display.blit(exit, exit_b)

    pauseloop = True
    while pauseloop:
        clock.tick(60)
        mx, my = pygame.mouse.get_pos()

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                pauseloop = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    # if click == True:
                    #     print("mouse pressionado")
            if resume_b.collidepoint((mx, my)):
                if click:
                    pauseloop = False

            if menu_b.collidepoint((mx, my)):
                if click:
                    pauseloop = False
                    main_menu()
            if exit_b.collidepoint((mx, my)):
                if click:
                    pygame.quit()
                    pauseloop = False
                    sys.exit()
            pygame.display.update()


def win_menu():
    background = pygame.sprite.Sprite(objectGroup)
    background.image = pygame.image.load("data/background_win.png")
    background.image = pygame.transform.scale(background.image, [840, 480])
    background.rect = background.image.get_rect()
    # sistema de save da pontuação
    save = SaveLoadSystem(".save", "save_data")
    totalscore = save.load_game_data(["totalscore"], [0])

    objectGroup.update()
    objectGroup.draw(display)

    # pontuação total
    font = pygame.font.Font("freesansbold.ttf", 32)
    text2 = font.render("COINS: " + str(totalscore), True, (0, 0, 0))
    textRect2 = text2.get_rect()
    textRect2.x = 5
    textRect2.y = 5
    textwin = font.render("CONGRATULATIONS! Vampires have been defeated", True, (0, 0, 0))
    textRectwin = textwin.get_rect()
    textRectwin.x = 420
    textRectwin.y = 440
    objectGroup.update()
    objectGroup.draw(display)

    menu_b = menu.get_rect()
    exit_b = exit.get_rect()

    menu_b.center = (270, 300)
    exit_b.center = (570, 300)

    display.blit(menu, menu_b)
    display.blit(exit, exit_b)
    display.blit(textwin, textRectwin)
    display.blit(text2, textRect2)
    winloop = True

    while winloop == True:
        clock.tick(60)
        mx, my = pygame.mouse.get_pos()

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save.save_game_data([totalscore], ["totalscore"])
                pygame.quit()
                winloop = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if menu_b.collidepoint((mx, my)):
                if click:
                    winloop = False
                    save.save_game_data([totalscore], ["totalscore"])
                    main_menu()
            if exit_b.collidepoint((mx, my)):
                if click:
                    save.save_game_data([totalscore], ["totalscore"])
                    pygame.quit()
                    winloop = False
                    sys.exit()
            pygame.display.update()


main_menu()
