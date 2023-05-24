import pygame
import numpy as np
import math
import random
from particle import Particle
from CONST import *

x0, y0 = WIDTH//2, HEIGHT//2

class Bullet():
	R = 5
	COLOR = WHITE
	def __init__(self, angle):
		self.bullet = Particle(x0, y0, self.R, self.COLOR, angle)
		self.bullet.set_bullet_vel()

	def update(self):
		self.bullet.update()

	def draw(self, screen):
		self.bullet.draw(screen)