
import pygame
import config as cf  # Importa el módulo config.py, asumiendo que contiene la clase Config que tiene un atributo deltaT_s
import sys
import random
tamano = (cf.SCREEN_WIDTH, cf.SCREEN_HEIGHT)  # Tamaño de la ventana del juego
screen = pygame.display.set_mode(tamano)  # Crea una ventana con el tamaño especificado

class Juego():
    def __init__(self):
        self.tablero_fondo = Fondo()
        self.snake_cuerpo = [Cuerpo(100, 100)]  # Inicializa la serpiente con un solo segmento en la posición (100, 100)
        self.direccion = "RIGHT"  # Inicializa la dirección de la serpiente
        self.velocidad = 0.5 #Velocidad de la serpiente
        self.manzana = Manzana()  # Agregar la manzana al juego

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
        self.manzana.dibujar(screen)  # Dibujar la manzana en la pantalla


    def actualizar(self):
        cabeza_x = self.snake_cuerpo[0].x
        cabeza_y = self.snake_cuerpo[0].y






        print("Cabeza de la serpiente:", cabeza_x, cabeza_y)
        print("Posición de la manzana:", self.manzana.x, self.manzana.y)
        
        # Verificar si la serpiente come la manzana (con un margen de 10 píxeles alrededor de la posición de la manzana)
        if abs(cabeza_x - self.manzana.x) < 10 and abs(cabeza_y - self.manzana.y) < 10:
            print("¡La serpiente comió la manzana!")
            self.manzana.generar_posicion()  # Generar una nueva posición para la manzana
            # Añadir un nuevo segmento al cuerpo de la serpiente en la posición de la última cola
            nueva_cola = Cuerpo(self.snake_cuerpo[-1].x, self.snake_cuerpo[-1].y)
            self.snake_cuerpo.append(nueva_cola)

        if self.direccion == "UP":
            cabeza_y -= self.velocidad
        elif self.direccion == "DOWN":
            cabeza_y += self.velocidad
        elif self.direccion == "LEFT":
            cabeza_x -= self.velocidad
        elif self.direccion == "RIGHT":
            cabeza_x += self.velocidad

        if cabeza_x < 0 or cabeza_x >= cf.SCREEN_WIDTH or cabeza_y < 0 or cabeza_y >= cf.SCREEN_HEIGHT:
            mensaje = f"""¡Colisión! Game Over"""
            font = pygame.font.SysFont(None, 36)
            texto = font.render(mensaje, True, (255, 255, 255))
            screen.blit(texto, (cf.SCREEN_WIDTH // 2 - texto.get_width() // 2, cf.SCREEN_HEIGHT // 2 - texto.get_height() // 2))
            pygame.display.update()
            pygame.time.delay(4000)
            pygame.quit()
            sys.exit()

        nueva_cabeza = Cuerpo(cabeza_x, cabeza_y)
        self.snake_cuerpo.insert(0, nueva_cabeza)
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

class Manzana():
    def __init__(self):
        """
        Inicializa un objeto de la clase Manzana con una posición aleatoria.
        """
        self.generar_posicion()

    def generar_posicion(self):
        """
        Genera una posición aleatoria para la manzana dentro del área del tablero.
        """
        self.x = random.randint(0, cf.SCREEN_WIDTH - 20)  # Posición x aleatoria dentro del ancho del tablero
        self.y = random.randint(0, cf.SCREEN_HEIGHT - 20)  # Posición y aleatoria dentro de la altura del tablero

    def dibujar(self, screen):
        """
        Dibuja la manzana en la pantalla.

        Args:
            screen (Surface): La superficie de la pantalla donde se dibujará la manzana.
        """
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(self.x, self.y, 20, 20))
