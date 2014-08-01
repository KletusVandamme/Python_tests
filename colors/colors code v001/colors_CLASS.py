# This Class defines my rotating box

from __future__ import division
import pygame, sys, random, math
from colors_SETTINGS import *
# from matt_stuff import *


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
