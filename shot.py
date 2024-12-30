import pygame
import math
import random
class Shot(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/Laser.png")
        self.image = pygame.transform.scale(self.image, [15, 10])
        self.rect = self.image.get_rect()

        self.speed = 4

    def update(self, *args):
        self.rect.x += self.speed

        if self.rect.left > 840:
            self.kill()
class Enemyshot(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/shotmonster.png")
        self.image = pygame.transform.scale(self.image, [30, 20])
        self.rect = self.image.get_rect()
        self.speed = 3
        self.x = random.randint(-1000, 1000)
        self.y = random.randint(-1000, 0)
        # posição do boss

    def update(self, *args):

        angle = math.atan2(self.x, self.y)
        self.rect.x += (math.cos(angle) * self.speed)
        self.rect.y += (math.sin(angle) * self.speed)

        #print("bala aqui x: {0} y: {1}".format(self.x, self.y))
        if self.rect.right > 840 or self.rect.left < 0 or self.rect.top < 0 or self.rect.bottom > 480:
            self.kill()

