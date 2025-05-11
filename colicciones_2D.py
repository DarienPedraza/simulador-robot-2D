
### Estos son codigos base para el codigo final estan oriendos
#en ciertos puntos del codigo final.




import pygame

## Diseño e implementación de obstáculos

obstaculo1 = pygame.Rect(300, 200, 100, 50)
obstaculo2 = pygame.Rect(500, 400, 120, 60)
lista_obstaculos = [obstaculo1, obstaculo2]

for obstaculo in lista_obstaculos:
    pygame.draw.rect(pantalla, (255, 0, 0), obstaculo)




##Detección de colisiones

robot_rect = pygame.Rect(robot_x, robot_y, robot_ancho, robot_alto)

for obstaculo in lista_obstaculos:
    if robot_rect.colliderect(obstaculo):
        if teclas[pygame.K_LEFT]:
            robot_x += velocidad
        if teclas[pygame.K_RIGHT]:
            robot_x -= velocidad
        if teclas[pygame.K_UP]:
            robot_y += velocidad
        if teclas[pygame.K_DOWN]:
            robot_y -= velocidad



##Reinicio de simulación

def reiniciar_simulacion():
    global robot_x, robot_y
    robot_x = 100
    robot_y = 100

for evento in pygame.event.get():
    if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_r:
            reiniciar_simulacion()
