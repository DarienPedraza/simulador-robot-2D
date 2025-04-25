# Clase que representa al robot en 2D

class Robot:
    def __init__(self, x=0, y=0, angle=0, speed=0):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed

    def move_forward(self):
        pass  # Aquí se implementará el movimiento hacia adelante

    def rotate(self, angle_delta):
        pass  # Aquí se implementará la rotación
