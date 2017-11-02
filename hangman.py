
import random
import sys

'''
Feature improvements
#TODO make it so you can keep playing
#TODO keep track of wins/loses in a session
'''

#Global Game Vars
chances = 6
missed = []
discovered = []
display = ""
wins = 0
losses = 0


'''
allows the user to choose the difficulty of the game. chooses between easy, medium and hard wordlists
'''

def choose_difficulty():
	difficulty = ""
	choice = raw_input("Choose difficulty: e for easy. n for normal. h for hard. ")
	if choice.isalpha():
		if len(choice) ==1:
			if choice == 'e' or choice == 'n' or choice == 'h':
				choice = choice.lower()
			else:
				print "You never listen. Goodbye"
				sys.exit()
		else:
			print "You never listen. Goodbye"
			sys.exit()
	else: 
		print "You never listen. Goodbye"
		sys.exit()


	return choice


'''
Set up game by choosing the target word from a file
'''

def game_setup(difficulty):

	all_text = ""

	if(difficulty) == 'e':
		with open('easy_hang_words.txt', 'r') as open_file:
		    all_text = open_file.read()
	elif difficulty == 'n':
		with open('normal_hang_words.txt', 'r') as open_file:
		    all_text = open_file.read()
	elif difficulty =='h':
	#read in options
		with open('hang_words.txt', 'r') as open_file:
		    all_text = open_file.read()

	word_list = all_text.split("\n")
	#choose random word
	target = word_list[random.randrange(0,len(word_list))]
	print target
	return target

"""
Lets the user submit a letter guess, validates the input,
shows the letters they missed or reveals the word with the letters
they correctly guessed

"""

def guess_letter(target_word):
	correct_guess_text = ["You guessed it!", "Nice job!","That's right!","I see what you did there.", "Keep it up!", "Just a few more to go!"]
	global chances 
	global display
	target = target_word
	display = ""

	guess = raw_input("Guess a letter: ")


	if guess.isalpha():
		if len(guess) ==1:
			guess = guess.lower()
			#print "You guessed:  %s" % guess 
			if guess not in target:
				if guess not in missed:
					missed.append(guess)
					print "That's not right. Try again"
					chances -=1
				else:
					print "You already guessed that. Try again"
				print "Missed Letters: ",				
				print missed
			else:
				if guess not in discovered:
					discovered.append(guess)
					print correct_guess_text[random.randrange(0, len(correct_guess_text))]
				else:
					print "You already guessed that. Try again"

		else:
			if guess == "exit" or guess == "quit":
				sys.exit()
			else:
				print "You can only guess one letter at a time"
	else:
		print "Try guessing a letter"

	for n in target:
		if n in discovered:
			display+= n + ' '
		else:
			display+='_ '
	print display 


'''starts the game and shares the victory or defeat message'''

def play():
	global wins
	global losses
	difficulty = choose_difficulty()

	target = game_setup(difficulty)
	while chances >0:
		guess_letter(target)
		print "You hace %s gueeses remaining." % chances
		if display.replace(" ", "") == target:
			print "That's right! The correct word is: %s" % target
			print "You win!"
			wins+=1
			print "You've won %d times" % wins
 			play_again()	
	else:
		print "Game Over! You Lose"
		print "The correct word was: %s" % target
		losses+=1
		print "You've lost %d time(s)" % losses

		play_again()

def play_again():
	again = raw_input("Wanna play again? Y/N: ")
	if again.isalpha():
		if len(again) ==1:
			if again.lower() == 'y':
				reset_values()
				play()
			else:
				print "Thanks for playing!"
				percent =(float(wins)/(wins+losses)) * 100
				print "You won %0.1f%% of games" % percent
				sys.exit()
		else:
			print "I only wanted one letter. You never listen. Goodbye"
			sys.exit()
	else:
		print "C'mon I asked for letters. You never listen. Goodbye"
		sys.exit()

def reset_values():
	global chances
	global missed
	global discovered
	global display

	chances = 6
	missed = []
	discovered = []
	display = ""


play()
