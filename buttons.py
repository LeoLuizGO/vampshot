import pygame
display = pygame.display.set_mode([840, 480])

print(pygame.font.get_fonts())

class Button():
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()

    def draw(self):
        display.blit(self.image, (self.rect.x, self.rect.y))