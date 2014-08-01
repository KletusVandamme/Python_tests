# This Class defines my rotating box
#test
import pygame, sys, random, math
from monkey_SETTINGS import *

#this is used below in getting the text dimensions in pixels.
# I need to move this
myfont = pygame.font.SysFont("Emilbus Mono", 20)

class Monkey(object):
	def __init__(self, image):
		self.image = image
		self.x = 0
		self.y = 0
		self.w = 41
		self.h = 82  
		self.shoulder_left_x_offset = 0
		self.shoulder_right_x_offset = 0
		self.shoulder_left_y_offset = 0
		self.shoulder_right_y_offset = 0
		self.shoulder_left_x = 0
		self.shoulder_left_y = 0
		self.shoulder_right_x = 0
		self.shoulder_right_y = 0
		self.left_arm = Arm(image)
		self.right_arm = Arm(image)
	
	def calc_shoulder_pos(self):
		self.right = self.x + self.w
		self.bottom = self.y + self.h
		self.shoulder_left_x = self.x + self.shoulder_left_x_offset
		self.shoulder_left_y = self.y + self.shoulder_left_y_offset
		self.shoulder_right_x = self.right + self.shoulder_right_x_offset
		self.shoulder_right_y = self.y + self.shoulder_right_y_offset

	def draw(self):
		screen.blit(self.image, (self.x, self.y))

class Arm(object):
	def __init__(self, image):
		self.image = image
		self.x = 0
		self.y = 0
		self.w = 0
		self.h = 0
		self.right = self.x + self.w
		self.bottom = self.y + self.h
		self.joint_offset_x = 0
		self.joint_offset_y = 0
		self.joint_x = 0
		self.joint_y = 0

	def calc_joint_pos(self):
		self.joint_x = self.x + self.joint_offset_x
		self.joint_y = self.y + self.joint_offset_y

	def draw(self):
		screen.blit(self.image, (self.x, self.y))

class Rect1(object):
	def __init__(self, x, y, w, h, thickness, color): 
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.right = self.x + self.w
		self.bottom = self.y + self.h
		self.thickness = thickness
		self.color = color
		
	def draw(self):
		pygame.draw.rect(screen, self.color, [self.x, self.y, self.w, self.h], self.thickness)
			
class Text_Segment(object):
	def __init__(self, x, y, text, color, ital, line_start, line_end): 
		self.x = x
		self.y = y
		self.text = text
		self.color = color
		# self.ital = ital
		# self.line_start = line_start
		# self.line_end = line_end
		self.string_length = 0
		self.string_height = 0
		# create self.rect with dummy values that will be replaced in the main program
		self.rect = Rect1(self.x, self.y,self.string_length,2,1,BLUE)
		self.box_buffer = 4
		self.show_banana = False
		self.highlight = False

	def draw(self):
		#draw highlight
		if self.highlight == True:
			self.rect = Rect1(self.x, self.y, (self.string_length),self.string_height,0,GRAY)
			self.rect.draw()
		#draw frame around word
		self.rect = Rect1(self.x, self.y, (self.string_length),self.string_height,1,BLUE)
		self.rect.draw()
		button_text(self.text, (self.rect.x + self.box_buffer , self.rect.y), self.color, 50)
		#draw banana
		if self.show_banana == True:
			screen.blit(banana, (self.x -12 + self.string_length/2, self.y-25))
			self.color = YELLOW


			

def button_text(text_display, (location_x, location_y), color=BLACK, font_size=30):
	myfont = pygame.font.SysFont("Emilbus Mono", font_size)
	label = myfont.render(text_display, 1, color)
 	screen.blit(label, (location_x, location_y))


