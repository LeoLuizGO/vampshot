import pygame
import random

class player(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load("data/ship.png")
        # redimensionamento de imagem
        self.image = pygame.transform.scale(self.image, [150, 100])
        self.rect = pygame.Rect(100, 100, 150, 100)
        self.speed = 0
        self.speed2 = 0

    def update(self, *args):

        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > 480:
            self.rect.bottom = 480
        elif self.rect.right > 840:
            self.rect.right = 840
        elif self.rect.left < 0:
            self.rect.left = 0


class player2(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load("data/ship2.png")
        # redimensionamento de imagem
        self.image = pygame.transform.scale(self.image, [150, 100])
        self.rect = pygame.Rect(100, 100, 150, 100)
        self.speed = 0
        self.speed2 = 0

    def update(self, *args):
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > 480:
            self.rect.bottom = 480
        elif self.rect.right > 840:
            self.rect.right = 840
        elif self.rect.left < 0:
            self.rect.left = 0


class player3(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load("data/ship3.png")
        # redimensionamento de imagem
        self.image = pygame.transform.scale(self.image, [150, 100])
        self.rect = pygame.Rect(100, 100, 150, 100)
        self.speed = 0
        self.speed2 = 0

    def update(self, *args):
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > 480:
            self.rect.bottom = 480
        elif self.rect.right > 840:
            self.rect.right = 840
        elif self.rect.left < 0:
            self.rect.left = 0


class player4(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load("data/ship4.png")
        # redimensionamento de imagem
        self.image = pygame.transform.scale(self.image, [150, 100])
        self.rect = pygame.Rect(100, 100, 150, 100)
        self.speed = 0
        self.speed2 = 0

    def update(self, *args):

        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > 480:
            self.rect.bottom = 480
        elif self.rect.right > 840:
            self.rect.right = 840
        elif self.rect.left < 0:
            self.rect.left = 0


class Shipsos(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load("data/shipsos.png")
        # redimensionamento de imagem
        self.image = pygame.transform.scale(self.image, [130, 80])
        self.rect = pygame.Rect(100, 100, 130, 80)
        self.speed = 3

        self.rect.x = 840 + random.randint(1, 400)
        self.rect.y = random.randint(1, 400)
    def update(self, *args):
        self.rect.x -= self.speed

        if self.rect.right < 0:
            self.kill()


class Shot3(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/triplegun.png")
        self.image = pygame.transform.scale(self.image, [150, 100])
        self.rect = pygame.Rect(100, 100, 150, 100)

    def update(self, *args):

        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > 480:
            self.rect.bottom = 480
        elif self.rect.right > 840:
            self.rect.right = 840
        elif self.rect.left < 0:
            self.rect.left = 0