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
		self.is_in_mouth = False
		
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

			# print "in mouth"

			
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
		# global main_loop_iteration
		print main_loop_iteration
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


