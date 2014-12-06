import pygame,sys
from pygame.locals import *

class input():
	#Temporarily treat the whole class as a function
	def __init__(self):
		if "keypress" in globals():
			pass
		else:
			print("Initializing Key Input")
			global keypress
		keypress = pygame.key.get_pressed()
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		if keypress[K_ESCAPE]:
			sys.exit()
			
			
	def steering_input(self):
		if keypress[K_LEFT]:
			return("left")
		if keypress[K_RIGHT]:
			return("right")
			
		return("none")
		
	def throttle_input(self):
		if keypress[K_UP]:
			return("up")
		if keypress[K_DOWN]:
			return("down")
			
		return("none")
