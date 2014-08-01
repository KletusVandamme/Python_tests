# This Class defines my rotating box
import pygame, sys, random, math
from settings import *
from polygon_SETTINGS import *

class Point(object):
	def __init__(self, angle_deg, radius, poly_center): 
		self.angle_deg = angle_deg
		self.radius = radius
		self.poly_center = poly_center
		self.new_loc = (100,100)
		# point_color = 
	def get_cartesian(self):

		self.x = self.radius*math.cos(self.angle_deg*(math.pi/180))
		self.y = self.radius*math.sin(self.angle_deg*(math.pi/180))
		self.new_loc = (int(self.x + self.poly_center[0]), int(self.y + self.poly_center[1]))
		return self.new_loc
	def draw(self):
		pygame.draw.circle(screen, BLUE, self.new_loc, 5, 0)


def run_game(): 
	pygame.init()
	
	my_point = Point(10, 100, (400,400))
	
	while True:
		for i in range (0,360):
			my_point.angle_deg = i
			my_point.get_cartesian()
		
			screen.fill(GRAY)

			my_point.draw()
			pygame.draw.circle(screen, BLUE, (400,400), 5, 0)

			pygame.display.update()
			pygame.time.wait(10)
			print my_point.new_loc
			#wait for ESCAPE keypress
			for event in pygame.event.get(): 
				keys = pygame.key.get_pressed()
				if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
					pygame.quit()
					sys.exit()



run_game()
