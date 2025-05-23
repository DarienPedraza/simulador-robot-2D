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

