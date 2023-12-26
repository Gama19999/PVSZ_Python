import pygame as pg
from pygame.locals import *

import os, sys

from assets.inicio import Inicio 


# Setup
pg.mixer.init()
pg.init()
CLOCK = pg.time.Clock() # Clock to control FPS
SCREEN = pg.display.set_mode((900,600), pg.RESIZABLE) # Creates the Surface

# Set customs for screen
pg.display.set_icon(pg.image.load(os.path.join('images','icon.png'))) # Icon
pg.display.set_caption('Plants VS Zombies') # Window title

# All created views
views = {}
active_view = 'home'

# Controls
controls = []

home = Inicio(SCREEN)
home.draw_stuff()
controls.extend(home.get_buttons())
views['home'] = home


def loop():
	while True:
		for ev in pg.event.get():
			match ev.type:
				case pg.KEYDOWN:
					if ev.key == pg.K_ESCAPE:
						sys.exit()
				case pg.QUIT:
					sys.exit()
				case pg.VIDEORESIZE:
					for k,v in views.items():
						v.draw_stuff()
				case pg.MOUSEBUTTONDOWN:
					for btn in controls:
						btn.process()

		CLOCK.tick(60) # 60 FPS


if __name__ == '__main__':
	loop()