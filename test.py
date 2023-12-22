import pygame as pg
from pygame.locals import *

import os

from assets.controls import Button

# CONTROLS
controls = []

# Watch for exit, resize or termination event
def closing(surface):
	state = True
	for e in pg.event.get():
		match e.type:
			case pg.KEYDOWN:
				if e.key == pg.K_ESCAPE:
					state = False
			case pg.QUIT:
				state = False
			case pg.VIDEORESIZE:
				to_inicio(surface)
	return state

# Watch for mouse events
def watch_mouse(objects):
	for obj in objects:
		obj.process()

# Resize component and repaint
def resized(surface, component, size, positionInSurf):
	surface.blit(pg.transform.scale(component, size), positionInSurf)
	pg.display.flip()

def to_inicio(surface, restartMusic=False):
	bg_inicio = pg.image.load(os.path.join('images','back_ini.jpg')) # Background inicio
	surface.blit(pg.transform.scale(bg_inicio, surface.get_size()), (0,0))
	pg.display.flip()

	bg_settings = pg.image.load(os.path.join('images','settings.png')) # Settings button
	x = surface.get_width() - 80
	y = 50
	settings = Button(x, y, 50, 50, bg_settings, surface)
	controls.append(settings)

	if restartMusic:
		pg.mixer.music.load(os.path.join('sounds','intro.mp3')) # Music inicio
		pg.mixer.music.play(loops=-1)

def main():
	# Basic elements
	pg.mixer.init()
	pg.init()
	clock = pg.time.Clock() # Clock to control FPS
	screen = pg.display.set_mode((800, 500), pg.RESIZABLE) # Create the Surface
	
	# Set customs for game
	pg.display.set_icon(pg.image.load(os.path.join('images','icon.png'))) # Icon
	pg.display.set_caption('Plants VS Zombies') # Window title

	to_inicio(screen, True) # Shows the inicio view and starts the bg music

	# Game loop
	while closing(screen):

		watch_mouse(controls)
		
		clock.tick(60)



if __name__ == '__main__':
	main()