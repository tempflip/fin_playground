import pygame
from pygame.locals import *
import time


SCALING = 10

class Obstacle:
	def __init__(self, x, y, w, h):
		self.x = x
		self.y = y
		self.w = w
		self.h = h

	def draw(self, surface, color):
		pygame.draw.rect(surface, color, (self.x * SCALING, self.y * SCALING, self.w * SCALING, self.h * SCALING), 1)

class Bat(Obstacle):
	def __init__(self, x, y):
		Obstacle.__init__(self, x, y, 1, 10)

	def down(self):
		self.y = self.y + 1

	def up(self):
		self.y = self.y - 1


class Border(Obstacle):
	def __init__(self, x, y, w, h):
		Obstacle.__init__(self, x, y, w, h)

class Ball:
	def __init__(self, coords, speed_vector):
		self.x = coords[0]
		self.y = coords[1]

		self.speed_vector = speed_vector

	def move(self):
		self.x = self.x + self.speed_vector[0]
		self.y = self.y + self.speed_vector[1]

	def draw(self, surface, color):
		pygame.draw.circle(surface, color, (self.x * SCALING + SCALING/2, self.y * SCALING + SCALING/2), 5)



def main():

	space = [60, 60]
	background_color = (250, 250, 250)

	bat = Bat(1, 10)
	ball = Ball((1, 15), (1,1))
	border_up =Border (0, 0, 60, 1)
	border_down = Border(0, 59, 60, 1)
	border_left =Border (0, 0, 1, 60)
	border_right =Border (59, 0, 1, 60)


	pygame.init()

	screen = pygame.display.set_mode([space[0] * SCALING, space[1] * SCALING])
	pygame.display.set_caption('Pong')

	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill(background_color)

	border_up.draw(background, (250,1,1))
	border_down.draw(background, (250,1,1))
	border_left.draw(background, (250,1,1))
	border_right.draw(background, (250,1,1))


	# Display some text
	font = pygame.font.Font(None, 36)
	text = font.render("Pong Game", 1, (10, 10, 10))
	textpos = text.get_rect()
	textpos.centerx = background.get_rect().centerx
	background.blit(text, textpos)


	# Blit everything to the screen
	screen.blit(background, (0, 0))
	pygame.display.flip()



	# Event loop
	while 1:
		frame_start = time.time()

		## clean up
		bat.draw(background, background_color )
		ball.draw(background, background_color )

		## events
		for event in pygame.event.get():
			if event.type == QUIT:
				print("OK bye!")
				return

		keys = pygame.key.get_pressed()

		if (keys[K_DOWN]): 
			bat.down()

		if (keys[K_UP]):
			bat.up()

		## do the stuff
		ball.move()

		## draw
		bat.draw(background, (44, 44, 44) )
		
		ball.draw(background, (99, 99, 99) )

		screen.blit(background, (0, 0))
		pygame.display.flip()

		print ("FPS: {}".format( 1 / (time.time() - frame_start) ))

if __name__ == '__main__': main()