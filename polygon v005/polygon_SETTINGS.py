
import pygame, sys, random, math

screen_width, screen_height = 600, 600
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

num_poly = 2
num_vertex = 3
center = (500,500)
radius = 100
polys = []
move_x = 10
move_y = 15
rotation_increment_deg = 0