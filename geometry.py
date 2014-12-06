import math
from input import *

class geometry_calc():
	def __init__(self):
		#initialize all math variables
		if "variables" in globals():
						
			#make this use ints and divide to get float for cleaner stuff
			direction = input().steering_input()
			if direction == "left":
				if steering_angle  < steering_lock:
					steering_angle += steering_rate
					for i in range(len(hub)):
						front_wheels[i+1]  = front_wheels[i+1]  + steering_rate
			else:
				if steering_angle  > 0:
					steering_angle -= steering_rate
					for i in range(len(hub)):
						front_wheels[i+1]  = front_wheels[i+1]  - steering_rate
			if direction == "right":
				if steering_angle  > -steering_lock:
					steering_angle -= steering_rate
					for i in range(len(hub)):
						front_wheels[i+1]  = front_wheels[i+1]  - steering_rate
			else:
				if steering_angle  < 0:
					steering_angle += steering_rate
					for i in range(len(hub)):
						front_wheels[i+1]  = front_wheels[i+1] + steering_rate
	
			throttle = input().throttle_input()
			rotation_speed = steering_angle/100
			if throttle == "up":
				new_x, new_y = math.sin(rotation), math.cos(rotation)
				posx    = posx - new_x
				posy    = posy - new_y
				rotation += rotation_speed
				for i in range(len(hub)):
						body[i+1] = body[i+1] + rotation_speed
						hub[i+1]  = hub[i+1]  + rotation_speed
						rear_wheels[i+1]  = rear_wheels[i+1]  + rotation_speed
						front_wheels[i+1]  = front_wheels[i+1]  + rotation_speed
			if throttle == "down":
				new_x, new_y = math.sin(rotation), math.cos(rotation)
				posx    = posx + new_x
				posy    = posy + new_y
				rotation -= rotation_speed
				for i in range(len(hub)):
						body[i+1] = body[i+1] - rotation_speed
						hub[i+1]  = hub[i+1]  - rotation_speed
						rear_wheels[i+1]  = rear_wheels[i+1]  - rotation_speed
						front_wheels[i+1]  = front_wheels[i+1]  - rotation_speed	


			##TESTING ROTATION
			test = False
			rotation_speed = 0.001
			if test == True:
				rotation = rotation - rotation_speed
				for i in range(len(body)):
						body[i+1] = body[i+1] - rotation_speed
				for i in range(len(hub)):
						hub[i+1]  = hub[i+1]  - rotation_speed
						rear_wheels[i+1]  = rear_wheels[i+1]  - rotation_speed
						front_wheels[i+1]  = front_wheels[i+1]  - rotation_speed
			
			
					
			#MAKE SURE POINTS ARE IN REAL BOUNDARIES
			if rotation > superpi:
					rotation = 0
			if rotation < 0:
					rotation = superpi
			for i in range(len(body)):
				if body[i+1] > superpi:
					body[i+1] = 0
				if body[i+1] < 0:
					body[i+1] = superpi
			for i in range(len(hub)):
				if hub[i+1] > superpi:
					hub[i+1] = 0
				if hub[i+1] < 0:
					hub[i+1] = superpi	
			for i in range(len(front_wheels)):
				if front_wheels[i+1] > superpi:
					front_wheels[i+1] = 0
				if front_wheels[i+1] < 0:
					front_wheels[i+1] = superpi
			for i in range(len(rear_wheels)):
				if rear_wheels[i+1] > superpi:
					rear_wheels[i+1] = 0
				if rear_wheels[i+1] < 0:
					rear_wheels[i+1] = superpi
					
			#BODY, HUBS, WHEELS
			for i in range(len(body)):
				body_points[i+1] = int(math.sin(body[i+1])*body_size+ posx), int(math.cos(body[i+1])*body_size + posy)
			for i in range(len(hub)):
				hub_points[i+1] = int(math.sin(hub[i+1])*70+ posx), int(math.cos(hub[i+1])*70 + posy) #EVENTUALLY HAVE THIS USE A VALUE FOR HUB SPACING
			for a in range(0,2):
				wheels[a+1] = {}
				if a == 0:
					for b in range(0,2):
						wheels[a+1][b+1] = {}
						for c in range(0,4):
							wheels[a+1][b+1][c+1] = int(math.sin(front_wheels[c+1]) * wheel_size + hub_points[b+1][0]), int(math.cos(front_wheels[c+1]) * wheel_size + hub_points[b+1][1])
				if a == 1:
					for b in range(2,4):
						wheels[a+1][b+1] = {}
						for c in range(0,4):
							wheels[a+1][b+1][c+1] = int(math.sin(rear_wheels[c+1]) * wheel_size + hub_points[b+1][0]), int(math.cos(rear_wheels[c+1]) * wheel_size + hub_points[b+1][1])
		else:
			print("Initializing Geometric Variables")
			global variables
			variables = True
			#globalize everything for reuse, but neatly in groups in the order they're assigned
			global superpi,picorrection  
			global steering_angle,steering_rate,steering_lock
			global rotation,body_size,center,posx,posy,body
			global hub
			global wheel_size
			global front_wheels
			global rear_wheels
			global body_points
			global hub_points
			global wheels
			
			#Pi
			superpi = math.pi * 2 #equal to 360
			picorrection = 0.01744444444 #do this due to 360 degrees equalling 6.28
			
			#Steering
			steering_degree = 0 #actual steering degree (float)
			steering_angle  = 0 #a whole number up to 1000 down to -1000 (int)
			steering_rate   = 0.001
			steering_lock   = 0.5

			
			#Body Corners
			rotation = 0
			body_size = 100
			center = posx,posy = 450,450
			body = {}
			body[1] = 205 * picorrection#"front_left"
			body[2] = 155 * picorrection#"front_right"
			body[3] = 25  * picorrection#"rear_left"
			body[4] = 335 * picorrection#"rear_right"
			#body[5] = 180 * picorrection#NOSE
			
			#TODO: rotate the wheels hubs with the corners of the body for deformation purposes
			#wheel hubs - on this vehicle, it's fr -5 fl +5 deg -30% total length to get hub points to where the tires will pivot off of
			hub = {}
			hub[1] = 210 * picorrection#"front_left"
			hub[2] = 150 * picorrection#"front_right"
			hub[3] = 30  * picorrection#"rear_left"
			hub[4] = 330 * picorrection#"rear_right"
			
			
			#Wheel Size (Tire) -- here you can change the size IF YOU DARE!
			wheel_size = 20
			
			#FRONT WHEELS
			front_wheels = {}
			front_wheels[1] = 205 * picorrection
			front_wheels[2] = 155 * picorrection
			front_wheels[3] = 25  * picorrection
			front_wheels[4] = 335 * picorrection
			
			#REAR WHEELS
			rear_wheels = {}
			rear_wheels[1] = 205 * picorrection
			rear_wheels[2] = 155 * picorrection
			rear_wheels[3] = 25  * picorrection
			rear_wheels[4] = 335 * picorrection

			
			
			#===============================================================#
			# NOW CONVERT ALL ANGLES TO USABLE POINTS                       #
			# THIS WILL ALSO BE DONE ON THE OTHER SIDE OF THIS IF STATEMENT #
			#===============================================================#
			
			#THE BODY
			body_points = {}
			for i in range(len(body)):
				body_points[i+1] = int(math.sin(body[i+1])*body_size+ posx), int(math.cos(body[i+1])*body_size + posy)
				
			#THE WHEEL HUBS
			hub_points = {}
			for i in range(len(hub)):
				hub_points[i+1] = int(math.sin(hub[i+1])*70+ posx), int(math.cos(hub[i+1])*70 + posy) #EVENTUALLY HAVE THIS USE A VALUE FOR HUB SPACING
				
			#THE WHEELS (MAIN TABLE - > A FRONT/BACK - > B WHEEL DIRECTION - > C WHEEL POINTS)
			wheels = {}
			for a in range(0,2):
				wheels[a+1] = {}
				if a == 0:
					for b in range(0,2):
						wheels[a+1][b+1] = {}
						for c in range(0,4):
							wheels[a+1][b+1][c+1] = int(math.sin(front_wheels[c+1]) * wheel_size + hub_points[b+1][0]), int(math.cos(front_wheels[c+1]) * wheel_size + hub_points[b+1][1])
				if a == 1:
					for b in range(2,4):
						wheels[a+1][b+1] = {}
						for c in range(0,4):
							wheels[a+1][b+1][c+1] = int(math.sin(rear_wheels[c+1]) * wheel_size + hub_points[b+1][0]), int(math.cos(rear_wheels[c+1]) * wheel_size + hub_points[b+1][1])
						
					
	def return_points_to_render(self):
		return(body_points,hub_points,wheels)

