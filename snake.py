
import pygame
import config as cf  # Importa el módulo config.py, asumiendo que contiene la clase Config que tiene un atributo deltaT_s
import sys
import random
tamano = (cf.SCREEN_WIDTH, cf.SCREEN_HEIGHT)  # Tamaño de la ventana del juego
screen = pygame.display.set_mode(tamano)  # Crea una ventana con el tamaño especificado

class Juego():
    def __init__(self):
        self.tablero_fondo = Fondo()
        self.snake_cuerpo = [Serpiente(100, 100)]  # Inicializa la serpiente con un solo segmento en la posición (100, 100)
        self.direccion = "RIGHT"  # Inicializa la dirección de la serpiente
        self.velocidad = 0.7 #Velocidad de la serpiente
        self.manzana = Manzana()  # Agregar la manzana al juego
        self.segmento_size = 20  # Tamaño inicial de los segmentos de la serpiente


    def movimiento_teclado(self, event): #Controles de la serpíente
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                if self.direccion != "DOWN":  # Evitar que la serpiente vaya hacia abajo si ya se está moviendo hacia arriba
                    self.direccion = "UP"
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if self.direccion != "UP":  # Evitar que la serpiente vaya hacia arriba si ya se está moviendo hacia abajo
                    self.direccion = "DOWN"
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if self.direccion != "RIGHT":  # Evitar que la serpiente vaya hacia la derecha si ya se está moviendo hacia la izquierda
                    self.direccion = "LEFT"
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if self.direccion != "LEFT":  # Evitar que la serpiente vaya hacia la izquierda si ya se está moviendo hacia la derecha
                    self.direccion = "RIGHT"


    def dibuja(self, screen): #el fondo de la imagen
        self.tablero_fondo.dibuja(screen)  # Dibuja el fondo del tablero
        for cuerpo in self.snake_cuerpo:
            cuerpo.dibujar(screen)  # Dibuja cada parte del cuerpo de la serpiente en la pantalla
        self.manzana.dibujar(screen)  # Dibujar la manzana en la pantalla


    def actualizar(self): #Para actualizar la pantalla
        cabeza_x = self.snake_cuerpo[0].x
        cabeza_y = self.snake_cuerpo[0].y


        # Verificar si la serpiente come la manzana (con un margen de 10 píxeles alrededor de la posición de la manzana)
        
        if abs(cabeza_x - self.manzana.x) < 25 and abs(cabeza_y - self.manzana.y) < 25:
            
            self.manzana.generar_posicion()  # Generar una nueva posición para la manzana
            # Aumentar el tamaño de los segmentos de la serpiente
            self.segmento_size += 900000
            # Añadir un nuevo segmento al cuerpo de la serpiente en la posición de la última cola
            nueva_cola = Serpiente(self.snake_cuerpo[-1].x, self.snake_cuerpo[-1].y)
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
        nueva_cabeza = Serpiente(cabeza_x, cabeza_y)
        self.snake_cuerpo.insert(0, nueva_cabeza)
        self.snake_cuerpo.pop()

class Fondo(): #Para que el fondo tenga una imagen
    def __init__(self):
        self.img_fondo = pygame.image.load("escuela.jpg")  # Carga una imagen de fondo para el tablero
        return
    def dibuja(self, screen): 
        rectangulo = self.img_fondo.get_rect()  # Obtiene el rectángulo de la imagen de fondo
        rectangulo.left = 0  # Posiciona el fondo en la esquina superior izquierda
        rectangulo.top = 0
        screen.blit(self.img_fondo, rectangulo)  # Dibuja el fondo en la pantalla
        return

class Serpiente(): #cuerop de la serpiente
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def dibujar(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.x, self.y, 25, 25))

class Manzana():
    def __init__(self):
        self.generar_posicion()

    def generar_posicion(self):
        self.x = random.randint(0, cf.SCREEN_WIDTH - 20)  # Posición x aleatoria dentro del ancho del tablero
        self.y = random.randint(0, cf.SCREEN_HEIGHT - 20)  # Posición y aleatoria dentro de la altura del tablero

    def dibujar(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(self.x, self.y, 25, 25))
