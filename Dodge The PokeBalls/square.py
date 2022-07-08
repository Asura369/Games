import pygame


class Square:
    def __init__(self, color, x, y, width, height, speed):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.direction = 'E'
        self.speed = speed

    def move(self):
        if self.direction == 'E':
            self.rect.x = self.rect.x + self.speed
        if self.direction == 'W':
            self.rect.x = self.rect.x - self.speed
        if self.direction == 'N':
            self.rect.y = self.rect.y - self.speed
        if self.direction == 'S':
            self.rect.y = self.rect.y + self.speed

    def moveDirection(self, direction):
        if direction == 'E':
            self.rect.x = self.rect.x + self.speed
        if direction == 'W':
            self.rect.x = self.rect.x - self.speed
        if direction == 'N':
            self.rect.y = self.rect.y - self.speed
        if direction == 'S':
            self.rect.y = self.rect.y + self.speed

    def collided(self, other_rect):
        return self.rect.colliderect(other_rect)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def reset(self, color, x, y, width, height, speed):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.speed = speed
