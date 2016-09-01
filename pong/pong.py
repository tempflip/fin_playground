import pygame
from pygame.locals import *
import time


SCALING = 10

class World:
	def __init__(self, space):
		self.max_x = space[0]
		self.max_y = space[1]
		self.obstacle_list = []
		self.ball_list = []

	def add_obstacles(self, obst_list):
		for obstacle in obst_list:
			obstacle.set_world(self)
			self.obstacle_list.append(obstacle)

	def add_balls(self, bl):
		for ball in bl:
			ball.set_world(self)
			self.ball_list.append(ball)

	def next_step(self):
		for ball in self.ball_list:
			ball.move()


class Obstacle:
	def __init__(self, x, y, w, h):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.score = 0
		self.penalty = 0

	def set_world(self, world):
		self.world = world

	def draw(self, surface, color):
		pygame.draw.rect(surface, color, (self.x * SCALING, self.y * SCALING, self.w * SCALING, self.h * SCALING), 1)

	def is_touching(self, x, y):

		x_touch = x >= self.x and x < (self.x + self.w)
		y_touch = y >= self.y and y < (self.y + self.h)

		if (x_touch == True and y_touch == True):
			print ':', x, y

		return x_touch and y_touch 

	def set_score(self, v):
		self.score = v

	def set_penalty(self, v):
		self.penalty = v

	def __str__(self):
		return "OBST {} {} {} {}".format(self.x, self.y, self.w, self.h)


class Bat(Obstacle):
	def __init__(self, x, y):
		Obstacle.__init__(self, x, y, 1, 10)

	def down(self):
		collision = False
		for obstacle in self.world.obstacle_list:
			if (obstacle == self): continue
			if obstacle.is_touching(self.x, self.y + self.h): collision = True

		if collision: return;

		self.y = self.y + 1

	def up(self):
		collision = False
		for obstacle in self.world.obstacle_list:
			if (obstacle == self): continue
			if obstacle.is_touching(self.x, self.y): collision = True

		if collision: return;

		self.y = self.y - 1


class Border(Obstacle):
	def __init__(self, x, y, w, h):
		Obstacle.__init__(self, x, y, w, h)

class Ball:
	def __init__(self, coords, speed_vector):
		self.x = coords[0]
		self.y = coords[1]

		self.speed_vector = speed_vector

		self.score = 0
		self.penalty = 0

	def set_world(self, world):
		self.world = world

	def move(self):
		for obst in self.world.obstacle_list:
			if obst.is_touching(self.x+self.speed_vector[0], self.y):
				self.bounce_x(obst)
				self.udate_score(obst)
			elif obst.is_touching(self.x, self.y + self.speed_vector[1]):
				self.bounce_y(obst)
				self.udate_score(obst)

		#print ("ball:", self.x, self.y)

		self.x = self.x + self.speed_vector[0]
		self.y = self.y + self.speed_vector[1]

	def draw(self, surface, color):
		pygame.draw.circle(surface, color, (self.x * SCALING + SCALING/2, self.y * SCALING + SCALING/2), 5)

	def bounce_x(self, obstacle):
		self.speed_vector = (self.speed_vector[0] * -1, self.speed_vector[1])

	def bounce_y(self, obstacle):
		self.speed_vector = (self.speed_vector[0], self.speed_vector[1] * -1)

	def udate_score(self, obst):
		self.score += obst.score
		self.penalty += obst.penalty


def draw_score(score, penalty, surface, color):
	font = pygame.font.Font(None, 30)
	text = font.render("{} / {}".format(score, penalty), 1, color)
	surface.blit(text, (400, 100))

def main():
	background_color = (250, 250, 250)
	obst_color = (250,1,1)

	## settint up the world
	space = [60, 60]

	world = World(space)

	bat = Bat(5, 10)
	bat.set_score(2)

	border_up =Border (0, 0, 60, 1)
	border_down = Border(0, 59, 60, 1)
	border_left =Border (0, 0, 1, 60)
	border_left.set_penalty(2)
	border_right = Border (59, 0, 1, 60)
	border_right.set_score(1)
	center = Border(30, 15, 1, 20)

	ball = Ball((10, 15), (1,1))

	world.add_obstacles([bat, border_up, border_down, border_left, border_right, center])
	world.add_balls([ball])

	## setting up the visualisation
	pygame.init()
	screen = pygame.display.set_mode([space[0] * SCALING, space[1] * SCALING])
	pygame.display.set_caption('Pong')

	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill(background_color)

	border_up.draw(background, obst_color)
	border_down.draw(background, obst_color)
	border_left.draw(background, obst_color)
	border_right.draw(background, obst_color)
	center.draw(background, obst_color)

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
		draw_score(ball.score, ball.penalty, background, background_color)

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

		draw_score(ball.score, ball.penalty, background, obst_color)


		screen.blit(background, (0, 0))
		pygame.display.flip()


		#print ("FPS: {}".format( 1 / (time.time() - frame_start) ))

if __name__ == '__main__': main()