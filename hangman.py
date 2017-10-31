
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
	target = word_list[random.randrange(0,len(word_list))]
	print target

#gets the user to submit a letter guess	

def guess_word():
	guess = raw_input("Guess a letter: ")
	print "You guessed:  %s" % guess 



def play():
	game_setup()
	guess_word()


play()
