import pygame
import numpy as np
import math
import random
import colorsys

from CONST import *

def calcvel(angle):
	v = [0, 0]

	v[0] = -math.cos(angle)

	v[1] = -math.sin(angle)

	return v

x0, y0 = WIDTH//2, HEIGHT//2

class Particle():
	def __init__(self, x, y, r, color, angle):
		self.pos = [x, y]
		self.vel = [0, 0]
		self.acc = [0, 0]
		self.r = r
		self.col = color
		self.angle = angle
		self.is_enemy = False
		self.lifespan = 255

	def set_player_vel(self):
		self.vel = [0, 0]

	def set_bullet_vel(self):
		v = calcvel(self.angle)
		v[0] *= -5
		v[1] *= -5
		self.vel = [v[0], v[1]]

	def set_enemy_vel(self):
		v = calcvel(self.angle)
		mult = 7-(self.r-5)*4/15

		print(mult)
		self.vel = [v[0]*mult, v[1]*mult]
		self.is_enemy = True

	def set_part_vel(self):
		v = calcvel(self.angle)
		mult = random.uniform(1, 3)
		self.vel = [v[0]*mult, v[1]*mult]
		self.is_enemy = True

	def done(self):
		x1, y1 = self.pos
		if (x1-x0)*(x1-x0) + (y1-y0)*(y1-y0) < (20+self.r)*(20+self.r)-100:
			return True
		return False

	def applyForce(self, force):
		self.acc[0] += force[0]
		self.acc[1] += force[1]

	def update(self):
		self.vel[0] += self.acc[0]
		self.vel[1] += self.acc[1]
		self.pos[0] += self.vel[0]
		self.pos[1] += self.vel[1]
		self.acc = [0, 0]

	def draw(self, screen):
		if self.lifespan >0:
			if self.is_enemy:
				c = colorsys.hsv_to_rgb(self.col, 1, 1)
				c = (int(c[0]*255), int(c[1]*255), int(c[2]*255))
				pygame.draw.circle(screen, c, (self.pos[0], self.pos[1]), self.r)

			else:
				try:
					pygame.draw.circle(screen, self.col, (self.pos[0], self.pos[1]), self.r)
				except:
					pygame.draw.circle(screen,WHITE, (self.pos[0], self.pos[1]), self.r)