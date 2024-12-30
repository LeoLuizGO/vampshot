import pygame

# contador de tempo:
currenttime = 0
timemark = 0


class hearts(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/heart2d.png")
        # redimensionamento de imagem
        self.image = pygame.transform.scale(self.image, [40, 40])    #diminuindo a imagem até 40 por 40
        self.rect = pygame.Rect(420, 20, 40, 40)                    #criando o retangulo que a imagem vai ficar

class heartsoff(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/heart2doff.png")
        # redimensionamento de imagem
        self.image = pygame.transform.scale(self.image, [40, 40])    #diminuindo a imagem até 40 por 40
        self.rect = pygame.Rect(420, 20, 40, 40)                    #criando o retangulo que a imagem vai ficar

class heartdrop(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/heartdrop.png")
        self.image = pygame.transform.scale(self.image, [30, 30])  # diminuindo a imagem até 40 por 40
        self.rect = pygame.Rect(420, 20, 30, 30)  # criando o retangulo que a imagem vai ficar

        self.start_time = pygame.time.get_ticks()

    def update(self):
        current_time = pygame.time.get_ticks()
        timespan = 5000  # 1000 milliseconds = 1 second

        if current_time > self.start_time + timespan:
            self.kill()

