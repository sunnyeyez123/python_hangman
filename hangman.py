
import random

#file = raw_input()
#TODO: LET USE CHOOSE DIFFICULTY


#set up game by choosing the target word from a file
chances = 6

def game_setup():
	#read in options
	with open('hang_words.txt', 'r') as open_file:
	    all_text = open_file.read()

	word_list = all_text.split("\n")
	#choose random word
	target = word_list[random.randrange(0,len(word_list))]
	print target

#gets the user to submit a letter guess	

def guess_letter():
	#TODO VALIDATE LEN
	#TODO VALIDATE ISLETTER
	#TODO VALIDATE LOWERCASE
	guess = raw_input("Guess a letter: ")
	print "You guessed:  %s" % guess 



def play(chances):

	life = chances
	game_setup()
	while life >0:
		guess_letter()
		life -=1
	print "Game Over! You Lose"


play(chances)
