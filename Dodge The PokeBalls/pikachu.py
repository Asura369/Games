import pygame


class Pikachu(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, speed=5):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("pikachu.png")
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = 'E'
        self.rect = pygame.Rect(self.x, self.y, 60, 60)

    def update(self, direction):
        if direction == 'E':
            self.x += self.speed
        if direction == 'W':
            self.x -= self.speed
        if direction == 'N':
            self.y -= self.speed
        if direction == 'S':
            self.y += self.speed
        self.rect = pygame.Rect(self.x, self.y, 60, 60)

    def collided(self, other_rect):
        return self.rect.colliderect(other_rect)

    def draw(self, surface, x, y):
        # pygame.draw.rect(surface, (255, 0, 0), self.rect)
        surface.blit(self.image, (x, y))
