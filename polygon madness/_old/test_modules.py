from classes import *

def test_modules():
		#####this code is to test the Rectangle class
		def test_Rectangle():
			my_rect = Rectangle(20, 20, 100, 400, BLUE)
			my_rect.print_data()
			my_rect.display()
		test_Rectangle()
		#####this code is to test the Rectangle class


		#####this code is to test the Rectangle class
		def test_Text():
			my_text = Text("Hello partner", 400, 500)
			my_text.print_data()
			my_text.display()
		test_Text()
		#####this code is to test the Rectangle class

		#####this code is to test the Rectangle class
		def test_Text_Box():
			my_test_box = Text_Box(200,200,300,300,WHITE, BLACK,"WHAT'S UP????",myfont)
			my_test_box.display()
		test_Text_Box()
		#####this code is to test the Rectangle class

		######this is test code for the Card class
		def test_Card(): 
			card1_x = 450
			card1_y = 300
			card1_w = 100
			card1_h = 100	
			card1_color = WHITE
			card1_text_color = RED
			card1 = Card("Card1")
			card1.text_box(card1_x, card1_y, card1_w, card1_h, card1_color, card1_text_color, "string", myfont)
			card1.card_text_box.display()
			card1.create_data()
			card1.print_data()
			card1.display_data()
		test_Card()




