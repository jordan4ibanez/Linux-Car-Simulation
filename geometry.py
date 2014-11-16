import math
from input import *

class geometry_calc():
	def __init__(self):
		#initialize all math variables
		if "variables" in globals():
			direction = input().steering_input()
			
			for i in range(len(body)):
				body_points[i+1] = int(math.sin(body[i+1])*body_size+ posx), int(math.cos(body[i+1])*body_size + posy)
			#make this use ints and divide to get float for cleaner stuff
			if direction == "left":
				#steering_angle = steering_angle - steering_rate
				for i in range(len(body)):
					body[i+1] = body[i+1] + steering_rate
			if direction == "right":
				#steering_angle = steering_angle + steering_rate
				for i in range(len(body)):
					body[i+1] = body[i+1] - steering_rate
			if direction == "none":
				pass #straighten
			print(steering_angle)
	#def rotation(self): #reminder
			
			
		else:
			print("Initializing Geometric Variables")
			global variables
			variables = True
			#globalize everything for reuse, but neatly in groups in the order they're assigned
			global superpi,picorrection  
			global steering_angle,steering_rate,steering_lock
			global body_size,center,posx,posy,body,rear_left,rear_right,front_left,front_right
			global wheel_front_left,wheel_front_right,wheel_rear_left,wheel_rear_right
			global wheel_size
			global front_wheels
			global rear_wheels
			global body_points
			
			#Pi
			superpi = math.pi * 2 #equal to 360
			picorrection = 0.01744444444 #do this due to 360 degrees equalling 6.28
			
			#Steering
			steering_degree = 0 #actual steering degree (float)
			steering_angle  = 0 #a whole number up to 1000 down to -1000 (int)
			steering_rate   = 0.001
			steering_lock   = 0.5
			
			#Body Corners
			body_size = 100
			center = posx,posy = 450,450
			body = {}
			body[1] = 205 * picorrection#"front_left"
			body[2] = 155 * picorrection#"front_right"
			body[3] = 25  * picorrection#"rear_left"
			body[4] = 335 * picorrection#"rear_right"
			
			#TODO: rotate the wheels hubs with the corners of the body for deformation purposes
			#wheel hubs - on this vehicle, it's fr -5 fl +5 deg -30% total length to get hub points to where the tires will pivot off of
			wheel_front_left  = 210 * picorrection
			wheel_front_right = 150 * picorrection
			wheel_rear_left   = 330 * picorrection
			wheel_rear_right  = 30  * picorrection
			
			#Wheel Size (Tire) -- here you can change the size IF YOU DARE!
			wheel_size = 20
			
			#FRONT WHEELS
			front_wheels = {}
			front_wheels["front_left"]  = 205 * picorrection
			front_wheels["front_right"] = 155 * picorrection
			front_wheels["rear_left"]   = 25  * picorrection
			front_wheels["rear_right"]  = 335 * picorrection
			
			#REAR WHEELS
			rear_wheels = {}
			rear_wheels["rear_left"]   = 25  * picorrection
			rear_wheels["rear_right"]  = 335 * picorrection
			rear_wheels["front_left"]  = 205 * picorrection
			rear_wheels["front_right"] = 155 * picorrection
			
			
			#========================================================================================#
			# Now convert all angles to usable points, and have them global for further modification #
			#========================================================================================#
			
			#THE BODY
			body_points = {}
			for i in range(len(body)):
				body_points[i+1] = int(math.sin(body[i+1])*body_size+ posx), int(math.cos(body[i+1])*body_size + posy)
			
	def return_points_to_render(self):
		return(body_points)

