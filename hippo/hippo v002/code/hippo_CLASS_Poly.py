# This Class defines my rotating box
import pygame, sys, random, math
from hippo_SETTINGS import *

class Rect(object):
	def __init__(self, x, y, w, h, thickness, color): 
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.right = self.x + self.w
		self.bottom = self.y + self.h
		self.thickness = thickness
		self.color = color
		self.hover = False
		self.click = False
		self.grab = False
		self.drop = False
		
	def draw(self):
		pygame.draw.rect(screen, self.color, [self.x, self.y, self.w, self.h], self.thickness)

	def detect_hover(self):
		mouse_x, mouse_y = pygame.mouse.get_pos()
		self.right = self.x + self.w
		self.bottom = self.y + self.h
		if mouse_x > self.x and mouse_x < self.right and mouse_y > self.y and mouse_y < self.bottom:
			self.hover = True
		else:
			self.hover = False

	def detect_grab(self):
		if pygame.mouse.get_pressed()[0] == 1:
			click = True
		else:
			click = False
		# if hover is detected, leave it on indefinately, until a drop is detected.  This prevents the grab from being canceled if the mouse moves faster than the screen can detect.
		self.detect_hover()
		if click == True and self.hover == True:
			self.grab = True

	def detect_drop(self):
		if pygame.mouse.get_pressed()[0] == 0 and self.grab == True:
			self.grab = False
			self.drop = True
			#remember to set it to false after you perform the drop action
			

# class Hippo(object):
# 	def __init__(self, loc): 
# 		self.angle_deg = angle_deg
# 		self.radius = radius
# 		self.poly_center = poly_center
# 		self.new_loc = (100,100)
# 		# point_color = 
# 	def beg(self):
# 		self.x = self.radius*math.sin(self.angle_deg*(math.pi/180))
# 		self.y = self.radius*math.cos(self.angle_deg*(math.pi/180))
# 		self.new_loc = (int(self.x + self.poly_center[0]), int(self.y + self.poly_center[1]))
# 		return self.new_loc
# 	def chew(self):
# 		pygame.draw.circle(screen, BLUE, self.new_loc, 5, 0)
# 	def poop(self):
# 		pygame.draw.circle(screen, BLUE, self.new_loc, 5, 0)

# class Poly(object):
# 	def __init__(self,no_vertices, diameter, color=RED, loc =(100,100), move_x=10, move_y=10, radius=50, spin_rate_deg=10, rot_angle_deg=10): 
# 		self.no_vertices = no_vertices
# 		self.diameter = diameter
# 		self.color = color
# 		self.loc = loc
# 		self.move_x = move_x
# 		self.move_y = move_y
# 		self.radius = radius
# 		self.spin_rate_deg = spin_rate_deg
# 		self.rot_angle_deg = rot_angle_deg
# 		# create a set of blank vertices
# 		self.vertices = []
# 		for vertex in range (0, self.no_vertices):
# 			point = Point(angle_deg=0, radius=self.diameter, poly_center = self.loc)
# 			self.vertices.append(point)
# 	def draw():
# 		a=1
# 	def light_up():
# 		a=1
# 	def chew():
# 		a=1
# 	def poop():
# 		a=1

# 	def update_position(self, polys, poly):
# 		# move poly
# 		# find left, right and topmost vertices, to be used in detecting a wall collision

# 		for i in range (0, len(polys)):
# 			this_poly = polys[i]
# 			all_x = []
# 			all_y = []
# 			for vertex in this_poly.vertices:
# 				all_x.append(vertex.new_loc[0])
# 				all_y.append(vertex.new_loc[1])
# 			# if you are off screen, reverse direction
# 			if (max(all_x) + this_poly.move_x) >= screen_width or (min(all_x) + this_poly.move_x) <=0:
# 				this_poly.move_x = this_poly.move_x * -1
# 			if (max(all_y) + this_poly.move_y) >= screen_height or (min(all_y) + this_poly.move_y) <=0:
# 				this_poly.move_y = this_poly.move_y * -1
# 		# modify location
# 		# for poly in range (0, len(polys)):
# 			this_poly.loc = (this_poly.loc[0] + this_poly.move_x, this_poly.loc[1] + this_poly.move_y)
	
# 	def draw(self):
# 		for i in range (0,(self.no_vertices)):
# 			this_vertex = self.vertices[i]
# 			this_vertex.draw()
# 		#draw lines
# 		for i in range (0, self.no_vertices-1):
# 			this_vertex = self.vertices[i]
# 			#draw all lines but last one
# 			pygame.draw.line(screen, self.color, this_vertex.new_loc, self.vertices[i+1].new_loc, 5)
# 		#draw last line
# 		pygame.draw.line(screen, self.color, self.vertices[len(self.vertices)-1].new_loc, self.vertices[0].new_loc, 5)