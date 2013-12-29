import pygame, sys, random
pygame.init()


# Screen parameters
screen_width, screen_height = 900, 600
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
bg_color = 200, 200, 200
scoreboard_height = 50
border = 25
font_size = 18
myfont = pygame.font.SysFont("Arial", font_size)

# Set up the colors
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 153, 0)
BLUE = (51, 51, 255)
YELLOW = (255, 255, 156)
LIME = (0, 255, 0)
GRAY = (126, 126, 126) 
CYAN = (  0, 255, 255)
SKY = (135, 206, 250)
SKY2 = (176, 226, 255)
SLATE = (112, 128, 144)
MATT_01 = (102,153,102)
MATT_02 = (102,153,128)
MATT_03 = (102,153,153)        
MATT_04 = (102,128,102)
MATT_05 = (192,192,192)
background_color = SLATE

# Set up game variables
user_input = True
is_yes_button = True
is_no_button = True
score = 0
current_no_of_rounds = 0
true_answers = 0
false_answers = 0

# Set up mouse and click positions
click_position = [0, 0]
click_positions = []
mousex = 0 # used to store x coordinate of mouse event
mousey = 0 # used to store y coordinate of mouse event
mouseClicked = False
game_in_progress = True
program_running = True
number_of_rounds = 20 # this one works

max_no_rounds = 20 # this one is doing something else

text_display = " "

# DICT_color = {1: BLUE, 2: RED, 3: BLACK, 4: GREEN}
# DICT_word = {1: "BLUE", 2: "RED", 3: "BLACK", 4: "GREEN"}

card_data = {1: ("BLUE", BLUE), 2: ("RED", RED), 3: ("BLACK", BLACK), 4: ("GREEN", GREEN)}

# value = 1
# print ("card word = " , card_data[value][0])
# print ("card color = " , card_data[value][1])

# Define scoreboard box dimensions
banner_w = 350
banner_h = screen_height - (2 * border)
banner_x = border
banner_y = border

# Define gamebox dimensions
game_w = 500
game_h = screen_height - (2 *border)
game_x = banner_w + border -1
game_y = border 

# Define card1_rect dimensions
card1_rect_w = game_w - (2 * border)
card1_rect_h = 100
card1_rect_x = banner_w + (2 * border)
card1_rect_y = border + border + border

# Define card2_rect dimensions
card2_rect_w = game_w - (2 * border)
card2_rect_h = 100
card2_rect_x = banner_w + (2 * border)
card2_rect_y = card1_rect_y + card1_rect_h+ border + border

# Define yes_button dimensions
yes_button_w = (game_w - (3 * border))/2
yes_button_h = 75
yes_button_x = banner_w + (2 * border)
yes_button_y = card2_rect_y + card2_rect_h + border

# Define no_button dimensions
no_button_w = (game_w - (3 * border))/2
no_button_h = 75
no_button_x = yes_button_x + yes_button_w + (border)
no_button_y = card2_rect_y + card2_rect_h + border

# Define instr box dimensions
instr_w = game_w - (2 * border)
instr_h = 50
instr_x = banner_w + (2 * border)
instr_y = no_button_y + no_button_h + border + border

text_height = 30
box_label_text_height = 20
card1_label = (card1_rect_x, card1_rect_y - (box_label_text_height *1.1))
card2_label = (card2_rect_x, card2_rect_y - (box_label_text_height *1.1))
yes_button_note = (yes_button_x + 10, yes_button_y + yes_button_h + 5)
no_button_note = (no_button_x + 10, (no_button_y + no_button_h + 5))

# Defines scoreboard text placement
rounds_text_loc = (banner_x +15, banner_y + (2 * text_height))
max_rounds_text_loc = (banner_x +15, banner_y + (3 * text_height))
true_answers_text_loc = (banner_x +15, banner_y + (5 * text_height))
false_answers_text_loc = (banner_x +15, banner_y + (6 * text_height))
score_text_loc = (banner_x + 15, banner_y + (7 * text_height))

# Defines font sizes and styles
scoreb_font_size = 25
scoreb_font = pygame.font.SysFont("Arial", scoreb_font_size)
card_font_size = 30
card_font = pygame.font.SysFont("Arial", card_font_size)
instr_font_size = 18
instr_font = pygame.font.SysFont("Arial", instr_font_size)
y_button_font_size = 24
y_button_font = pygame.font.SysFont("Arial", y_button_font_size)



