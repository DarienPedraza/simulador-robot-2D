import pygame
import math

class Robot:
    def __init__(self, x, y):
        self.x = x  # Posición X
        self.y = y  # Posición Y
        self.angle = 0  # Ángulo en grados
        self.speed = 0  # Velocidad actual
        self.size = 40  # Tamaño del robot
        self.image = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        self.image.fill((0, 255, 0))  # Verde

        self.energy = 100  # Energía del robot (0 a 100)
        self.score = 0     # Puntos por recolectar elementos

    def move(self):
        # Mueve el robot en la dirección actual, si tiene energía
        if self.energy > 0:
            rad = math.radians(self.angle)
            self.x += self.speed * math.cos(rad)
            self.y -= self.speed * math.sin(rad)
            self.energy = max(0, self.energy - abs(self.speed) * 0.1)  # Consumo de energía

    def draw(self, screen):
        # Rota y dibuja el robot en pantalla
        rotated = pygame.transform.rotate(self.image, self.angle)
        rect = rotated.get_rect(center=(self.x, self.y))
        screen.blit(rotated, rect)

def get_rect(self):
        # Devuelve el rectángulo de colisión del robot
        return pygame.Rect(self.x - self.size / 2, self.y - self.size / 2, self.size, self.size)

def reset(self, x, y):
        # Reinicia la posición, ángulo, velocidad, energía y puntos
        self.x, self.y = x, y
        self.angle = 0
        self.speed = 0
        self.energy = 100
        self.score = 0
