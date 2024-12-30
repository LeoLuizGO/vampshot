import pygame
#from ship import player, Speed
class sbuff(pygame.sprite.Sprite):
    speedd = int
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/speedbuff.png")
        self.image = pygame.transform.scale(self.image, [50, 50])
        self.rect = pygame.Rect(10, 70, 50, 50)

        self.start_time = pygame.time.get_ticks()
    def update(self):
        current_time = pygame.time.get_ticks()
        #timespan2 = 12000
        timespan = 15000  # 1000 milliseconds = 1 second
        #speedd = 0
        #print("update: %d" % speedd)
        #if current_time > self.start_time + timespan2:
            #speedd = 1
        if current_time > self.start_time + timespan:
            self.kill()
            #print("update: %d" % speedd)
class Shotbuff(pygame.sprite.Sprite):
    speedd = int
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/shotbuff.png")
        self.image = pygame.transform.scale(self.image, [50, 50])
        self.rect = pygame.Rect(70, 70, 50, 50)

        self.start_time = pygame.time.get_ticks()
    def update(self):
        current_time = pygame.time.get_ticks()
        #timespan2 = 12000
        timespan = 15000  # 1000 milliseconds = 1 second
        #speedd = 0
        #print("update: %d" % speedd)
        #if current_time > self.start_time + timespan2:
            #speedd = 1
        if current_time > self.start_time + timespan:
            self.kill()
            #print("update: %d" % speedd)