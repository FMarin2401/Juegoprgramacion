# Primer programa en Pygame
import pygame  # Importa el módulo pygame para trabajar con gráficos y sonido
import config as cf  # Importa el módulo config.py, asumiendo que contiene la clase Config que tiene un atributo deltaT_s
import snake as sk  # Importa el módulo modulo_juego.py que contiene la clase Juego
pygame.init()  # Inicializa pygame

# Creamos la ventana de juego
tamano = (800, 600)  # Tamaño de la ventana del juego
screen = pygame.display.set_mode(tamano)  # Crea una ventana con el tamaño especificado

# El tiempo que pasa entre un cuadro y otro
deltaTiempo_s = cf.Config.deltaT_s  # Obtiene el atributo deltaT_s de la clase Config

# Construir el juego
este_juego = sk.Juego()  # Inicializa un objeto de la clase Juego del módulo modulo_juego

salir = False  # Variable para controlar la salida del bucle principal del juego
while salir == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: salir = True  # Si se detecta el evento de cerrar la ventana, se establece salir como True

    # Entrada por teclado
    key = pygame.key.get_pressed()  # Obtiene el estado de todas las teclas
    if key[pygame.K_ESCAPE]: salir = True  # Si se presiona la tecla ESCAPE, se establece salir como True

    # Aqui recalculamos todas las variables del juego
    este_juego.actualiza_variables()  # Llama al método actualiza_variables de la clase Juego para actualizar las variables del juego

    # Aquí redibujamos todos los objetos del juego
    este_juego.dibuja(screen)  # Llama al método dibuja de la clase Juego para redibujar todos los objetos en la pantalla

    # Flip para pantalla
    pygame.display.flip()  # Actualiza la pantalla
    pygame.time.wait(int(deltaTiempo_s * 1000))  # Espera un tiempo determinado antes de la siguiente iteración del bucle

pygame.display.quit()  # Cierra la ventana de pygame
print("Fin del programa")  # Imprime un mensaje indicando que el programa ha terminado
