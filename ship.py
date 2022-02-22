import pygame

class player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/ship.png")
        # redimensionamento de imagem
        self.image = pygame.transform.scale(self.image, [150, 100])
        self.rect = pygame.Rect(100, 100, 100, 100)

        self.speed = 0
        self.speed2 = 0

    def update(self, *args):
        #logica
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.rect.x += 5
        elif keys[pygame.K_a]:
            self.rect.x -= 5
        elif keys[pygame.K_w]:
            self.rect.y -= 5
        elif keys[pygame.K_s]:
            self.rect.y += 5

        self.rect.y += self.speed2
        self.rect.x += self.speed

        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > 480:
            self.rect.bottom = 480
        elif self.rect.right > 840:
            self.rect.right = 840
        elif self.rect.left < 0:
            self.rect.left = 0
