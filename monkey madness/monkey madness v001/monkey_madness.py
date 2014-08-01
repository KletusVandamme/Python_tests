#started 26Dec2013
#test
from pygame.locals import *
import pygame, sys, random, math
from monkey_CLASS import *
from monkey_SETTINGS import *

def run_game():
	#create monkey and define parameters
	monkey = Monkey(monkey_image)
	init_monkey(monkey)

	#segment text and store in array
	word_segment_array = []
	game_text = "This simulated Python code is where Mambo the Monkey gets her workout! !"

	#create substrings from main string
	run = True
	x = 120
	y = 400
	length = 0
	height = 0
	box_buffer = 4

	#
	while run == True:
		#fix this, last segment gets it wrong
		loc = game_text.find(" ")
		string_sub = game_text[:loc] + " "
		game_text = game_text[(loc+1):]
		if loc<0:
			run = False

		##### use code below to calculate string length
		length = myfont.size(string_sub)[0]
		height = myfont.size(string_sub)[1]
		my_seg = Text_Segment(x, y, string_sub, WHITE, False, False, False)
		my_seg.box_buffer = box_buffer
		my_seg.string_length = length
		my_seg.string_height = height
		x += length
		word_segment_array.append(my_seg)

	#set which bananas to display
	i = len(word_segment_array)
	# word_segment_array[0].line_start = True
	# word_segment_array[i-1].line_end = True
	word_segment_array[i-3].show_banana = True
	word_segment_array[i-4].show_banana = True
	word_segment_array[i-5].show_banana = True
	word_segment_array[i-5].highlight = True


	#define screen objects
	pygame.init()
	pygame.display.set_caption('Monkey Madness!!!')
	pygame.display.update()	

	monkey.left_arm.y = word_segment_array[0].y + 40
	monkey.right_arm.y = word_segment_array[0].y + 40

	#create arrays of monkey positions and instructions
	instructions = ["CMD-RIGHT", "CMD-RIGHT", "OPTION-LEFT", "OPTION-LEFT", "OPTION-SHIFT-LEFT (x3)", "OPTION-SHIFT-LEFT (x3)", "OPTION-SHIFT-LEFT (x3)", "CTRL-C", "CTRL-C", "CTRL-C"]
	left_pos =  [0, 0,12,11,11,10, 9, 8]
	right_pos = [0,12,12,12,11,11,11,11]
	for i in range (0,len(left_pos)):
		# highlight word segment if required
		
		#create simulated game play
		screen.blit(back_image, (0,0))
		#calculate left arm position and draw
		monkey.left_arm.x = word_segment_array[left_pos[i]].x - 15
		monkey.left_arm.calc_joint_pos()
		#calculate right arm position and draw
		monkey.right_arm.x = word_segment_array[right_pos[i]].x + 0
		monkey.right_arm.calc_joint_pos()
		#calculate monkey position
		monkey.x = (monkey.right_arm.x - monkey.left_arm.x)/2 + monkey.left_arm.x - 10
		monkey.y = min(monkey.left_arm.y, monkey.right_arm.y) + 50;
		monkey.calc_shoulder_pos()

		#draw instructions box and instructions
		instruction_font = pygame.font.SysFont("Emilbus Mono", 25)
		x = 400
		y = 250
		w = 300
		h = 30
		font_height = 25
		pygame.draw.rect(screen, GRAY, [x,y-h,w,50])
		pygame.draw.rect(screen, BLUE, [x,y-h,w,50],1)
		box_title_text = "Keyboard Shortcut to Use"
		button_text(box_title_text, (x+ w/2 - instruction_font.size(box_title_text)[0]/2, y - h*.75), BLACK, font_height)

		pygame.draw.rect(screen, GRAY, [x,y,w,h])
		pygame.draw.rect(screen, BLUE, [x,y,w,h],1)
		#center instruction text
		intruction_length = instruction_font.size(instructions[i])[0]
		intruction_width = instruction_font.size(instructions[i])[1]
		button_text(instructions[i], (x+ w/2 - intruction_length/2, y +h/2 - intruction_width/2), BLACK, font_height)

		#draw monkey parts
		monkey.left_arm.draw()
		monkey.right_arm.draw()
		monkey.draw()
		#draw biceps
		pygame.draw.line(screen, BROWN, (monkey.shoulder_left_x, monkey.shoulder_left_y), (monkey.left_arm.joint_x, monkey.left_arm.joint_y),6)
		pygame.draw.line(screen, BROWN, (monkey.shoulder_right_x, monkey.shoulder_right_y), (monkey.right_arm.joint_x, monkey.right_arm.joint_y),6)
		#draw word segments
		for seg in word_segment_array:
			seg.draw()
		pygame.display.update()
		pygame.time.wait(400)




	wait_for_input()
#------------------------------------------------------------------------------
 
def wait_for_input():
	mouseClicked = False
	while mouseClicked == False: 
		
		for event in pygame.event.get(): 
			keys = pygame.key.get_pressed() 

			if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
				pygame.quit()
				sys.exit()	
			# if event.type == MOUSEBUTTONUP:
			# 	mousex, mousey = event.pos
			# 	# Identifies if yes or no button has been clicked
			# 	is_yes_button = mousex >= yes_button_x and mousex < yes_button_x + yes_button_w and mousey >= yes_button_y and mousey <yes_button_y + yes_button_h
			# 	is_no_button = mousex >= no_button_x and mousex < no_button_x + no_button_w and mousey >= no_button_y and mousey < no_button_y + no_button_h
			# 	if is_yes_button or is_no_button:
			# 		mouseClicked = True	

			# 	# Depending on which button (Y/N) was clicked, assigns user_input
			# 	if is_yes_button:
			# 		user_input = True
			# 	elif is_no_button:
			# 		 user_input = False
			# # Allows game play using Right and Left keyboard strokes
			if event.type == pygame.KEYDOWN:
				if keys[pygame.K_LEFT]: 
					user_input = True
					mouseClicked = True	
				if keys[pygame.K_RIGHT]: 
					user_input = False
					mouseClicked = True	
			
def init_monkey(monkey):
	monkey.shoulder_left_x_offset = 0
	monkey.shoulder_left_y_offset = 30

	monkey.shoulder_right_x_offset = -4
	monkey.shoulder_right_y_offset = 35

	monkey.left_arm.l = 18
	monkey.left_arm.w = 37
	monkey.left_arm.joint_offset_x = 0
	monkey.left_arm.joint_offset_y = 30


	monkey.right_arm.l = 18
	monkey.right_arm.w = 35
	monkey.right_arm.joint_offset_x = 15
	monkey.right_arm.joint_offset_y = 30

	monkey.left_arm.image = arm_left
	monkey.right_arm.image = arm_right

run_game()
