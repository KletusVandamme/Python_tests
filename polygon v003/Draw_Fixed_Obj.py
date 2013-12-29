from settings import*
from classes import *
# from functions import *
	

def button_text(text_display, (location_x, location_y), color=BLACK, font_size=30):
	myfont = pygame.font.SysFont("Arial", font_size)
	label = myfont.render(text_display, 1, color)
	screen.blit(label, (location_x, location_y))

def display_scoreboard_text(loc1, loc2, loc3, loc4, loc5):
	button_text("# of Rounds", loc1, BLACK, scoreb_font_size)
	button_text("Max # of Rounds", loc2, BLACK, scoreb_font_size)
	button_text("Correct Answers", loc3, BLACK, scoreb_font_size)
	button_text("Incorrect Answers", loc4, BLACK, scoreb_font_size)
	button_text("Score", loc5, BLACK, scoreb_font_size)

def draw_fixed_objs():
	# Displays unchanging screen decorations
	# Displays game box
	game = Rectangle(game_x, game_y, game_w, game_h, MATT_03)
	game.display()
	# Displays instruction box and blit text in box
	instr = Rectangle(instr_x, instr_y, instr_w, instr_h, MATT_02)
	instr.display()
	instr_text_loc = (instr.horz_center - instr_font.size("Does the Box 1 word match the Box 2 font color?")[0]/2, instr_y + 15)
	button_text("Does the Box 1 word match the Box 2 font color?", instr_text_loc, BLACK, 18)
	#Displays scoreboard
	display_sb = Rectangle(banner_x, banner_y, banner_w, banner_h, MATT_01)
	display_sb.display()
	display_scoreboard_text(rounds_text_loc, max_rounds_text_loc, true_answers_text_loc, false_answers_text_loc, score_text_loc)
	# Displays card labels
	button_text("Box 1", card1_label, BLACK, box_label_text_height)
	button_text("Box 2", card2_label, BLACK, box_label_text_height)
	# Displays yes button and instructions
	yes_button = Rectangle(yes_button_x, yes_button_y, yes_button_w, yes_button_h, MATT_04)
	yes_button.display()
	button_text("Click box or use left arrow", yes_button_note, BLACK, 15)

	# Displays no button and instructions
	no_button = Rectangle(no_button_x, no_button_y, no_button_w, no_button_h, MATT_04)
	no_button.display()
	button_text("Click box or use right arrow", no_button_note, BLACK, 15)
	# Blits text in Yes and No buttons
	yes_text_loc = (yes_button.horz_center - y_button_font.size("YES")[0]/2, yes_button.vert_center - text_height/2)
	no_text_loc = (no_button.horz_center - y_button_font.size("NO")[0]/2, no_button.vert_center - text_height/2)
	button_text("YES", yes_text_loc, BLACK, 24)
	button_text("NO", no_text_loc, BLACK, 24)

def flash_card(): 
		# Displays card1 box
		card1_text_color = RED
		card1 = Card("Card1")
		card1.text_box(card1_rect_x, card1_rect_y, card1_rect_w, card1_rect_h, MATT_05, card1_text_color, "string", myfont)
		card1.card_text_box.display()
		card1.create_data()
		card1.print_data()
		card1.display_data()
		# Displays card2 box
		card2_text_color = BLUE
		card2 = Card("Card2")
		card2.text_box(card2_rect_x, card2_rect_y, card2_rect_w, card2_rect_h, MATT_05, card1_text_color, "string", myfont)
		card2.card_text_box.display()
		card2.create_data()
		card2.print_data()
		card2.display_data()

# test_Card()
	

		
# 		data_right_edge = game_x - border
# # 		# Writes and displays score to screen
# 		score_data = button_text(str(score), (data_right_edge - scoreb_font.size(str (score))[0], score_text_loc[1]), BLACK,scoreb_font_size)
# 		# Writes and displays Current # of rounds to screen
# 		curr_rounds_data = button_text(str(current_no_of_rounds), (data_right_edge - scoreb_font.size(str (current_no_of_rounds))[0], rounds_text_loc[1]), BLACK,scoreb_font_size)
# 		# Writes and displays Max # of Rounds to screen
# 		max_rounds_data = button_text(str(max_no_rounds), (data_right_edge - scoreb_font.size(str (max_no_rounds))[0], max_rounds_text_loc[1]), BLACK,scoreb_font_size)
# 		# Writes and displays # True Answers to screen
# 		true_answers_data = button_text(str(true_answers), (data_right_edge - scoreb_font.size(str (true_answers))[0], true_answers_text_loc[1]), BLACK,scoreb_font_size)
# 		# Writes and displays # of False answers to screen
# 		false_answers_data = button_text(str(false_answers), (data_right_edge - scoreb_font.size(str (false_answers))[0], false_answers_text_loc[1]), BLACK,scoreb_font_size)


	# high_score = my_high_score.read_file()
	# button_text(str(high_score), (border,400), BLACK, 24)
	# high_score = my_high_score.read_file()