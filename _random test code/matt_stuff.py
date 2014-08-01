# repository for my code snippets
def sep():
	print "----------"
def polar_to_cartesian(self,angle_deg,distance):
	x = distance*math.sin(self.angle_deg*(math.pi/180))
	y = distance*math.cos(self.angle_deg*(math.pi/180))
	
	new_loc = (int(x), int(y))
	return new_loc
			
def look_for_quit():
	for event in pygame.event.get(): 
		keys = pygame.key.get_pressed()
		if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
			pygame.quit()
			sys.exit()
