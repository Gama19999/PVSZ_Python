import pygame as pg
from pygame.locals import *

import os

from assets.controls import *

class Inicio():
	def __init__(self, screen):
		self.screen = screen
		self.rect = screen.get_rect()
		self.w, self.h = self.screen.get_size()
		self.bg_img = pg.image.load(os.path.join('images','back_ini.jpg')) # Backgroun inicio
		self.buttons = []

		self.setup()

	def setup(self):
		self.bg_settings = pg.image.load(os.path.join('images','settings.png')) # Settings button
		x = self.screen.get_width() - 80
		y = 50
		self.btn_settings = Button(x, y, 50, 50, self.bg_settings, 'btn_settings', self.fun_settings)
		self.buttons.append(self.btn_settings)

		pg.mixer.music.load(os.path.join('sounds','intro.mp3')) # Music inicio
		pg.mixer.music.play(loops=-1)

	def draw_stuff(self):
		self.screen.blit(pg.transform.scale(self.bg_img, self.screen.get_size()), (0,0))

		for btn in self.buttons:
			x = self.screen.get_width() - 80
			y = 50
			btn.rect = pg.Rect(x,y,50,50)
			self.screen.blit(btn.button, btn.rect)

		pg.display.update()

	def get_buttons(self):
		return self.buttons

	def fun_settings(self, show):
		if show:
			self.conf_surf = pg.image.load(os.path.join('images','conf_surf.jpg'))
			self.screen.blit(self.conf_surf, (self.screen.get_width() - 440, 110))
			pg.display.update()
		else:
			self.draw_stuff()

