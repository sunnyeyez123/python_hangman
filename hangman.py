
import random

#file = raw_input()
#TODO: LET USE CHOOSE DIFFICULTY



#Global Game Vars
chances = 6
missed = []
discovered = []
display = ""


#set up game by choosing the target word from a file

def game_setup():
	#read in options
	with open('hang_words.txt', 'r') as open_file:
	    all_text = open_file.read()

	word_list = all_text.split("\n")
	#choose random word
	target = word_list[random.randrange(0,len(word_list))]
	print target
	return target

"""Lets the user submit a letter guess, validates the input,
shows the letters they missed or reveals the word with the letters
they correctly guressed

"""

def guess_letter(target_word):
	global chances 
	global display
	target = target_word
	display = ""
	
	#TODO VALIDATE LEN
	#TODO VALIDATE ISLETTER .isalpha()
	#TODO VALIDATE LOWERCASE .lower()
	guess = raw_input("Guess a letter: ")
	print "You guessed:  %s" % guess 
	if guess not in target:
		print "That is not in the word."
		missed.append(guess)
		chances -=1
		print "Missed Letters: ",
		print missed
	else:
		discovered.append(guess)
		#TODO REVEAL GUESSED LETTERS
		for n in target:
			if n in discovered:
				display+= n
			else:
				display+='_'
		print display

#starts the game and shares the victory or defeat message

def play():

	target = game_setup()
	while chances >0:
		guess_letter(target)
		print "You hace %s gueeses remaining." % chances
		if display == target:
			print "You win!"
			break	
	else:
		print "Game Over! You Lose"



play()
