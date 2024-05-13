import pygame
import config as cf  # Importa el módulo config.py, asumiendo que contiene la clase Config que tiene un atributo deltaT_s
import sys
import random
class Juego():
    def __init__(self):
        self.tablero_fondo = Fondo()
        self.snake_cuerpo = [Cuerpo(100, 100)]  # Inicializa la serpiente con un solo segmento en la posición (100, 100)
        self.direccion = "RIGHT"  # Inicializa la dirección de la serpiente
        self.velocidad = 0.5 #Velocidad de la serpiente
        
    def movimiento_teclado(self, event):
        """
        Maneja los eventos de teclado para controlar la dirección de la serpiente.

        Args:
            event: El evento de teclado.
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                self.direccion = "UP"
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.direccion = "DOWN"
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.direccion = "LEFT"
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.direccion = "RIGHT"

    def dibuja(self, screen):
        """
        Dibuja el tablero y el cuerpo en la pantalla.

        Args:
            screen (Surface): La superficie de la pantalla donde se dibujarán los objetos.
        """
        self.tablero_fondo.dibuja(screen)  # Dibuja el fondo del tablero
        for cuerpo in self.snake_cuerpo:
            cuerpo.dibujar(screen)  # Dibuja cada parte del cuerpo de la serpiente en la pantalla

    def actualizar(self):
        """
        Actualiza la posición de la serpiente en función de la dirección y la velocidad.
        Verifica las colisiones con los bordes de la ventana.
        """
        cabeza_x = self.snake_cuerpo[0].x
        cabeza_y = self.snake_cuerpo[0].y

        if self.direccion == "UP":
            cabeza_y -= self.velocidad
        elif self.direccion == "DOWN":
            cabeza_y += self.velocidad
        elif self.direccion == "LEFT":
            cabeza_x -= self.velocidad
        elif self.direccion == "RIGHT":
            cabeza_x += self.velocidad

        # Verifica las colisiones con los bordes de la ventana
        if cabeza_x < 0 or cabeza_x >= cf.SCREEN_WIDTH or cabeza_y < 0 or cabeza_y >= cf.SCREEN_HEIGHT:
            # La serpiente ha colisionado con los bordes de la ventana
            mensaje = "¡Colisión con el borde de la ventana!"
            font = pygame.font.SysFont(None, 36)  # Define la fuente del texto
            texto = font.render(mensaje, True, (255, 255, 255))  # Renderiza el texto
            screen.blit(texto, (cf.SCREEN_WIDTH // 2 - texto.get_width() // 2, cf.SCREEN_HEIGHT // 2 - texto.get_height() // 2))  # Dibuja el texto en el centro de la pantalla
            pygame.display.update()  # Actualiza la pantalla
            pygame.time.delay(2000)  # Espera 2 segundos antes de cerrar el juego
            pygame.quit()  # Cierra pygame
            sys.exit()  # Cierra el programa

        # Crea un nuevo segmento en la posición de la nueva cabeza
        nueva_cabeza = Cuerpo(cabeza_x, cabeza_y)

        # Inserta el nuevo segmento al principio de la lista
        self.snake_cuerpo.insert(0, nueva_cabeza)

        # Elimina el último segmento de la serpiente (para que parezca que se está moviendo)
        self.snake_cuerpo.pop()




class Fondo():
    def __init__(self):
        self.img_fondo = pygame.image.load("escuela.jpg")  # Carga una imagen de fondo para el tablero
        return
    
    def dibuja(self, screen):
        """
        Dibuja el fondo del tablero en la pantalla.
        
        Args:
            screen (Surface): La superficie de la pantalla donde se dibujará el fondo.
        """
        rectangulo = self.img_fondo.get_rect()  # Obtiene el rectángulo de la imagen de fondo
        rectangulo.left = 0  # Posiciona el fondo en la esquina superior izquierda
        rectangulo.top = 0
        screen.blit(self.img_fondo, rectangulo)  # Dibuja el fondo en la pantalla
        return


class Cuerpo():
    def __init__(self, x, y):
        """
        Inicializa un objeto de la clase Cuerpo.

        Args:
            x (int): La coordenada x inicial del cuerpo.
            y (int): La coordenada y inicial del cuerpo.
        """
        self.x = x
        self.y = y

    def dibujar(self, screen):
        """
        Dibuja el cuerpo en la pantalla.

        Args:
            screen (Surface): La superficie de la pantalla donde se dibujará el cuerpo.
        """
        # El cuerpo
        # Por simplicidad, vamos a dibujar un rectángulo
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.x, self.y, 20, 20))


pygame.init()  # Inicializa pygame
