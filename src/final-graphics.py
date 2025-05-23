import pygame

def cargar_imagenes():
    robot_size = (70, 70)
    obstacle_size = (100, 100)
    collectible_size = (50, 50)
    boton_reset_size = (100, 40)

    # Cargar imágenes con transparencia
    robot_img = pygame.transform.scale(pygame.image.load("imagenes/robot.png").convert_alpha(), robot_size)
    obstacle_img = pygame.transform.scale(pygame.image.load("imagenes/meteorito.png").convert_alpha(), obstacle_size)
    collectible_img = pygame.transform.scale(pygame.image.load("imagenes/bateria.png").convert_alpha(), collectible_size)
    boton_reset_img = pygame.transform.scale(pygame.image.load("imagenes/reset.png").convert_alpha(), boton_reset_size)

    # Crear máscaras de colisión
    robot_mask = pygame.mask.from_surface(robot_img)
    obstacle_mask = pygame.mask.from_surface(obstacle_img)
    collectible_mask = pygame.mask.from_surface(collectible_img)

    return (robot_img, obstacle_img, collectible_img, boton_reset_img, robot_mask, obstacle_mask, collectible_mask)
