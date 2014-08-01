# this code tests numpy array funtions

from __future__ import division
import pygame, sys, random, math
from numpy import *
pygame.init()
# threed_array[0,0,0]


def basic_tests():
	def print_array():
		print "print array"
		print new_array
		print ""

	# initialize array
	num_row = 3
	num_col = 5
	new_array = zeros((num_row,num_col))
	print_array()

	# programatically replace values
	place(new_array, new_array==0, 5)

	#set single value
	new_array[2,2] = 8

	# get single value
	print "get single value"
	print new_array[2,2]
	print ""

	print_array()

	flip = transpose(new_array)
	print "transposed array"
	print flip

	# get a column from array
	col = flip[:,2]
	print "columm"
	print col
	print ""


	row = []
	test2 = [][]
	for i in range (0,4):
		for j in range (0,4):
			print "i,j", i, j
			test2[0] = 5 #(10*i + j)

	print "test2"
	print test2
	print ""




def look_for_quit():
	for event in pygame.event.get(): 
		keys = pygame.key.get_pressed()
		if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
			pygame.quit()
			sys.exit()


BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 153, 0)
BLUE = (51, 51, 255)
YELLOW = (255, 255, 100)
basic_tests()
