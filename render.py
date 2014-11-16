import pygame
from pygame.locals import *
from geometry import *
#rendering = if the environment/objects are being rendered

class render_environment():
	def __init__(self):
		#always test if game is rendering to start the rendering
		if "rendering" in globals():
			screen.fill((0,0,0))
			#check the body points from the calculations and render them
			body_points = geometry_calc().return_points_to_render()
			for i in range(len(body_points)):
				pygame.draw.circle(screen, (255,0,0), body_points[i+1], 3)
				
			pygame.display.flip()
		else:
			print("Initializing Pygame")
			global rendering,screensize, screen
			screensize = screenh,screenw = 900, 900
			screen     = pygame.display.set_mode(screensize)
			rendering  = True
			pygame.display.set_caption("Car Physics Simulation 2D")
			pygame.init()
		
