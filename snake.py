import pygame
import config as cf
import sys
import random
tamano = (cf.SCREEN_WIDTH, cf.SCREEN_HEIGHT)
screen = pygame.display.set_mode(tamano)

class Juego():
    def __init__(self):
        self.tablero_fondo = Fondo()
        self.snake_cuerpo = [Serpiente(100, 100)]
        self.direccion = "RIGHT"
        self.velocidad = 0.2
        self.manzana = Manzana()
        self.segmento_size = 2
    def movimiento_teclado(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                if self.direccion != "DOWN":
                    self.direccion = "UP"
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if self.direccion != "UP":
                    self.direccion = "DOWN"
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if self.direccion != "RIGHT":
                    self.direccion = "LEFT"
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if self.direccion != "LEFT":
                    self.direccion = "RIGHT"
    def dibuja(self, screen):
        self.tablero_fondo.dibuja(screen)
        for cuerpo in self.snake_cuerpo:
            cuerpo.dibujar(screen)
        self.manzana.dibujar(screen)
    def actualizar(self):
        cabeza_x = self.snake_cuerpo[0].x
        cabeza_y = self.snake_cuerpo[0].y
        if abs(cabeza_x - self.manzana.x) < 25 and abs(cabeza_y - self.manzana.y) < 25:
            self.manzana.generar_posicion()
            self.segmento_size += 2
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

class Fondo():
    def __init__(self):
        self.img_fondo = pygame.image.load("fondo.jpg")
        return
    def dibuja(self, screen):
        rectangulo = self.img_fondo.get_rect()
        rectangulo.left = 0
        rectangulo.top = 0
        screen.blit(self.img_fondo, rectangulo)
        return

class Serpiente():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def dibujar(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.x, self.y, 25, 25))

class Manzana():
    def __init__(self):
        self.generar_posicion()
    def generar_posicion(self):
        self.x = random.randint(0, cf.SCREEN_WIDTH - 20)
        self.y = random.randint(0, cf.SCREEN_HEIGHT - 20)
    def dibujar(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(self.x, self.y, 25, 25))
