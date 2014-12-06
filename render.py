import pygame
from pygame.locals import *
from geometry import *
#RENDERING = IF THE ENVIRONMENT/OBJECTS ARE BEING RENDERED

class render_environment():
	def __init__(self):
		#ALWAYS TEST IF GAME IS RENDERING TO START THE RENDERING
		if "rendering" in globals():
			
			screen.fill((0,0,0))
			
			
			#GET THE POINTS FROM THE GEOMETRY CALC CLASS AND RENDER THEM
			body_points,hub_points,wheels = geometry_calc().return_points_to_render()
			
			pygame.draw.polygon(screen, (255,255,255), [body_points[1],body_points[2],body_points[3],body_points[4]])			
			
			#THE BODY WILL BE DRAWN BEFORE THE TIRES FOR DEBUG PURPOSES
			for i in range(len(body_points)):
				pygame.draw.circle(screen, (255,0,0), body_points[i+1], 3)
				#DEBUG
				#title = font.render(str(body_points[i+1]), 1, (0,0,255))
				#screen.blit(title,body_points[i+1])
			for a in range(0,2):
				if a == 0:
					for b in range(0,2):
						render_group = []
						for c in range(0,4):
							render_group.insert(0,wheels[a+1][b+1][c+1])
						pygame.draw.polygon(screen, (0,0,255), render_group)		
				if a == 1:
					for b in range(2,4):
						render_group = []
						for c in range(0,4):
							render_group.insert(0,wheels[a+1][b+1][c+1])
						pygame.draw.polygon(screen, (0,0,255), render_group)
			for i in range(len(hub_points)):
				pygame.draw.circle(screen, (255,0,0), hub_points[i+1], 5)
						
							
			pygame.display.flip()
			
			
		else:
			print("Initializing Pygame")
			
			global rendering,screensize,screen,font
			
			screensize = screenw,screenh = 1600, 900
			screen     = pygame.display.set_mode(screensize)
			rendering  = True
			pygame.display.set_caption("Car Physics Simulation 2D")
			pygame.init()
			font = pygame.font.Font(pygame.font.get_default_font(), 12)
