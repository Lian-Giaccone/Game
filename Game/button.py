import pygame as pg

class Button():
	def __init__(self, x, y, image):
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.click = False

	def draw(self, screen):
		action = False

		pos = pg.mouse.get_pos()

		if self.rect.collidepoint(pos):
			if pg.mouse.get_pressed()[0] == 1 and self.click == False:
				action = True
				self.click = True

		if pg.mouse.get_pressed()[0] == 0:
			self.click = False

		screen.blit(self.image, self.rect)

		return action
