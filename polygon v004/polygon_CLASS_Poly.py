# This Class defines my rotating box
import pygame, sys, random, math
from settings import *
from polygon_SETTINGS import *

screen_width, screen_height = 1000, 1000
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)


class Point(object):
	def __init__(self, angle_deg, radius, poly_center = (100,100)): 
		self.angle_deg = angle_deg
		self.radius = radius
		self.poly_center = poly_center
		self.new_loc = (100,100)
	def get_cartesian(self):
		self.x = self.radius*math.sin(self.angle_deg*(math.pi/180))
		self.y = self.radius*math.cos(self.angle_deg*(math.pi/180))
		# self.loc = (self.x, self.y)
		self.new_loc = (int(self.x + self.poly_center[0]), int(self.y + self.poly_center[1]))
		# print "self.new_cs = ", self.new_CS
	def draw(self):
		pygame.draw.circle(screen, BLUE, self.new_loc, 5, 0)

	

class Poly(object):
	def __init__(self,no_vertices, diameter, color=RED, loc =(100,100), move_x=10, move_y=10, radius=50): 
		self.no_vertices = no_vertices
		self.diameter = diameter
		self.color = color
		self.loc = loc
		self.move_x = move_x
		self.move_y = move_y
		self.radius = radius
		# create a set of blank vertices
		self.vertices = []
		for vertex in range (0, self.no_vertices):
			point = Point(angle_deg=0, radius=self.diameter, poly_center = self.loc)
			self.vertices.append(point)
	def update_position(self, polys, poly):
		# move poly

		# all_vertices = []
		# for poly in polys:
		# 	for vertex in poly.vertices:
		# 		print vertex.poly_center
		# 		print vertex.new_loc
		# 		all_vertices.append(vertex.new_loc)


		# if you are off screen, reverse direction
		if (polys[poly].loc[0] + self.move_x + self.radius) >= screen_width or (polys[poly].loc[0] + self.move_x - self.radius) <=0:
			self.move_x = self.move_x * -1
		if (polys[poly].loc[1] + self.move_y + self.radius) >= screen_height or (polys[poly].loc[1] + self.move_y - self.radius) <=0:
			self.move_y = self.move_y * -1
		# modify location
		polys[poly].loc = (polys[poly].loc[0] + self.move_x, polys[poly].loc[1] + self.move_y) #polys[poly].loc[0] + 10
	def draw(self, deg):
		#set the angle between the vertices
		angle_delta = 360/self.no_vertices

		#draw vertices
		for vertex in range (0,(self.no_vertices)):
			#set the polar coordinates angle for each vertex
			self.vertices[vertex].angle_deg = deg + angle_delta*vertex
			#set the origin for each poly
			self.vertices[vertex].poly_center = self.loc
			self.vertices[vertex].get_cartesian()
			self.vertices[vertex].draw()
		#draw lines
		for vertex in range (0, self.no_vertices-1):
			#draw all lines but last one
			pygame.draw.line(screen, RED, self.vertices[vertex].new_loc, self.vertices[vertex+1].new_loc, 5)
		#draw last line
		pygame.draw.line(screen, RED, self.vertices[len(self.vertices)-1].new_loc, self.vertices[0].new_loc, 5)