import pygame
import random

class enemies(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/enemy1.png")
        # redimensionamento de imagem
        self.image = pygame.transform.scale(self.image, [150, 100])
        self.rect = pygame.Rect(100, 100, 100, 100)

        self.rect.x = 840 + random.randint(1, 400)
        self.rect.y = random.randint(1, 400)

        self.speed = 1 + random.random() * 2

    def update(self, *args):
        self.rect.x -= self.speed

        if self.rect.right < 0:
            self.kill()
class enemy2(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/enemy2.png")
        # redimensionamento de imagem
        self.image = pygame.transform.scale(self.image, [150, 100])
        self.rect = pygame.Rect(100, 100, 110, 110)

        self.rect.x = 840 + random.randint(1, 400)
        self.rect.y = random.randint(1, 400)


        self.speed = 1 + random.random() * 2

        self.start_time = pygame.time.get_ticks()

    def update(self, *args):
        if self.rect.x > 600:
            self.rect.x -= self.speed
        if self.rect.x < 600:
            current_time = pygame.time.get_ticks()
            timespan = 5000

            if current_time > self.start_time + timespan:
                self.rect.x -= self.speed
                print("liberado")
        if self.rect.x < 0:
            self.kill()
class enemy3(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/bat3.png")
        # redimensionamento de imagem
        self.image = pygame.transform.scale(self.image, [150, 100])
        self.rect = pygame.Rect(100, 100, 110, 110)

        self.rect.x = 840 + random.randint(1, 400)
        self.rect.y = random.randint(1, 400)

        self.speed = 1 + random.random() * 7
    def update(self, *args):
        self.rect.x -= self.speed

        if self.rect.right < 0:
            self.kill()


class boss(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/boss.png")
        self.image = pygame.transform.scale(self.image, [330, 450])
        self.rect = pygame.Rect(100, 100, 330, 450)

        self.rect.x = 840 + random.randint(1, 400)
        self.rect.y = 20

        self.speed = 1 + random.random() * 2
        #vida maxima do boss
        self.health = 180
        self.mult = 0
        self.pos = 330
    def update(self, *args):
        if self.rect.x > 550:
            self.rect.x -= self.speed
        if self.rect.x <= 550:
            self.rect.x = self.rect.x

    def healthbarboss(self, *groups):
        pygame.sprite.Sprite.__init__(self, *groups)
        self.image = pygame.image.load("data/healthbarboss.png")
        self.image = pygame.transform.scale(self.image, [370, 110])
        self.rect = pygame.Rect(210, 390, 330, 110)
        print("print")
        #(390, 410, 330, 70)
    def hit(self):
        if self.health > 0:
            if self.mult == 0:
                self.health -= 3
                self.pos = 330
                self.mult += 1
            else:
                self.health -= 3
                self.pos = 330 - (5.5 * self.mult)
                self.mult += 1
            #print("hit self.pos: %d" % self.pos)
        else:
            self.kill()
        #print('hit')
    def healthbarinner(self, *groups):
        pygame.sprite.Sprite.__init__(self, *groups)
        self.hit()
        self.image = pygame.image.load("data/healbarinner.png")
        self.image = pygame.transform.scale(self.image, [self.pos, 110])
        self.rect = pygame.Rect(250, 390, 330, 110)



