from settings import *
import pygame, sys, random
pygame.init()

###########################################################################################################
# This is all test code for unit testing
# myfont = 5
card1_x = 0
card1_y = 0
card1_w = 10
card1_h = 10
card1_color = BLACK
card1_text_color = RED
card_font = 5

# def run_game():
# 	#test button
# 	yes_button = Text_Box(yes_button_x, yes_button_y, yes_button_w, yes_button_h, BLACK, WHITE, "YES", myfont)
# 	yes_button.display()
# 	yes_button.print_data()

# 	#test card
# 	card1 = Card("Card1")
# 	card1.text_box(card1_x, card1_y, card1_w, card1_h, card1_color, card1_text_color, "string",card_font)
# 	card1.button.display()
# 	card1.create_data()
# 	card1.print_data()

###########################################################################################################

# class Screen():
# 	def __init__(self):
# 		a=1
# 	def display_scoreboard_text(loc1, loc2, loc3, loc4, loc5):
# 		button_text("# of Rounds", loc1, BLACK, scoreb_font_size)
# 		button_text("Max # of Rounds", loc2, BLACK, scoreb_font_size)
# 		button_text("Correct Answers", loc3, BLACK, scoreb_font_size)
# 		button_text("Incorrect Answers", loc4, BLACK, scoreb_font_size)
# 		button_text("Score", loc5, BLACK, scoreb_font_size)
# 	def draw_fixed_objs(self,rect1):
# 		yes_button.display

class Card(object):
	def __init__(self,card_label="card label"): 
		self.card_label = card_label
	def text_box(self,x,y,width,height,color, text_color,string,font):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.color = color
		self.text_color = text_color
		self.string = string
		self.font = font
		self.card_text_box = Text_Box(x,y,width,height,color, text_color,"",font)

	def create_data(self, color=1, word=1, word_text="nil", color_text="nil"):   
		# this is untested, but should allow 1 dictionary to be used for generating both the word and color and providing the name of the color
		color_value = random.randint(1, 4)
		word_value = random.randint(1, 4)
		self.word = card_data[word_value][0]
		self.word_color = card_data[color_value][1]
		self.color_name = card_data[color_value][0]

	def display_data(self):
		temp = Text_Box(self.x,self.y,self.width,self.height,self.color, self.word_color,self.word,self.font)
		temp.display()	

	def print_data(self, color=1, word=1, word_text="nil", color_text="nil"):   
		print "-----------------"
		print "card data: "
		print "-----------------"
		print "color = ", self.color	
		print "color_name = ", self.color_name
		print "word = ", self.word
		print "-----------------"	

	def is_answer_correct(user_input, correct_answer): 
		# Reviews whether answer is correct and increment score
		if user_input == correct_answer: 
			score += 10
			true_answers += 1
		elif user_input != correct_answer: 
			false_answers +=1

class Text_Box(object):
		def __init__(self,x,y,width,height,color, text_color,string,font):
			self.x = x
			self.y = y
			self.w = width
			self.h = height
			self.color = color
			self.text_color = text_color
			self.string = string
			self.font = font
			
			self.rect = Rectangle(self.x,self.y,self.w,self.h,self.color)

			self.string_length = myfont.size(self.string)[0] ##### use code below to calculate string length
			self.string_height = myfont.size(self.string)[1]  

			self.text_x = self.rect.horz_center - self.string_length/2
			self.text_y = self.rect.vert_center - self.string_height/2

			self.text = Text(self.string, self.text_x, self.text_y, self.text_color, self.font)

		def display(self):
			self.rect.display()
			self.text.display()

		def print_data(self):
			self.rect.print_data()
			print()
			self.text.print_data()

			# button_text(card2_data.word_text,(card2_rect.horz_center - card_font.size(str(card2_data.word_text))[0]/2, card2_rect.vert_center - text_height/2), card2_data.color_text)

class Text():
	def __init__(self, string="dummy_string", x=0, y=0, color=BLACK, font=myfont):
		self.myfont = myfont
		self.x = x
		self.y = y
		self.string = string
		self.color = color
		
	def display(self):
		label = self.myfont.render(self.string, 1, self.color)
		screen.blit(label, (self.x, self.y))

	def print_data(self):
		#for diagnostic purposes
		print "-----------------"
		print "text details: "
		print "-----------------"
		print "string = ", self.string	
		print "x = ", self.x
		print "y = ", self.y
		print "color = ", self.color
		print "font = ", self.myfont	
		print "-----------------"


class Rectangle():
	def __init__(self, x, y, width, height, color):
		self.color = color
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.vert_center = self.y + height/2
		self.horz_center = self.x + width/2
		self.right = self.x + self.width
		self.bottom = self.y + self.height

	def display(self):
		a=1
		pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, self.height])	
		pygame.draw.rect(screen, BLACK, [self.x, self.y, self.width, self.height], 1)
		
	def print_data(self):
		# print("rect test")
		print "-----------------"
		print "rect details: "
		print "-----------------"
		print "x = ", self.x	
		print "y = ", self.y	
		print "w = ", self.width	
		print "h = ", self.height	
		print "color = ", self.color	
		print "-----------------"

		# def print_data(self):
		# # print("rect test")
		# print "-----------------"
		# print("rect details: ")
		# print("-----------------")
		# print("x = ", self.x)	
		# print("y = ", self.y)	
		# print("w = ", self.width)	
		# print("h = ", self.height)	
		# print("color = ", self.color)	
		# print("-----------------")

###########################################################################################################		


# run_game()
