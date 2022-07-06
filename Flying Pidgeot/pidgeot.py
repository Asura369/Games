import pygame


class Pidgeot(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, speed=2):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("pidgeot.png")
        self.x = x
        self.y = y
        self.speed = speed
        self.rect = pygame.Rect(self.x, self.y, 60, 60)

    def update(self, direction=-1):
        if direction > 0:
            self.y -= self.speed
        else:
            self.y += self.speed
        self.rect = pygame.Rect(self.x, self.y, 60, 60)

    def collided(self, other_rect):
        return self.rect.colliderect(other_rect)

    def draw(self, surface, x, y):
        surface.blit(self.image, (x, y))
