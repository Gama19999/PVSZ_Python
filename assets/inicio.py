import pygame as pg
from pygame.locals import *

import os

from assets.controls import *

class Inicio():
	def __init__(self, screen):
		self.screen = screen
		self.conf_surf = pg.transform.scale(pg.image.load(os.path.join('images','home','conf_surf.png')), (290,240))
		self.rect = screen.get_rect()
		self.w, self.h = self.screen.get_size()
		self.bg_img = pg.image.load(os.path.join('images','home','back_ini.jpg')) # Backgroun inicio
		self.buttons = []
		self.font = pg.font.Font(os.path.join('fonts','Base.ttf'), 30)
		self.music_muted = False

		self.setup()

	def setup(self):
		self.bg_settings = pg.image.load(os.path.join('images','controls','settings.png'))
		
		# Buttons declaration
		self.btn_settings = Button(self.screen.get_width() - 80, 50, 50, 50, self.bg_settings, 'btn_settings', self.fun_settings) # Settings button
		self.btn_vol_up = Button(self.screen.get_width() - 300, 165, 50, 50, pg.image.load(os.path.join('images','controls','volume_up.png')), 'vol_up', self.fun_vol_up) # Vol_up button
		self.btn_vol_down = Button(self.screen.get_width() - 103, 165, 50, 50, pg.image.load(os.path.join('images','controls','volume_down.png')), 'vol_down', self.fun_vol_down) # Vol_down button
		self.btn_mute = Button(self.screen.get_width() - 200, 165, 50, 50, pg.image.load(os.path.join('images','controls','mute.png')), 'mute', self.fun_mute) # Mute button
		self.buttons.extend([self.btn_settings, self.btn_vol_up, self.btn_vol_down, self.btn_mute])

		# Music setup
		pg.mixer.music.load(os.path.join('sounds','intro.mp3'))
		pg.mixer.music.play(loops=-1)

	def draw_stuff(self):
		self.screen.blit(pg.transform.scale(self.bg_img, self.screen.get_size()), (0,0))

		self.buttons[0].rect = pg.Rect(self.screen.get_width() - 80, 50, 50, 50) # Adjust settings button position
		self.buttons[1].rect = pg.Rect(self.screen.get_width() - 300, 165, 50, 50) # Adjust vol_up button position
		self.buttons[2].rect = pg.Rect(self.screen.get_width() - 103, 165, 50, 50) # Adjust vol_down button position
		self.buttons[3].rect = pg.Rect(self.screen.get_width() - 200, 165, 50, 50) # Adjust vol_down button position

		self.screen.blit(self.buttons[0].button, self.buttons[0].rect)

		pg.display.update()

	def get_buttons(self):
		return self.buttons

	def fun_settings(self, show):
		if show:
			self.screen.blit(self.conf_surf, (self.screen.get_width() - 323, 110))

			_vol = self.font.render('Volume Control', True, (255,255,255))
			_sha = self.font.render('Volume Control', True, (34, 34, 34))
			self.screen.blit(_vol, (self.screen.get_width() - 262, 122))
			self.screen.blit(_sha, (self.screen.get_width() - 260, 120))

			self.screen.blit(self.btn_vol_up.button, self.btn_vol_up.rect)
			self.screen.blit(self.btn_vol_down.button, self.btn_vol_down.rect)
			self.screen.blit(self.btn_mute.button, self.btn_mute.rect)

			pg.display.update()
		else:
			self.draw_stuff()

	def fun_vol_up(self, _):
		pg.mixer.music.set_volume(pg.mixer.music.get_volume() + 0.1)
		print(f'Current volume: {pg.mixer.music.get_volume()}')

	def fun_vol_down(self, _):
		pg.mixer.music.set_volume(pg.mixer.music.get_volume() - 0.1)
		print(f'Current volume: {pg.mixer.music.get_volume()}')

	def fun_mute(self, _):
		if self.music_muted:
			pg.mixer.music.unpause()
			self.music_muted = False
			self.btn_mute.button = pg.transform.scale(pg.image.load(os.path.join('images','controls','mute.png')), (50,50))
		else:
			pg.mixer.music.pause()
			self.music_muted = True
			self.btn_mute.button = pg.transform.scale(pg.image.load(os.path.join('images','controls','unmute.png')), (50,50))

		print(f'Music muted: {self.music_muted}')


