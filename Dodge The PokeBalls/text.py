import pygame


class Text:
    def __init__(self, x=0, y=0, size=24, text=""):
        self.x = x
        self.y = y
        self.size = size
        self.text = text
        fontObj = pygame.font.Font("freesansbold.ttf", self.size)
        self.__surface = fontObj.render(self.text, True, (255, 0, 0))

    def draw(self, surface):
        fontObj = pygame.font.Font("freesansbold.ttf", self.size)
        self.__surface = fontObj.render(self.text, True, (255, 0, 0))
        surface.blit(self.__surface, (self.x, self.y))

    def reset(self, x=0, y=0):
        self.x = x
        self.y = y
        fontObj = pygame.font.Font("freesansbold.ttf", 48)
        self.__surface = fontObj.render(self.text, True, (255, 0, 0))
