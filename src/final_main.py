# ===== IMPORTS =====
import pygame
import sys
import random

# ===== INICIALIZACIÓN =====
pygame.init()

# ===== CONFIGURACIÓN DE PANTALLA =====
# Detectar resolución de pantalla
info = pygame.display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = info.current_w, info.current_h
screen = pygame.display.set_mode((SCREEN_WIDTH - 100, SCREEN_HEIGHT - 100), pygame.RESIZABLE)
pygame.display.set_caption("Robot 2D")

# ===== CARGAR RECURSOS =====
# Cargar imágenes después de crear la ventana
robot_img, obstacle_img, collectible_img, boton_reset_img, robot_mask, obstacle_mask, collectible_mask = cargar_imagenes()

# Cargar icono y fondo
fondo = pygame.image.load("imagenes/space.png").convert()
# ===== CONSTANTES =====
# Colores
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
AZUL = (70, 70, 200)
VERDE = (0, 255, 0)
AMARILLO = (255, 255, 0)
NEGRO = (0, 0, 0)

# Fuente y reloj
font = pygame.font.SysFont("Arial", 18)
clock = pygame.time.Clock()
FPS = 60

































































# ===== CONTROLES =====
 # Controles por teclado
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        robot.speed = 150 * dt
    elif keys[pygame.K_s]:
        robot.speed = -150 * dt
    else:
        robot.speed = 0

    if keys[pygame.K_a]:
        robot.angle += 180 * dt
    if keys[pygame.K_d]:
        robot.angle -= 180 * dt

    # Movimiento por botón mantenido
    if mouse_held and button_pressed:
        if button_pressed == "up":
            robot.speed = 150 * dt
        elif button_pressed == "down":
            robot.speed = -150 * dt
        elif button_pressed == "left":
            robot.angle += 180 * dt
        elif button_pressed == "right":
            robot.angle -= 180 * dt
