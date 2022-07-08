import pygame


class Pokeball(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, speedX=3, speedY=3):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("pokeball.png")
        self.x = x
        self.y = y
        self.speedX = speedX
        self.speedY = speedY
        self.rect = pygame.Rect(self.x, self.y, 30, 30)

    def update(self, directionX=1, directionY=1):
        if directionX == 1:
            self.x += self.speedX
        else:
            self.x -= self.speedX
        if directionY == 1:
            self.y += self.speedY
        else:
            self.y -= self.speedY
        self.rect = pygame.Rect(self.x, self.y, 30, 30)

    def collided(self, other_rect):
        return self.rect.colliderect(other_rect)

    def draw(self, surface, x, y):
        # pygame.draw.rect(surface, (255, 0, 0), self.rect)
        surface.blit(self.image, (x, y))
