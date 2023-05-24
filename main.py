import pygame
import numpy as np
import math
import random
from player import Player
from enemy import Enemy
from CONST import *


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
lost = False
score = 0
max_score = 0

def draw_rect_alpha(surface, color, rect):
    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
    surface.blit(shape_surf, rect)

def draw(screen, player, enemys):
	global lost
	global score
	if not lost:
		draw_rect_alpha(screen, (0, 0, 0, 51), (0,0, WIDTH, HEIGHT))
		# screen.fill(BACKGROUND)

		for enemy in enemys:
			enemy.update()
			enemy.draw(screen)
			if enemy.kill and enemy.exit:
				lost = True
			for bullet in player.bullets:
				if enemy.collide(bullet):
					player.bullets.remove(bullet)
					enemy.enemy.r -= bullet.R
					if enemy.enemy.r <= 5:
						enemy.exit = False

					elif enemy.enemy.r < 12:
						enemy.enemy.r = 8

			if not enemy.exit and len(enemy.parts) == 0:
				enemys.remove(enemy)
				score += 10

		player.update()
		player.draw(screen)

	if lost:
		screen.fill(BACKGROUND)

	pygame.display.update()


def main():
	global lost
	global score
	global max_score
	player = Player()
	enemys = [Enemy()]
	shootloop = 0
	enemyloop = 0

	run = True
	while run:
		clock.tick(30)
		if shootloop > 0:
			shootloop += 1
		if shootloop > 5:
			shootloop = 0
		if not lost:
			if enemyloop > 0:
				enemyloop += 1
			if enemyloop > 20:
				enemyloop = 0
			if random.randrange(0, 100) < 3 and enemyloop == 0:
				enemys.append(Enemy())
				enemyloop += 1

		draw(screen, player, enemys)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				pass
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN and lost:
					lost = False
					player = Player()
					enemys = [Enemy()]
					if score > max_score:
						max_score = score
					score = 0

		left, mid, right = pygame.mouse.get_pressed()

		if left and shootloop == 0:
			x, y = pygame.mouse.get_pos()
			player.shoot(x, y)
			shootloop +=1

	pygame.quit()

main()
