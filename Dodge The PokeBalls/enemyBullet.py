import math
from square import Square


class EnemyBullet(Square):
    def __init__(self, color, x, y, width, height, speed, target_x, target_y):
        super().__init__(color, x, y, width, height, speed)
        angle = math.atan2(target_y - y, target_x - x)  # get angle to target in radians
        # print('Angle in degrees:', int(angle * 180 / math.pi))
        self.dx = math.cos(angle) * speed
        self.dy = math.sin(angle) * speed
        self.x = x
        self.y = y

    def move(self):
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
