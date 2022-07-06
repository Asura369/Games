import random
import pygame


class Fearow(pygame.sprite.Sprite):
    def __init__(self, maxWidth=0, height=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("fearow.png")
        self.x = maxWidth
        self.y = random.randint(5, height - 50)
        self.rect = pygame.Rect(self.x, self.y, 50, 50)


    def update(self, change):
        self.x -= change
        self.rect = pygame.Rect(self.x, self.y, 50, 50)

    def collided(self, other_rect):
        return self.rect.colliderect(other_rect)

    def draw(self, surface, x, y):
        surface.blit(self.image, (x, y))
