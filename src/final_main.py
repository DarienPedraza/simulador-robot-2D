# ===== IMPORTS =====
import pygame
from robot import Robot
import sys
import random
from graphics import cargar_imagenes

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

# Cantidad de collectibles
NUM_COLLECTIBLES = 10

# ===== OBJETOS DEL JUEGO =====
# Obstáculos (lista)
obstacles = [
    pygame.Rect(100, 100, 100, 100),
    pygame.Rect(400, 50, 100, 100),
    pygame.Rect(750, 100, 100, 100),
    pygame.Rect(1100, 150, 100, 100),
    pygame.Rect(1400, 200, 100, 100),
    pygame.Rect(1700, 50, 100, 100),
    pygame.Rect(150, 400, 100, 100),
    pygame.Rect(500, 450, 100, 100),
    pygame.Rect(900, 400, 100, 100),
    pygame.Rect(1300, 450, 100, 100),
    pygame.Rect(1700, 400, 100, 100),
    pygame.Rect(250, 700, 100, 100),
    pygame.Rect(700, 650, 100, 100),
    pygame.Rect(1200, 680, 100, 100),
    pygame.Rect(1600, 700, 100, 100),
]

# ===== FUNCIONES AUXILIARES =====
# Función para crear puntos sin que queden dentro de obstáculos
def generar_collectible_valido():
    while True:
        c = pygame.Rect(random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100), 30, 30)
        if not any(c.colliderect(ob) for ob in obstacles):
            return c
            
# ===== INICIALIZACIÓN DE OBJETOS =====
# Inicializar robot y collectibles
robot = Robot(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
collectibles = [generar_collectible_valido() for _ in range(NUM_COLLECTIBLES)]

# ===== INTERFAZ DE USUARIO =====
# Botones
reset_button = pygame.Rect(SCREEN_WIDTH - 150, 20, 120, 40)
btn_up = pygame.Rect(80, SCREEN_HEIGHT - 120, 60, 40)
btn_down = pygame.Rect(80, SCREEN_HEIGHT - 60, 60, 40)
btn_left = pygame.Rect(20, SCREEN_HEIGHT - 90, 50, 40)
btn_right = pygame.Rect(150, SCREEN_HEIGHT - 90, 50, 40)

# Estados de botones
mouse_held = False
button_pressed = None

# ===== BUCLE PRINCIPAL =====
# Fondo animado
X = 0
running = True
while running:
    dt = clock.tick(FPS) / 1000  # Delta time

    # ===== MANEJO DE FONDO =====
    # Fondo en movimiento
    x_relativa = X % fondo.get_rect().width
    screen.blit(fondo, (x_relativa - fondo.get_rect().width, 0))
    if x_relativa < SCREEN_WIDTH:
        screen.blit(fondo, (x_relativa, 0))
    X -= 1

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
    
# ===== LÓGICA DEL JUEGO =====
    # Movimiento y colisión
    prev_pos = (robot.x, robot.y)
    robot.move()
    for ob in obstacles:
        # Obtener posiciones relativas
        offset_x = ob.x - robot.x
        offset_y = ob.y - robot.y
    
        # Verificar colisión pixel-perfect
        if robot_mask.overlap(obstacle_mask, (offset_x, offset_y)):
            robot.x, robot.y = prev_pos
            break

    # Colisión con recolectables
    for c in collectibles[:]:
        if robot.get_rect().colliderect(c):
            robot.score += 1
            robot.energy = min(100, robot.energy + 20)
            collectibles.remove(c)
            
            # Al consumir uno, generar dos nuevos inmediatamente
            for _ in range(1):
                collectibles.append(pygame.Rect(random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100), 30, 30))

    # ===== RENDERIZADO =====
    # Dibujar elementos
    screen.blit(robot_img, (robot.x, robot.y))

    # Dibujar obstáculos
    for ob in obstacles:
        screen.blit(obstacle_img, (ob.x, ob.y))

    # Recolectables
    for c in collectibles:
        screen.blit(collectible_img, (c.x, c.y))

    # Botón reiniciar
    screen.blit(boton_reset_img, (reset_button.x, reset_button.y))

    # Botones de GUI
    pygame.draw.rect(screen, BLANCO, btn_up)
    pygame.draw.rect(screen, BLANCO, btn_down)
    pygame.draw.rect(screen, BLANCO, btn_left)
    pygame.draw.rect(screen, BLANCO, btn_right)

    screen.blit(font.render("↑", True, NEGRO), (btn_up.x + 22, btn_up.y + 8))
    screen.blit(font.render("↓", True, NEGRO), (btn_down.x + 22, btn_down.y + 8))
    screen.blit(font.render("←", True, NEGRO), (btn_left.x + 18, btn_left.y + 8))
    screen.blit(font.render("→", True, NEGRO), (btn_right.x + 18, btn_right.y + 8))

 # Info en pantalla
    info_text = f"Pos: ({int(robot.x)}, {int(robot.y)}) | Ángulo: {int(robot.angle)}° | Puntos: {robot.score}"
    screen.blit(font.render(info_text, True, BLANCO), (20, 20))

    # Energía
    pygame.draw.rect(screen, NEGRO, (20, 50, 200, 20))
    pygame.draw.rect(screen, VERDE, (20, 50, 2 * robot.energy, 20))
    screen.blit(font.render(f"Energía: {robot.energy}%", True, BLANCO), (230, 50))

    # ===== MANEJO DE EVENTOS =====
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
            screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_held = True
            if reset_button.collidepoint(event.pos):
                robot.reset(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
                collectibles = [generar_collectible_valido() for _ in range(NUM_COLLECTIBLES)]

            elif btn_up.collidepoint(event.pos):
                button_pressed = "up"
            elif btn_down.collidepoint(event.pos):
                button_pressed = "down"
            elif btn_left.collidepoint(event.pos):
                button_pressed = "left"
            elif btn_right.collidepoint(event.pos):
                button_pressed = "right"

        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_held = False
            button_pressed = None
            robot.speed = 0  # Detener movimiento al soltar

        elif event.type == pygame.VIDEORESIZE:
            SCREEN_WIDTH, SCREEN_HEIGHT = event.w, event.h
            screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
            reset_button = pygame.Rect(SCREEN_WIDTH - 150, 20, 120, 40)
            btn_up = pygame.Rect(80, SCREEN_HEIGHT - 120, 60, 40)
            btn_down = pygame.Rect(80, SCREEN_HEIGHT - 60, 60, 40)
            btn_left = pygame.Rect(20, SCREEN_HEIGHT - 90, 50, 40)
            btn_right = pygame.Rect(150, SCREEN_HEIGHT - 90, 50, 40)

    pygame.display.flip()

pygame.quit()
sys.exit()
