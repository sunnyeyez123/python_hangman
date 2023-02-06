
''' A revised game of hangman with two game modes. You can guess words at 3
difficulty levels or guess a common phrase. In each mode you only have 6
chances to guess the right letter. You also have the option to play again. '''

from ast import IsNot
import random
import sys
import json

#Global Game Vars
#Update in the 'Reset_values' method if you change these
chances = 6
missed = []
discovered = []
display = ""
username = ""
high_scores = {}
#these are never reset during a session
wins = 0
losses = 0


'''
Allows the user to choose between the two game types: words or phrases. 
'''
def choose_game_type():
	options = ['p', 'w', 'P', 'W']
	choice = input("Choose game type: w for words. p for phrases: ")
	if choice.isalpha():
		if len(choice) == 1:
			if choice in options:
				choice = choice.lower()
			else:
				print(bcolors.WARNING + "That's not one of the options I gave you. You never listen. Goodbye" + bcolors.ENDC)
				sys.exit()
		else:
			print(bcolors.WARNING + "I only need one letter. You never listen. Goodbye" + bcolors.ENDC)
			sys.exit()
	else: 
		print(bcolors.WARNING + "Letters only, gosh. You never listen. Goodbye" + bcolors.ENDC)
		sys.exit()

	return choice


def get_username():
	"""
	Allows the user to choose a username
	"""
	name = input("What's your name? ")

	if high_scores.get(name) is not None:
		print("Welcome back, " + name)
	else:
		print("Nice to meet you, " + name)

	print("I'll be keeping track of your highscore. Good Luck! " + '\n')

	return name


def choose_difficulty():
	""" Allows the user to choose the difficulty of a word game. chooses between
	easy, medium and hard wordlists."""
	options = ['e', 'E', 'n', 'N', 'h', 'H']

	choice = input("Choose difficulty: e for easy. n for normal. h for hard. ")
	if choice.isalpha():
		if len(choice) == 1:
			if choice in options:
				choice = choice.lower()
			else:
				print(bcolors.WARNING + "That's not one of the options I game you. You never listen. Goodbye" + bcolors.ENDC)
				sys.exit()
		else:
			print(bcolors.WARNING + "I only need one letter. You never listen. Goodbye" + bcolors.ENDC)
			sys.exit()
	else: 
		print(bcolors.WARNING + "Letters only, gosh. You never listen. Goodbye" + bcolors.ENDC)
		sys.exit()

	return choice


def choose_topic():
	""" Allows the user to choose the topic of the phrases for a phrase. There are currently
	options to choose idioms or slogans"""
	options = ['i', 'I', 's', 'S']

	choice = input("Choose difficulty: i for idioms. s for slogans: ")
	if choice.isalpha():
		if len(choice) ==1:
			if choice in options:
				choice = choice.lower()
			else:
				print(bcolors.WARNING + "That's not one of the options I game you. You never listen. Goodbye" + bcolors.ENDC)
				sys.exit()
		else:
			print(bcolors.WARNING + "I only need one letter. You never listen. Goodbye" + bcolors.ENDC)
			sys.exit()
	else: 
		print(bcolors.WARNING + "Letters only, gosh. You never listen. Goodbye" + bcolors.ENDC)
		sys.exit()

	return choice


def word_game_setup(difficulty):
	"""
	Set up game by choosing the target word from a file based on difficulty
	"""
	filename_map = {
		'e': 'easy_hang_words.txt',
		'n': 'normal_hang_words.txt',
		'h': 'hang_words.txt'
	}

	filename = filename_map.get(difficulty, 'easy_hang_words.txt')

	with open(filename, 'r') as open_file:
		all_text = open_file.read()

	word_list = all_text.split("\n")
	target = random.choice(word_list)

	return target


def phrase_game_setup(topic):
	"""
	Set up game by choosing the target phrase from a file based on topic
	"""
	all_text = ""

	if topic == 'i':
		with open('idioms.txt', 'r') as open_file:
			all_text = open_file.read()
	elif topic == 's':
		with open('slogans.txt', 'r') as open_file:
			all_text = open_file.read()

	phrase_list = all_text.split("\n")
	target = phrase_list[random.randrange(0, len(phrase_list))]
	target = target.lower()
	return target


def guess(targeted, game_type):
	"""
	Asks the user to submit a letter guess, then validates the input,
	shows the letters they missed or reveals the word with the letters
	they correctly guessed.

	"""
	global chances
	global display

	correct_guess_text = [
		"You guessed it!",
		"Nice job!",
		"That's right!",
		"I see what you did there.",
		"Keep it up!",
		"Just a few more to go!"
	]
	target = targeted
	display = ""
	try_to_solve = False

	guess = input("Guess a letter or type 'solve': ")

	if guess.isalpha():
		if len(guess) == 1:
			guess = guess.lower()
			if guess in target:
				if guess not in discovered:
					discovered.append(guess)
					print(correct_guess_text[random.randrange(0, len(correct_guess_text))])
				else:
					print(bcolors.WARNING + "You already guessed that. Try again." + bcolors.ENDC)
			else:
				if guess not in missed:
					missed.append(guess)
					print("That's not right. Try again.")
					chances -= 1
				else:
					print(bcolors.WARNING + "You already guessed that. Try again." + bcolors.ENDC)
			print("Missed Letters: ", missed)
		elif guess == "solve":
			try_to_solve = True
			if game_type == 'p':
				solution = input("Enter the full phrase: ")
			else:
				solution = input("Enter the full word: ")
		else:
			if guess == "exit" or guess == "quit":
				print("Thanks for playing")
				sys.exit()
			else:
				print(bcolors.WARNING + "You can only guess one letter at a time." + bcolors.ENDC)
	else:
		print(bcolors.WARNING + "Try guessing a letter" + bcolors.ENDC)

	if try_to_solve:
		result = you_win if solution == target else you_lose
		result(game_type, target)
	else:
		display = ""
		for n in target:
			display += (n + " ") if n in discovered else (' / ' if n == ' ' else '_ ')
		print(display)


def play():
	"""Starts the game, reviews the guessing progress and shares the victory or
	defeat message"""
	game_type = choose_game_type()
	if game_type == 'w':
		difficulty = choose_difficulty()
		target = word_game_setup(difficulty)
	elif game_type == 'p':
		topic = choose_topic()
		target = phrase_game_setup(topic)
	challenge = ""

	print("Alright, let's get started. Can you solve this? : \n")

	for letter in target:
		if letter == ' ':
			challenge += ' / '
		else:
			challenge += '_ '
	print(challenge)

	while chances > 0:

		current_guess = ""

		guess(target, game_type)
		print("You have %s guesses remaining." % chances)
		print()

		target_words = display.split("/")
		for word in target_words:
			current_guess += word.replace(" ", "") + " "
		if current_guess[len(current_guess)-1] == ' ':
			current_guess = current_guess[0:len(current_guess)-1]

		if current_guess == target:
			you_win(game_type, target)

	else:
		you_lose(game_type, target)
		

def you_win(game_type, target):
	""" Shares the victory messages depending on the game type"""
	global wins

	print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
	if game_type == 'p':
		print(f"That's right! The correct phrase was: {target}")
	else:
		print(f"That's right! The correct word was: {target}")

	wins += 1
	print(f"You've won {wins} time" + ("s" * (wins != 1)))
	print()
	play_again()


def you_lose(game_type, target):
	""" Shares the defeat messages depending on the game type"""
	global losses

	print(bcolors.FAIL + "Game Over! You Lose" + bcolors.ENDC)
	if game_type == 'p':
		print(f"The correct phrase was: {target}")
	else:
		print(f"The correct word was: {target}")

	losses += 1
	print(f"You've lost {losses} time" + ("s" * (losses != 1)))
	play_again()


def play_again():
	"""
	Asks the user if they want to play again. Kicks off a new game or ends the game session
	It also shares the win percentage and times played when leaving the session.
	"""
	save_highscore()
	again = input("Wanna play again? Y/N: ")
	if again.isalpha():
		if len(again) == 1:
			if again.lower() == 'y':
				print("Yay! Let's go again" + '\n')
				reset_values()
				play()
			else:
				print("Thanks for playing!")
				rounds = wins+losses
				percent = (float(wins)/rounds) * 100
				print("You played %d times" % rounds)
				print("You won %0.1f%% of games!" % percent)
				sys.exit()
		else:
			print("I'm going to assume you meant no")
			sys.exit()
	else:
		print("I'm going to assume you meant no")
		sys.exit()


def reset_values():
	"""
	Resets global game value variables
	"""
	global chances
	global missed
	global discovered
	global display
	global username

	chances = 6
	missed = []
	discovered = []
	display = ""
	username = ""


def save_highscore():
	"""
	Saves the high score of the current user
	"""
	global username
	global wins
	current_score = wins
	old_score = high_scores.get(username)

	if old_score is None or current_score > old_score:
		high_scores[username] = current_score
		f = open("highscores.json", "w")
		json.dump(high_scores, f, indent = 6)
		f.close()


def load_highscore():
	# Opening JSON file
	f = open('highscores.json',)
	# returns JSON object as 
	# a dictionary
	return json.load(f)


class bcolors:
	"""
	CLI colors
	"""

	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'


"""
The action starts here
"""
if __name__ == "__main__":
	print("Welcome to Hang_words.")
	print("You can quit the game by typing 'exit' or 'quit' instead of guessing a letter. ")
	print()
	high_scores = load_highscore()
	username = get_username()
	play()
