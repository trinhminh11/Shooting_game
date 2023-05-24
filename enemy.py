import pygame
import numpy as np
import math
import random
from particle import Particle
from CONST import *

x0, y0 = WIDTH//2, HEIGHT // 2

def random2D():
	angle = random.uniform(0, math.pi*2)
	x = SPAWN_POINT*math.cos(angle) + x0
	y = SPAWN_POINT*math.sin(angle) + y0
	return [x, y], angle

class Enemy():
	def __init__(self):
		self.pos, self.angle = random2D()
		self.color = random.uniform(0, 1)
		self.enemy = Particle(self.pos[0], self.pos[1], random.uniform(5,20), self.color, self.angle)
		self.enemy.set_enemy_vel()
		self.parts = []
		self.kill = False
		self.exit = True

	def update(self):
		for part in self.parts:
			part.update()
			part.lifespan -= 20
			if part.lifespan <= 0:
				self.parts.remove(part)
		self.enemy.update()
		if self.enemy.done():
			self.kill = True

	def collide(self, bullet):
		x = self.enemy.pos[0] - bullet.bullet.pos[0]
		y = self.enemy.pos[1] - bullet.bullet.pos[1]
		r = self.enemy.r + bullet.bullet.r
		dist = x*x+y*y
		if dist < r*r:

			for i in range(300):
				self.parts.append(Particle(self.enemy.pos[0], self.enemy.pos[1], random.uniform(0, 3), self.color, random.uniform(0, math.pi*2)))
				self.parts[i].set_part_vel()

			return True

		return False

	def draw(self, screen):
		for part in self.parts:
			part.draw(screen)
		if self.exit:
			self.enemy.draw(screen)




