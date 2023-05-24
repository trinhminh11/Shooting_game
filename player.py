import pygame
import numpy as np
import math
import random
from particle import Particle
from bullet import Bullet
from CONST import *


x0, y0 =WIDTH // 2, HEIGHT // 2

class Player():
	R = 20
	COLOR = WHITE
	POS = (WIDTH//2, HEIGHT//2)
	def __init__(self):
		self.player = Particle(self.POS[0], self.POS[1], self.R, self.COLOR, 0)
		self.bullets = []

	def update(self):
		for bullet in self.bullets:
			bullet.update()

	def shoot(self, x, y):
		angle = math.atan2(y-y0,x-x0)
		self.bullets.append(Bullet( angle))

	def draw(self, screen):
		for bullet in self.bullets:
			bullet.draw(screen)

		self.player.draw(screen)