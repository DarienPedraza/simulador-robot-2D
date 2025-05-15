
import pygame
from robot import Robot

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulador de Robot 2D")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 18)

robot = Robot(WIDTH//2, HEIGHT//2)
obstacle = pygame.Rect(300, 200, 100, 100)
reset_button = pygame.Rect(650, 20, 120, 40)

## Diseño e implementación de obstáculos adicionales
obstaculo1 = pygame.Rect(300, 200, 100, 50)
obstaculo2 = pygame.Rect(500, 400, 120, 60)
lista_obstaculos = [obstaculo1, obstaculo2]

## Reinicio de simulación con tecla 'R'
def reiniciar_simulacion():
    robot.x = 100
    robot.y = 100

running = True
while running:
    screen.fill((30, 30, 30))
    dt = clock.tick(60) / 1000

    # Input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: robot.speed = 150 * dt
    elif keys[pygame.K_s]: robot.speed = -150 * dt
    else: robot.speed = 0

    if keys[pygame.K_a]: robot.angle += 180 * dt
    if keys[pygame.K_d]: robot.angle -= 180 * dt

    # Movimiento y colisión
    prev_pos = (robot.x, robot.y)
    robot.move()
    if robot.get_rect().colliderect(obstacle):
        robot.x, robot.y = prev_pos  # retrocede

    ## Detección de colisiones con nuevos obstáculos
    robot_rect = pygame.Rect(robot.x, robot.y, 50, 50)
    for obst in lista_obstaculos:
        if robot_rect.colliderect(obst):
            if teclas[pygame.K_LEFT]:
                robot.x += 150 * dt
            if teclas[pygame.K_RIGHT]:
                robot.x -= 150 * dt
            if teclas[pygame.K_UP]:
                robot.y += 150 * dt
            if teclas[pygame.K_DOWN]:
                robot.y -= 150 * dt

    # Dibujo
    robot.draw(screen)
    pygame.draw.rect(screen, (255, 0, 0), obstacle)
    pygame.draw.rect(screen, (70, 70, 200), reset_button)
    screen.blit(font.render("Reiniciar", True, (255, 255, 255)), (reset_button.x + 10, reset_button.y + 10))

     ## Dibujo de nuevos obstáculos
    for obst in lista_obstaculos:
        pygame.draw.rect(pantalla, (255, 0, 0), obst)

    # Mostrar datos
    info = f"Pos: ({int(robot.x)}, {int(robot.y)}) | Ángulo: {int(robot.angle)} | Velocidad: {round(robot.speed*60,1)} px/s"
    screen.blit(font.render(info, True, (255, 255, 255)), (20, 20))

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if reset_button.collidepoint(event.pos):
                robot.reset(WIDTH//2, HEIGHT//2)

    pygame.display.flip()

pygame.quit()
