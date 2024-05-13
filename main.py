# Primer programa en Pygame
import pygame  # Importa el módulo pygame para trabajar con gráficos y sonido
import config as cf  # Importa el módulo config.py, asumiendo que contiene la clase Config que tiene un atributo deltaT_s
import snake as sk  # Importa el módulo modulo_juego.py que contiene la clase Juego
pygame.init()  # Inicializa pygame


# Creamos la ventana de juego
tamano = (cf.SCREEN_WIDTH, cf.SCREEN_HEIGHT)  # Tamaño de la ventana del juego
screen = pygame.display.set_mode(tamano)  # Crea una ventana con el tamaño especificado

# El tiempo que pasa entre un cuadro y otro
deltaTiempo_s = cf.Config.deltaT_s  # Obtiene el atributo deltaT_s de la clase Config

# Construir el juego
snake_juego = sk.Juego()  # Inicializa un objeto de la clase Juego del módulo modulo_juego

salir = False  # Variable para controlar la salida del bucle principal del juego

# Bucle principal del juego
while not salir:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            salir = True  # Si se detecta el evento de cerrar la ventana, se establece salir como True
        snake_juego.movimiento_teclado(event)  # Maneja los eventos de teclado

    # Actualiza la posición de la serpiente en función de la dirección
    snake_juego.actualizar()

    # Aquí redibujamos todos los objetos del juego
    snake_juego.dibuja(screen)  # Llama al método dibuja de la clase Juego para redibujar todos los objetos en la pantalla

    # Flip para pantalla
    pygame.display.flip()  # Actualiza la pantalla

pygame.quit()  # Cierra pygame
print("Fin del programa")  # Imprime un mensaje indicando que el programa ha terminado