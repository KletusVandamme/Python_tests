# This Class defines my rotating box
import pygame, sys, random, math
from settings import *
from polygon_SETTINGS import *

screen_width, screen_height = 1000, 1000
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)


class Point(object):
	def __init__(self, angle_deg, radius,new_CS = (100,100)): 
		self.angle_deg = angle_deg
		self.radius = radius
		self.new_CS = new_CS		
	def get_cartesian(self):
		self.x = self.radius*math.sin(self.angle_deg*(math.pi/180))
		self.y = self.radius*math.cos(self.angle_deg*(math.pi/180))
		self.loc = (self.x, self.y)
		self.new_loc = (int(self.x + self.new_CS[0]), int(self.y + self.new_CS[1]))
	def draw(self):
		pygame.draw.circle(screen, BLUE, self.new_loc, 5, 0)

	

class Poly(object):
	def __init__(self,no_vertices, diameter, color=RED, loc =(100,100)): 
		self.no_vertices = no_vertices
		self.diameter = diameter
		self.color = color
		self.loc = loc
		# create a set of blank vertices
		self.vertices = []
		for vertex in range (0, self.no_vertices):
			point = Point(angle_deg=0, radius=self.diameter, new_CS = self.loc)
			self.vertices.append(point)
	def draw(self, deg, loc):
		#set the angle between teh vertices
		angle_delta = 360/self.no_vertices

		#draw vertices
		for vertex in range (0,(self.no_vertices)):
			#set the polar coordinates angle for each vertex
			self.vertices[vertex].angle_deg = deg + angle_delta*vertex
			#set the origin for each poly
			self.vertices[vertex].loc = self.loc
			self.vertices[vertex].get_cartesian()
			self.vertices[vertex].draw()
		#draw lines
		for vertex in range (0, self.no_vertices-1):
			#draw all lines but last one
			pygame.draw.line(screen, RED, self.vertices[vertex].new_loc, self.vertices[vertex+1].new_loc, 1)
		#draw last line
		pygame.draw.line(screen, RED, self.vertices[len(self.vertices)-1].new_loc, self.vertices[0].new_loc, 1)