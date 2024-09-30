import pygame
import random

pygame.init()

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Laboratorio N°1 - Ejercicio 2")


# Colores
AZUL = (0, 0, 255)
ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)

# FPS (Frames por segundo)
FPS = 60
reloj = pygame.time.Clock()

class Puntos:
    def __init__(self, x, y, velocidad):
        self.x = x
        self.y = y
        self.velocidad = velocidad
        self.radio = 8  # Tamaño del punto

    def mover(self):
        self.y += self.velocidad
        if self.y > ALTO:  # Se reinicia la posición cuando el punto rojo sale de la pantalla
            self.reiniciar()

    def reiniciar(self):
        self.x = random.randint(0, ANCHO - self.radio)
        self.y = random.randint(-100, -40)

    def dibujar(self):
        pygame.draw.circle(pantalla, ROJO, (self.x, self.y), self.radio)


# Clase Triángulo

""" IMPLEMENTAR CÓDIGO """
class Triangulo():
    def __init__(self, x, velocidad):
        self.x = x
        self.velocidad = velocidad
    
    def dibujar(self):
        pygame.draw.polygon(pantalla, AZUL, self.x, {100, 400})

triangulo = Triangulo(400, 500)


# Función Principal
def main():
    # Creación de la lista de puntos rojos
    puntos_rojos = [Puntos(random.randint(0, ANCHO - 10), random.randint(-100, -40), random.randint(2, 6)) for _ in range(5)]

    corriendo = True
    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

        # Limpiar pantalla
        pantalla.fill(NEGRO)

        # Mover y dibujar los puntos rojos
        for punto in puntos_rojos:
            punto.mover()
            punto.dibujar()

        # Actualizar pantalla
        pygame.display.flip()
        reloj.tick(FPS)

    pygame.quit()

# Iniciar el juego
if __name__ == "__main__":
    main()
