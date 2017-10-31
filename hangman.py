
import random

#file = raw_input()
#TODO: LET USE CHOOSE DIFFICULTY


#set up game by choosing the target word from a file

def game_setup():
	#read in options
	with open('hang_words.txt', 'r') as open_file:
	    all_text = open_file.read()

	word_list = all_text.split("\n")
	#choose random word
	target = random.randrange(0,len(new))
	print target

def guess_word()



def play():
	game_setup()




play()
