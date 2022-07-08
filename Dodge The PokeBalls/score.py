import pygame


class Score:
    def __init__(self, x=0, y=0, num=0):
        self.x = x
        self.y = y
        self.num = num
        fontObj = pygame.font.Font("freesansbold.ttf", 24)
        self.__surface = fontObj.render(self.__str__(), True, (255, 255, 0))

    def __str__(self):
        return f'Score: {self.num}'

    # draws the text to game screen
    def draw(self, surface):
        fontObj = pygame.font.Font("freesansbold.ttf", 24)
        self.__surface = fontObj.render(self.__str__(), True, (255, 255, 0))
        surface.blit(self.__surface, (self.x, self.y))

    def reset(self, x=0, y=0, num=0):
        self.x = x
        self.y = y
        self.num = num
        fontObj = pygame.font.Font("freesansbold.ttf", 24)
        self.__surface = fontObj.render(self.__str__(), True, (255, 255, 0))
