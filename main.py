import pygame
import config as cf
import snake as sk
pygame.init()
tamano = (cf.SCREEN_WIDTH, cf.SCREEN_HEIGHT)
screen = pygame.display.set_mode(tamano)
deltaTiempo_s = cf.Config.deltaT_s
snake_juego = sk.Juego()
salir = False
while not salir:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            salir = True
        snake_juego.movimiento_teclado(event)
    snake_juego.actualizar()
    snake_juego.dibuja(screen)
    pygame.display.flip()
pygame.quit()
print("Fin del programa")