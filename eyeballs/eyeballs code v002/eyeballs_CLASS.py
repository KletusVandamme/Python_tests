# This Class defines my rotating box
#test
from __future__ import division
import pygame, sys, random, math
from eyeballs_SETTINGS import *
# from matt_stuff import *


# eye_image
class Eye_image(object):
	def __init__ (self, x, y, w, h, eye_image_back, eye_image_front, eye_image_iris):
		self.y = y
		self.x = x
		self.w = w
		self.h = h
		self.right = self.x + self.w
		self.bottom = self.y + self.h
		self.center_x = self.x + self.w/2
		self.center_y = self.y + self.h/2
		self.eye_image_back = eye_image_back
		self.eye_image_front = eye_image_front
		self.eye_image_iris = eye_image_iris

		# self.iris_x = self.x
		# self.iris_y = self.y
		self.iris_w = 41
		self.iris_h = 40
		self.iris_offset_x = 0
		self.iris_offset_y = 0

		self.target_x = 0
		self.target_y = 0

	def calc_iris_offest(self):
		x_distance = (self.target_x - self.center_x)
		y_distance = (self.target_y - self.center_y)
		x = 0
		z = 0
		y = 0.01
		y_increment = 0.01
		iris_radius = 10
		# this gets rid of the glitchy cases when y or x = 0
		if y_distance == 0:
			x = z* (x_distance/math.fabs(x_distance))
			y = 0
		elif x_distance == 0:
			y = z* (y_distance/math.fabs(y_distance))
			x = 0
		else:
			slope = y_distance/x_distance
			# use a trial and error method to find a new x and y, to find the correct z
			# when you have find the correct z, the x and y are correct
			# you use the slope of the angle between the eye and the bird
			while z <= iris_radius:
				y += y_increment
				x = y/slope
				z = math.sqrt(x*x + y*y)
			#account for z having negative roots
			if y_distance < 0:
				x *= -1
				y *= -1
			self.iris_offset_x = int(x)
			self.iris_offset_y = int(y)

	def calc_center(self):
		self.center_x = self.x + self.w/2
		self.center_y = self.y + self.h/2		
	def draw (self):
		self.calc_center()
		self.calc_iris_offest()
		screen.blit(self.eye_image_back, (self.x,self.y))
		screen.blit(self.eye_image_iris, ((self.center_x + self.iris_offset_x - self.iris_w/2),(self.center_y + self.iris_offset_y - self.iris_h/2)))
		screen.blit(self.eye_image_front, (self.x,self.y))
		# pygame.draw.circle(screen, BLUE, (self.center_x, self.center_y), 2, 0)
		# pygame.draw.circle(screen, RED, (self.center_x + self.iris_offset_x, self.center_y + self.iris_offset_y), 1, 0)

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
		self.is_in_mouth = False
		self.x_move = 5
		self.y_move = 5
		
	def draw(self):
		pygame.draw.rect(screen, self.color, [self.x, self.y, self.w, self.h], self.thickness)

	def detect_hover(self):
		mouse_x, mouse_y = pygame.mouse.get_pos()
		self.right = self.x + self.w
		self.bottom = self.y + self.h
		if mouse_x > self.x and mouse_x < self.right and mouse_y > self.y and mouse_y < self.bottom:
			self.hover = True
			self.color = BLUE
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
			self.color = RED

	def detect_drop(self):
		if pygame.mouse.get_pressed()[0] == 0 and self.grab == True:
			self.grab = False
			self.drop = True
			#remember to set it to false after you perform the drop action
	def detect_in_mouth(self, mouth_rect):
		if self.x > mouth_rect.x and self.x < mouth_rect.right and self.y > mouth_rect.y and self.y < mouth_rect.bottom:
			self.color = SLATE
			self.is_in_mouth = True
			self.x = food_rect_x
			self.y = food_rect_y

			
# global main_loop_iteration
class Hippo(object):
	def __init__(self, x, y, hippo_image_open, hippo_image_closed): 
		self.x = x
		self.y = y
		self.is_beg = True
		self.is_chew  = False
		self.is_poop = False
		self.hippo_image_open = hippo_image_open
		self.hippo_image_closed = hippo_image_closed
	def beg(self, main_loop_iteration):
		a=1
	def chew(self):
		a = 1
	def poop(self):
		a = 1
	def draw(self, main_loop_iteration):
		# print self.is_beg
		if self.is_beg ==True:
			if main_loop_iteration%50 >= 0 and main_loop_iteration%50 <= 25:
				hippo_image = self.hippo_image_open
			else:
				hippo_image = self.hippo_image_closed
		else:
			hippo_image = self.hippo_image_closed
		screen.blit(hippo_image, (self.x,self.y))


def draw_var_watches():
	a = "hover = " + str(my_rect.hover)
	b = "grab = " + str(my_rect.grab)
	c =  "drop = " + str(my_rect.drop)
	d =  "click = " + str(my_rect.click)

	spacing = 30
	button_text(a, (200, 200 + 1*spacing), color=BLACK, font_size=30)
	button_text(b, (200, 200 + 2*spacing), color=BLACK, font_size=30)
	button_text(c, (200, 200 + 3*spacing), color=BLACK, font_size=30)
	button_text(d, (200, 200 + 4*spacing), color=BLACK, font_size=30)
	print a
	print b
	print c
	print d
	print "----------"


