import pygame
import config as cf  # Importa el módulo config.py, asumiendo que contiene la clase Config que tiene un atributo deltaT_s
import math

class Juego():
    def __init__(self):
        self.este_tablero = Tablero()  # Inicializa un objeto Tablero
        self.este_cuerpo = Cuerpo(200, 100, 150, 35)  # Inicializa un objeto Cuerpo con coordenadas, velocidad y ángulo dados
        return
    
    def dibuja(self, screen):
        """
        Dibuja el tablero y el cuerpo en la pantalla.
        
        Args:
            screen (Surface): La superficie de la pantalla donde se dibujarán los objetos.
        """
        self.este_tablero.dibuja(screen)  # Llama al método dibuja de Tablero para dibujar el fondo
        self.este_cuerpo.dibuja(screen)  # Llama al método dibuja de Cuerpo para dibujar el cuerpo
        return
    
    def actualiza_variables(self):
        """Actualiza las variables del juego."""
        self.este_cuerpo.avanza()  # Llama al método avanza de Cuerpo para actualizar la posición del cuerpo
    
class Tablero():
    def __init__(self):
        self.img_fondo = pygame.image.load("hubble2.bmp")  # Carga una imagen de fondo para el tablero
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
    def __init__(self, pr_coord_x, pr_coord_y, pr_velocidad_pxs, pr_alfa_grados):
        """
        Inicializa un objeto Cuerpo con coordenadas, velocidad y ángulo dados.
        
        Args:
            pr_coord_x (float): Coordenada x inicial del cuerpo.
            pr_coord_y (float): Coordenada y inicial del cuerpo.
            pr_velocidad_pxs (float): Velocidad del cuerpo en píxeles por segundo.
            pr_alfa_grados (float): Ángulo inicial del cuerpo en grados.
        """
        self.x = pr_coord_x  # Establece la coordenada x inicial
        self.y = pr_coord_y  # Establece la coordenada y inicial
        self.velocidad = pr_velocidad_pxs  # Establece la velocidad del cuerpo
        self.a_grados = pr_alfa_grados  # Establece el ángulo del cuerpo
        return
    
    def dibuja(self, screen):
        """
        Dibuja el cuerpo en la pantalla.
        
        Args:
            screen (Surface): La superficie de la pantalla donde se dibujará el cuerpo.
        """
        color = (255, 0, 0)  # Color rojo
        pygame.draw.circle(screen, color, (self.x, self.y), 20)  # Dibuja un círculo en las coordenadas del cuerpo
        return
    
    def avanza(self):
        """Actualiza la posición del cuerpo según su velocidad y ángulo."""
        a_radianes = math.radians(self.a_grados)  # Convierte el ángulo a radianes
        velocidad_x = self.velocidad * math.cos(a_radianes)  # Calcula la velocidad en x
        velocidad_y = self.velocidad * math.sin(a_radianes)  # Calcula la velocidad en y
        self.x = self.x + velocidad_x * cf.Config.deltaT_s  # Actualiza la coordenada x
        self.y = self.y + velocidad_y * cf.Config.deltaT_s  # Actualiza la coordenada y
        # Si el cuerpo sale de los límites de la pantalla, lo hace reaparecer en el lado opuesto
        if self.x > 800: self.x = 0
        if self.y > 600: self.y = 0
        if self.x < 0: self.x = 800
        if self.y < 0: self.y = 600
        return
