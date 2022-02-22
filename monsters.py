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
        #self.speed = 5
        #self.timer = 0
    def update(self, *args):
        #self.timer += 0.001
        #self.rect.x = 200 + math.sin(self.timer) * 250
        self.rect.x -= self.speed

        if self.rect.right < 0:
            self.kill()