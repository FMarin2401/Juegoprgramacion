import pygame  # Importa el módulo pygame para trabajar con gráficos y sonido
from pygame.math import Vector2  # Importa la clase Vector2 del módulo pygame.math para manipular vectores
import random  # Importa el módulo random para generar números aleatorios
import os  # Importa el módulo os para trabajar con rutas de archivos

pygame.init()  # Inicializa pygame

ANCHO = 720  # Ancho de la ventana del juego
ALTO = 480  # Alto de la ventana del juego

# Carga las imágenes del juego y las redimensiona
SNAKE_BODY = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Administrator\Desktop\SNAKETUTO\images\snakebody.png")),(20,20))
APPLE = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Administrator\Desktop\SNAKETUTO\images\manzana.png")),(20,20))
SNAKE_HEAD = []

for x in range(1,5):
	SNAKE_HEAD+=[pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\Administrator\Desktop\SNAKETUTO\images\SnakeHead"+str(x)+".png")),(20,20))]
EAT_SOUND = pygame.mixer.Sound("coin.wav")  # Carga el sonido de comer
WIN = pygame.display.set_mode((ANCHO,ALTO))  # Crea una ventana con el tamaño especificado
SCORE_TEXT = pygame.font.SysFont("Russo One",15)  # Define una fuente para el texto del puntaje

class Snake:
	def __init__(self):
		self.body = [Vector2(20,100),Vector2(20,110),Vector2(20,120)]  # Inicializa el cuerpo de la serpiente con posiciones predefinidas
		self.direction = Vector2(0,-20)  # Inicializa la dirección de la serpiente hacia arriba
		self.add = False  # Inicializa el indicador para añadir un bloque de cuerpo extra

	def draw(self):
		# Dibuja el cuerpo de la serpiente
		for bloque in self.body:
			WIN.blit(SNAKE_BODY,(bloque.x,bloque.y))

		# Dibuja la cabeza de la serpiente según la dirección actual
		if self.direction == Vector2(0,-20):
			WIN.blit(SNAKE_HEAD[0],(self.body[0].x,self.body[0].y))

		if self.direction == Vector2(0,20):
			WIN.blit(SNAKE_HEAD[2],(self.body[0].x,self.body[0].y))

		if self.direction == Vector2(20,0):
			WIN.blit(SNAKE_HEAD[1],(self.body[0].x,self.body[0].y))

		if self.direction == Vector2(-20,0):
			WIN.blit(SNAKE_HEAD[3],(self.body[0].x,self.body[0].y))

	def move(self):
		# Mueve la serpiente
		if self.add == True:
			body_copy = self.body
			body_copy.insert(0,body_copy[0]+self.direction)
			self.body = body_copy[:]
			self.add = False
		else:
			body_copy = self.body[:-1]
			body_copy.insert(0,body_copy[0]+self.direction)
			self.body = body_copy[:]

	def move_up(self):
		# Cambia la dirección de la serpiente hacia arriba
		self.direction = Vector2(0,-20)

	def move_down(self):
		# Cambia la dirección de la serpiente hacia abajo
		self.direction = Vector2(0,20)

	def move_right(self):
		# Cambia la dirección de la serpiente hacia la derecha
		self.direction = Vector2(20,0)

	def move_left(self):
		# Cambia la dirección de la serpiente hacia la izquierda
		self.direction = Vector2(-20,0)

	def die(self):
		# Verifica si la serpiente choca con los bordes de la ventana o consigo misma
		if self.body[0].x >= ANCHO+20 or self.body[0].y >= ALTO+20 or self.body[0].x <= -20 or self.body[0].y <= -20:
			return True

		# Verifica si la serpiente choca consigo misma
		for i in self.body[1:]:
			if self.body[0] == i:
				return True

class Apple:
	def __init__(self):
		self.generate()  # Genera una manzana en una posición aleatoria

	def draw(self):
		# Dibuja la manzana en pantalla
		WIN.blit(APPLE,(self.pos.x,self.pos.y))

	def generate(self):
		# Genera una nueva posición para la manzana
		self.x = random.randrange(0,ANCHO/20)
		self.y = random.randrange(0,ALTO/20)
		self.pos = Vector2(self.x*20,self.y*20)

	def check_collision(self,snake):
		# Verifica si la serpiente come la manzana
		if snake.body[0] == self.pos:
			self.generate()
			snake.add = True
			return True

		# Verifica si la manzana aparece en una posición ocupada por la serpiente
		for bloque in snake.body[1:]:
			if self.pos == bloque:
				self.generate()

		return False

def main():
	# Inicializa la serpiente, la manzana y el puntaje
	snake = Snake()
	apple = Apple()
	score = 0

	fps = pygame.time.Clock()

	while True:
		fps.tick(30)  # Controla la velocidad de actualización de la pantalla

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()

			# Maneja los eventos de teclado para cambiar la dirección de la serpiente
			if event.type == pygame.KEYDOWN and snake.direction.y != 20:
				if event.key == pygame.K_UP:
					snake.move_up()

			if event.type == pygame.KEYDOWN and snake.direction.y != -20:
				if event.key == pygame.K_DOWN:
					snake.move_down()

			if event.type == pygame.KEYDOWN and snake.direction.x != -20:
				if event.key == pygame.K_RIGHT:
					snake.move_right()

			if event.type == pygame.KEYDOWN and snake.direction.x != 20:
				if event.key == pygame.K_LEFT:
					snake.move_left()
						
		WIN.fill((175,215,70))  # Llena la pantalla con un color de fondo

		snake.draw()  # Dibuja la serpiente
		apple.draw()  # Dibuja la manzana

		snake.move()  # Mueve la serpiente

		if apple.check_collision(snake):
			score+=1
			EAT_SOUND.play()  # Reproduce el sonido de comer

		# Verifica si la serpiente choca y termina el juego
		snake.die()
		if snake.die():
			quit()

		# Muestra el puntaje en pantalla
		text = SCORE_TEXT.render("Score: {}".format(score),1,(255,255,255))
		WIN.blit(text,(ANCHO-text.get_width()-20,20))

		pygame.display.update()  # Actualiza la pantalla

main()  # Llama a la función main para iniciar el juego
