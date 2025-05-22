
import pygame
import math

class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0  # en grados
        self.speed = 0
        self.size = 40

    def move(self):
        rad = math.radians(self.angle)
        self.x += self.speed * math.cos(rad)
        self.y -= self.speed * math.sin(rad)

    def draw(self, screen):
        rotated = pygame.transform.rotate(
            pygame.Surface((self.size, self.size)), self.angle
        )
        rotated.fill((0, 255, 0))
        rect = rotated.get_rect(center=(self.x, self.y))
        screen.blit(rotated, rect)

    def get_rect(self):
        return pygame.Rect(self.x - self.size/2, self.y - self.size/2, self.size, self.size)

    def reset(self, x, y):
        self.x, self.y = x, y
        self.angle = 0
        self.speed = 0
