import pygame as pg
import os

# Class Button
class Button():
	def __init__(self, x, y, width, height, surfImg, idd, onclick=None):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.onclick = onclick
		self.idd = idd
		self.clicked = False

		self.button = pg.transform.scale(surfImg, (self.width, self.height))
		self.rect = pg.Rect(self.x, self.y, self.width, self.height)

	def process(self):
		if self.rect.collidepoint(pg.mouse.get_pos()): # Mouse hovering button
			print(f'HOVERING the button {self.idd}')
		
			if pg.mouse.get_pressed(num_buttons=3)[0]: # Clicked left btn
				print(f'Button {self.idd} PRESSED')
				self.clicked = False if self.clicked else True
				print(f'Button {self.idd} is PRESSED {self.clicked}')

				self.onclick(self.clicked)
		else:
			pass

