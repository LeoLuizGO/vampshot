import pygame
class speeddrop(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/speeddrop.png")
        self.image = pygame.transform.scale(self.image, [30, 30])
        self.rect = pygame.Rect(420, 20, 30, 30)

        self.start_time = pygame.time.get_ticks()

    def update(self):
        current_time = pygame.time.get_ticks()
        timespan = 5000

        if current_time > self.start_time + timespan:
            self.kill()


class Coindrop(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/coin+100.png")
        self.image = pygame.transform.scale(self.image, [30, 30])
        self.rect = pygame.Rect(420, 20, 30, 30)

        self.start_time = pygame.time.get_ticks()

    def update(self):
        current_time = pygame.time.get_ticks()
        timespan = 5000  # 1000 milliseconds = 1 second

        if current_time > self.start_time + timespan:
            self.kill()


class Scoredrop(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/scoredrop+100.png")
        self.image = pygame.transform.scale(self.image, [30, 30])
        self.rect = pygame.Rect(420, 20, 30, 30)

        self.start_time = pygame.time.get_ticks()

    def update(self):
        current_time = pygame.time.get_ticks()
        timespan = 5000  # 1000 milliseconds = 1 second

        if current_time > self.start_time + timespan:
            self.kill()


class Shotdrop(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/gundrop.png")
        self.image = pygame.transform.scale(self.image, [30, 30])
        self.rect = pygame.Rect(420, 20, 30, 30)

        self.start_time = pygame.time.get_ticks()

    def update(self):
        current_time = pygame.time.get_ticks()
        timespan = 5000  # 1000 milliseconds = 1 second

        if current_time > self.start_time + timespan:
            self.kill()
