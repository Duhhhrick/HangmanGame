#hangman clone
#creates a list out of wordlist.txt and selects a random word. Images.py stores image assets
#works as intended, could be condensed and written cleaner
import random
import os
import images

print(images.logo)
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

my_file = open("wordlist.txt", "r")
words = []
for line in my_file:
	words.append(line.strip())

is_done = False
health = 6
guessed_letters = []
#choose word from list
num = random.randint(0, len(words) - 1)
chosen_word = words[num]
print("Welcome to hangman!")
print("")
#create line equal to letters
line = []
num_count = len(chosen_word) - 1
while num_count >= 0:
	line.append("_ ")
	num_count -= 1
print(*line)


#guess letter 
while is_done == False and health >= 1:
	print(images.images[health])
	guess = input("please guess a letter: ").lower()
	counter = 0
	correct = False
	clearConsole()
	#check if guess is correct
	if guess in guessed_letters:
		print("You've already guessed this letter!")
		pass
	else:
		guessed_letters.append(guess)
		for item in chosen_word:
			if guess == item:
				line[counter] = guess
				counter += 1
				correct = True
			else:
				counter += 1
				
		if correct == False:
			health -= 1

	print(*line)
	if line.__contains__("_ "):
		is_done = False
	else:
		is_done = True
		
	
if is_done == True:
	print("You guessed the word!")
else:
	print("You died!")
	print(f"The word was {chosen_word}")
	
#this comment is a test
